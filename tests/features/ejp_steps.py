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
  world.author_parsed = world.ejp.parse_author_file(world.document)
  assert world.ejp.fs.document is not None, \
    "Got document %s" % world.ejp.fs.document

@step('I get the ejp fs document') 
def i_get_the_ejp_fs_document(step):
  world.ejp_document = world.ejp.fs.get_document()
  assert world.ejp_document is not None, \
    "Got ejp_document %s" % world.ejp_document
    
@step('Then I have the ejp document (\S+)')
def i_have_the_ejp_document_count_count(step, ejp_document):
  assert world.ejp_document == ejp_document, \
    "Got ejp_document %s" % world.ejp_document


