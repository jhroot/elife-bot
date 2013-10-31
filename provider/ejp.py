import json
import random
import datetime
import calendar
import time
from operator import itemgetter, attrgetter

import csv

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
    self.author_default_filename = "authors.csv"
    self.editor_default_filename = "editors.csv"
    
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


  def parse_author_file(self, document, filename = None):
    """
    Given a filename to an author file, download
    or copy it using the filesystem provider,
    then parse it
    """

    if(self.fs is None):
      self.fs = self.get_fs()
    
    # Save the document to the tmp_dir
    self.fs.write_document_to_tmp_dir(document, filename)

    (column_headings, author_rows) = self.parse_author_data(self.fs.document)
    
    return (column_headings, author_rows)
  
  def parse_author_data(self, document):
    """
    Given author data - CSV with header rows - parse
    it and return an object representation
    """
    
    column_headings = None
    author_rows = []
    
    f = self.fs.open_file_from_tmp_dir(self.fs.document, mode = 'rb')

    filereader = csv.reader(f)

    for row in filereader:
      # For now throw out header rows
      if(filereader.line_num <= 3):
        pass
      elif(filereader.line_num == 4):
        # Column headers
        column_headings = row
      else:
        author_rows.append(row)

    return (column_headings, author_rows)
  
  def get_authors(self, doi_id = None, corresponding = None, document = None):
    """
    Get a list of authors for an article
      If doi_id is None, return all authors
      If corresponding is
        True, return corresponding authors
        False, return all but corresponding authors
        None, return all authors
      If document is None, find the most recent authors file
    """
    authors = []
    # Check for the document
    if(document is None):
      # No document? Find it on S3, save the content to
      #  the tmp_dir
      if(self.fs is None):
        self.fs = self.get_fs()
      s3_key = self.find_latest_file(file_type = "author")
      contents = s3_key.get_contents_as_string()
      self.fs.write_content_to_document(contents, self.author_default_filename)
      document = self.fs.get_document
    
    # Parse the author file
    filename = self.author_default_filename
    (column_headings, author_rows) = self.parse_author_file(document, filename)
    
    if(author_rows):
      for a in author_rows:
        add_author = True
        # Check doi_id column value
        if(doi_id is not None):
          if(int(doi_id) != int(a[0])):
            add_author = False
        # Check corresponding column value
        if(corresponding and add_author is True):
          
          author_type_cde = a[5]
          dual_corr_author_ind = a[6]
          is_corr = self.is_corresponding_author(author_type_cde, dual_corr_author_ind)
          
          if(corresponding is True):
            # If not a corresponding author, drop it
            if(is_corr is not True):
              add_author = False
          elif(corresponding is False):
            # If is a corresponding author, drop it
            if(is_corr is True):
              add_author = False
              
        # Finish up, add the author if we should
        if(add_author is True):
          authors.append(a)

    if(len(authors) <= 0):
      authors = None
    
    return (column_headings, authors)
    
  def is_corresponding_author(self, author_type_cde, dual_corr_author_ind):
    """
    Logic for checking whether an author row is for
    a corresponding author. Can be either "Corresponding Author"
    or "dual_corr_author_ind" column is 1
    """
    is_corr = None
    
    if(author_type_cde == "Corresponding Author" or dual_corr_author_ind == "1"):
      is_corr = True
    else:
      is_corr = False
      
    return is_corr
    
  def find_latest_file(self, file_type):
    """
    Given the file_type, find the S3 key of the object
    for the latest file in the S3 bucket
      file_type options: author, editor
    """
    
    ####### TODo !!!!!!
    
    return s3_key
  
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