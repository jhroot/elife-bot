import time
import json
from provider import process
from optparse import OptionParser
from S3utility.s3_sqs_message import S3SQSMessage
import boto.sqs
import settings as settings_lib
import log
import os
import requests

import newrelic.agent


def work(ENV, flag):
    # Specify run environment settings
    settings = settings_lib.get_settings(ENV)

    # Log
    identity = "exeter_event_notifier_%s" % os.getpid()
    log_file = "exeter_event_notifier.log"
    # logFile = None
    logger = log.logger(log_file, settings.setLevel, identity)

    # Simple connect
    conn = boto.sqs.connect_to_region(settings.sqs_region,
                                      aws_access_key_id=settings.aws_access_key_id,
                                      aws_secret_access_key=settings.aws_secret_access_key)
    queue = conn.get_queue(settings.exeter_notifier_queue)
    queue.set_message_class(S3SQSMessage)

    application = newrelic.agent.application()

    # Poll for an activity task indefinitely
    if queue is not None:
        while flag.green():

            logger.info('reading message')
            queue_message = queue.read(30)

            if queue_message is None:
                logger.info('no messages available')
            else:
                with newrelic.agent.BackgroundTask(application, name=queue_message.notification_type,
                                                   group='exeter_event_notifier.py'):
                    logger.info('got message id: %s' % queue_message.id)

                    # process incoming message
                    process_message(settings, logger, queue_message)

                    # cancel incoming message from queue
                    logger.info("cancelling message")
                    queue.delete_message(queue_message)
                    logger.info("message cancelled")

            time.sleep(10)
        logger.info("graceful shutdown")

    else:
        logger.error('error obtaining queue')


def process_message(settings,logger,  message):

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    outer_body = json.loads(message.get_body())
    if 'Message' not in outer_body:
        logger.error("Incorrect incoming message format")
        return
    message = json.loads(outer_body['Message'])
    r = requests.post(settings.exeter_notification_endpoint, data=json.dumps(message), headers=headers)
    if r.status_code != 200:
        logger.error("Could not contact exeter notification endpoint")
        # TODO : retry policy?

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-e", "--env", default="dev", action="store", type="string", dest="env",
                      help="set the environment to run, either dev or live")
    (options, args) = parser.parse_args()
    if options.env:
        ENV = options.env
    process.monitor_interrupt(lambda flag: work(ENV, flag))
