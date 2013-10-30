import json
import random
import datetime
import calendar
import time
from operator import itemgetter, attrgetter

import boto.s3
from boto.s3.connection import S3Connection

import filesystem as fslib

"""
EJP data provider
Connects to S3, discovers, downloads, and parses files exported by EJP
"""

class EJP(object):
  
  def __init__(self, settings = None, tmp_dir = None):
    self.settings = settings
    self.tmp_dir = tmp_dir
    
    # Default tmp_dir if not specified
    self.tmp_dir_default = "ejp_provider"
    
    # Default S3 bucket name
    self.bucket_name = None
    if(self.settings is not None):
      self.bucket_name = self.settings.ejp_bucket
    
    # S3 connection
    self.s3_conn = None
    
    # Filesystem provider
    self.fs = None
    
    # Some EJP file types we expect
    self.latest_author_file = None
    self.latest_editor_file = None
    
  def connect(self):
    """
    Connect to S3 using the settings
    """
    s3_conn = S3Connection(self.settings.aws_access_key_id, self.settings.aws_secret_access_key)
    return self.s3_conn

  def get_bucket(self, bucket_name = None):
    """
    Using the S3 connection, lookup the bucket
    """
    if(self.s3_conn is None):
      s3_conn = self.connect()
    else:
      s3_conn = self.s3_conn
    
    if(bucket_name is None):
      # Use the object bucket_name if not provided
      bucket_name = self.bucket_name
    
    # Lookup the bucket
    bucket = s3_conn.lookup(bucket_name)

    return bucket

  def get_s3key(self, s3key, bucket = None):
    """
    Get the S3 key from the bucket
    If the bucket is not provided, use the object bucket
    """
    if(bucket is None):
      bucket = self.bucket
    
    s3key = boto.s3.key.Key(bucket)
    
    return s3key


  def parse_author_file(self, document):
    """
    Given a filename to an author file, download
    or copy it using the filesystem provider,
    then parse it
    """

    if(self.fs is None):
      self.fs = self.get_fs()
    
    self.fs.write_document_to_tmp_dir(document)
    content = self.fs.read_document_from_tmp_dir(self.fs.document)
    
    author_parsed = self.parse_author_data(author_data = content)
    
    return author_parsed
  
  def parse_author_data(self, author_data):
    """
    Given author data - CSV with header rows - parse
    it and return an object representation
    """
    
    #### TO DO !!!!!!!!
    author_parsed = author_data
    
    return author_parsed
  
  def get_fs(self):
    """
    For running tests, return the filesystem provider
    so it can be interrogated
    """
    if(self.fs is None):
      # Create the filesystem provider
      self.fs = fslib.Filesystem(self.get_tmp_dir())
    return self.fs
  
  def get_tmp_dir(self):
    """
    Get the temporary file directory, but if not set
    then make the directory
    """
    if(self.tmp_dir):
      return self.tmp_dir
    else:
      self.tmp_dir = self.tmp_dir_default
      
    return self.tmp_dir