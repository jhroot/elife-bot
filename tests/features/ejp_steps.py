from lettuce import *
import activity
import json
import datetime
import os
import provider.ejp as ejplib

@step('I create a ejp provider')
def i_create_a_ejp_provider(step):
  try:
    world.settings = world.settings
  except AttributeError:
    world.settings = None

  world.ejp = ejplib.EJP(world.settings, world.tmp_dir)
  assert world.ejp is not None, \
    "Got ejp %s" % world.ejp
    
@step('I parse author file the document with ejp')
def i_parse_author_file_the_document_with_ejp(step):
  (world.column_headings, world.author_rows) = world.ejp.parse_author_file(world.document, world.filename)
  assert world.ejp.fs.document is not None, \
    "Got document %s" % world.ejp.fs.document

@step('I get the ejp fs document') 
def i_get_the_ejp_fs_document(step):
  world.ejp_document = world.ejp.fs.get_document()
  assert world.ejp_document is not None, \
    "Got ejp_document %s" % world.ejp_document
    
@step('I have the ejp document (\S+)')
def i_have_the_ejp_document_count_count(step, ejp_document):
  assert world.ejp_document == ejp_document, \
    "Got ejp_document %s" % world.ejp_document

@step('I have the column headings (.+)')
def i_have_the_column_headings(step, column_headings):
  assert str(world.column_headings) == str(column_headings), \
    "Got column_headings %s " % str(world.column_headings)

@step('I have the authors count (\d+)')
def i_have_the_authors_count(step, count):
  assert len(world.authors) == int(count), \
    "Got count %s " % len(world.authors)
  
@step('I get the authors from ejp')
def i_get_the_authors_from_ejp(step):
  try:
    world.corr = world.corr
  except AttributeError:
    world.corr = None
  
  (world.column_headings, world.authors) = world.ejp.get_authors(world.doi_id, world.corr, world.document)
  assert world.authors is not None, \
    "Got authors %s" % world.authors
  
@step('I have corresponding (\S+)')
def i_have_corresponding(step, corr):
  if(corr == "None"):
    world.corr = None
    assert world.corr is None, \
      "Got corr %s" % world.corr
  elif(corr == "True"):
    world.corr = True
    assert world.corr is True, \
      "Got corr %s" % world.corr
  elif(corr == "False"):
    world.corr = False
    assert world.corr is False, \
      "Got corr %s" % world.corr
  else:
    world.corr = corr
    assert world.corr is not None, \
      "Got corr %s" % world.corr