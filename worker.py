import boto.swf
import settings as settingsLib
import log
import json
import random
import datetime
import os
import importlib
import time
from multiprocessing import Process
from optparse import OptionParser

import activity
from activity.activity import activity as activitybase
# Add parent directory for imports, so activity classes can use elife-api-prototype
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

"""
Amazon SWF worker
"""

def work(ENV = "dev"):
	# Specify run environment settings
	settings = settingsLib.get_settings(ENV)

	# Log
	identity = "worker_%s" % int(random.random() * 1000)
	logFile = "worker.log"
	#logFile = None
	logger = log.logger(logFile, settings.setLevel, identity)

	# Simple connect
	conn = boto.swf.layer1.Layer1(settings.aws_access_key_id, settings.aws_secret_access_key)

	token = None

	# Poll for an activity task indefinitely
	while(True):
		if(token == None):
			logger.info('polling for activity...')
			activity_task = conn.poll_for_activity_task(settings.domain, settings.default_task_list, identity)

			token = get_taskToken(activity_task)

			logger.info('got activity: [json omitted], token %s' % token)
			#logger.info('got activity: \n%s' % json.dumps(activity_task, sort_keys=True, indent=4))



			# Complete the activity based on data and activity type
			success = False
			if(token != None):
				# Get the activityType and attempt to do the work
				activityType = get_activityType(activity_task)
				if(activityType != None):
					logger.info('activityType: %s' % activityType)

					# Build a string for the object name
					activity_name = get_activity_name(activityType)

					# Attempt to import the module for the activity
					if(import_activity_class(activity_name)):
						# Instantiate the activity object
						activity_object = get_activity_object(activity_name, settings, logger, conn, token, activity_task)

						# Get the data to pass
						data = get_input(activity_task)

						# Do the activity
						try:
							activity_result = activity_object.do_activity(data)
						except Exception as e:
							logger.error('error executing activity %s' % activity_name, exc_info=True)

						# Print the result to the log
						logger.info('got result: \n%s' % json.dumps(activity_object.result, sort_keys=True, indent=4))

						if type(activity_result) == str:
							if activity_result == activitybase.ACTIVITY_SUCCESS:
								message = activity_object.result
								respond_completed(conn, logger, token, message)
							elif activity_result == activitybase.ACTIVITY_TEMPORARY_FAILURE:
								reason = 'error: activity failed with result ' + str(activity_object.result)
								detail = ''
								respond_failed(conn, logger, token, detail, reason)
							else:
								# (activitybase.ACTIVITY_PERMANENT_FAILURE)
								reason = 'error: activity failed with result ' + str(activity_object.result)
								detail = ''
								signal_cancel_workflow(conn, logger, settings.domain,
													 activity_task['workflowExecution']['workflowId'],
													 activity_task['workflowExecution']['runId'])

						else:
							# for legacy actions

							# Complete the activity task if it was successful
							if activity_result:
								message = activity_object.result
								respond_completed(conn, logger, token, message)
							else:
								reason = 'error: activity failed with result ' + str(activity_object.result)
								detail = ''
								respond_failed(conn, logger, token, detail, reason)

					else:
						reason = 'error: could not load object %s\n' % activity_name
						detail = ''
						respond_failed(conn, logger, token, detail, reason)
						logger.info('error: could not load object %s\n' % activity_name)

		# Reset and loop
		token = None

def get_input(activity_task):
	"""
	Given a response from polling for activity from SWF via boto,
	extract the input from the json data
	"""
	try:
		input = json.loads(activity_task["input"])
	except KeyError:
		input = None
	return input

def get_taskToken(activity_task):
	"""
	Given a response from polling for activity from SWF via boto,
	extract the taskToken from the json data, if present
	"""
	try:
		return activity_task["taskToken"]
	except KeyError:
		# No taskToken returned
		return None

def get_activityType(activity_task):
	"""
	Given a polling for activity response from SWF via boto,
	extract the activityType from the json data
	"""
	try:
		return activity_task["activityType"]["name"]
	except KeyError:
		# No activityType found
		return None

def get_activity_name(activityType):
	"""
	Given an activityType, return the name of a
	corresponding activity class to load
	"""
	return "activity_" + activityType

def import_activity_class(activity_name):
	"""
	Given an activity subclass name as activity_name,
	attempt to lazy load the class when needed
	"""
	try:
		module_name = "activity." + activity_name
		importlib.import_module(module_name)
		# Reload the module, in case it was imported before
		reload_module(module_name)
		return True
	except ImportError as e:
		return False

def reload_module(module_name):
	"""
	Given an module name,
	attempt to reload the module
	"""
	try:
		reload(eval(module_name))
	except:
		pass

def get_activity_object(activity_name, settings, logger, conn, token, activity_task):
	"""
	Given an activity_name, and if the module class is already
	imported, create an object an return it
	"""
	full_path = "activity." + activity_name + "." + activity_name
	f = eval(full_path)
	# Create the object
	activity_object = f(settings, logger, conn, token, activity_task)
	return activity_object

def respond_completed(conn, logger, token, message):
	"""
	Given an SWF connection and logger as resources,
	the token to specify an accepted activity and a message
	to send, communicate with SWF that the activity was completed
	"""
	try:
		out = conn.respond_activity_task_completed(token,str(message))
		logger.info('respond_activity_task_completed returned %s' % out)
	except boto.exception.SWFResponseError:
		logger.info('SWFResponseError: SWFResponseError: 400 Bad Request on respond_completed')

def respond_failed(conn, logger, token, details, reason):
	"""
	Given an SWF connection and logger as resources,
	the token to specify an accepted activity, details and a reason
	to send, communicate with SWF that the activity failed
	"""
	try:
		out = conn.respond_activity_task_failed(token,str(details),str(reason))
		logger.info('respond_activity_task_failed returned %s' % out)
	except boto.exception.SWFResponseError:
		logger.info('SWFResponseError: SWFResponseError: 400 Bad Request on respond_failed')

def signal_cancel_workflow(conn, logger,  domain, workflow_id, run_id):
	"""
	Given an SWF connection and logger as resources,
	the token to specify an accepted activity, details and a reason
	to send, communicate with SWF that the activity failed
	and the workflow should be abandoned
	"""
	try:
		out = conn.request_cancel_workflow_execution(domain,workflow_id, run_id=run_id  )
		logger.info('request_cancel_workflow_execution %s' % out)
	except boto.exception.SWFResponseError:
		logger.info('SWFResponseError: SWFResponseError: 400 Bad Request on respond_failed')

def start_single_thread(ENV):
	"""
	Start in single process / threaded mode, but
	return a pool resource of None to indicate it
	is running in a single thread
	"""
	print 'starting single thread'
	work(ENV)
	return None

def start_multiple_thread(ENV):
	"""
	Start multiple processes using a manual pool
	"""
	pool = []
	for num in range(forks):
		p = Process(target=work, args=(ENV,))
		p.start()
		pool.append(p)
		print 'started worker thread'
		# Sleep briefly so polling connections do not happen at once
		time.sleep(0.5)
	return pool

def monitor_KeyboardInterrupt(pool = None):
	# Monitor for keyboard interrupt ctrl-C
	try:
		time.sleep(10)
	except KeyboardInterrupt:
		print 'caught KeyboardInterrupt, terminating threads'
		if(pool != None):
			for p in pool:
				p.terminate()
		return False
	return True

if __name__ == "__main__":

	# Add options
	parser = OptionParser()
	parser.add_option("-e", "--env", default="dev", action="store", type="string", dest="env", help="set the environment to run, either dev or live")
	parser.add_option("-f", "--forks", default=10, action="store", type="int", dest="forks", help="specify the number of forks to start")
	(options, args) = parser.parse_args()
	if options.env:
		ENV = options.env
	if options.forks:
		forks = options.forks

	pool = None
	try:
		if(forks > 1):
			pool = start_multiple_thread(ENV)
		else:
			pool = start_single_thread(ENV)
	except Exception as e:
 		log ("Exception: " + e.message)

	# Monitor for keyboard interrupt ctrl-C
	loop = True
	while(loop):
		loop = monitor_KeyboardInterrupt(pool)


