======
Publication Email activity
======

Also known as the author email.

# Overview

The ``PublicationEmail`` activity sends emails to the authors and editors of an eLife article when it is first published. The activity is added to the list of steps in the ``PublishArticle`` workflow.

* Author and editor data comes from the ``ejp.py`` provider.
* Article data comes from the ``article.py`` provider.
* Email content is formatted by the ``templates.py`` provider, using optional jinja2 syntax.

# Rough activity steps

1. A starter starts a ``PublishArticle`` workflow execution. The input data is like, for example:

  ```
  {"data": {"allow_duplicates": false, "elife_id": "00778", "document": "https://s3.amazonaws.com/elife-articles-dev/00778/elife_2013_00778.xml.zip"}}
    
  ```
  
1. As part of the workflow steps, ``worker.py`` receives an activityTask token from Amazon SWF with the activity type ``PublicationEmail``.
1. ``worker.py`` instantiates a ``activity_PublicationEmail`` class (in the ``activity/activity_PublicationEmail.py file) and calls its ``do_activity()`` method.
1. The activity object uses the ``templates.py`` provider to "warm" the email templates. Basically, it connects to the ``templates_bucket`` S3 bucket and downloads the list of objects needed for sending emails and saves them as files to the activity's tmp_dir directory.
1. The elife provider object supplies the ``submit_url`` and ``facebook_url`` used in templates.
1. The article provider gets data for the particular article from the latest article XML stored in the ``bucket`` S3 bucket.
1. The ejp provider gets a list of authors of the particular article from files stored in the ``ejp_bucket`` S3 bucket.
1. For each author, the headers and body of an email is formatted using the templates.
1. If ``allow_duplicates`` is ``False``, then it will check if a similar email was already sent previously. The combination of doi_id, email_type and recipient_email is used to check for duplicates.
1. If there is no duplicate email, or allow_duplicates is "True", then the email is added to the SimpleDB ``EmailQueue``.
1. Similarly, for each editor an email is formatted, checked for duplicates, and added to the email queue.

Unsent emails in the ``EmailQueue`` are automatically sent using Amazon SES in batches of 100 every 5 minutes, in normal operation of the eLife bot.

The email will be queued for delivery on the article's publication date. Therefore, if the article's publication date is before today, the emails will effectively be sent immediately; if the article's publication date is after today, the emails will be queued to send at a future date.

At this time, when ``starter/starter_PublishArticle.py`` is run on the ``dev`` environment, ``allow_duplicates`` is set to ``True``. This allows for easy testing on the files in the dev environment.

# Templates and jinja details

## Overview

Template files are stored in a folder named ``email`` in the ``templates_bucket`` S3 bucket. These can be edited and replaced, but they must be syntactically correct.

Each email uses a pair of template files: the headers file has the file extension ``.json``, and the body file has the file extension ``.html``.

## Email header template

Example headers file: named ``author_publication_email.json``:

```
{
  "sender_email": "press@elifesciences.org",
  "email_type": "author_publication_email",
  "subject": "{{ author.first_nm }}, Your eLife paper is now online"
}
`` `

* ``sender_email`` is the sender, and must be validated with Amazon SES before it can be used as a sender
* ``email_type`` is used to determine whether duplicate emails exist of this type
* ``subject`` can use jijna syntax for at least variable substitution

## Email body template

Example email body file: named ``author_publication_email.html``:

```
{% include "email_header.html" %}
<p>Dear {{ author.first_nm }},</p>

<p>Congratulations, your paper has now been published by eLife! You can <a href="{{ article.doi_url }}">read it</a> online. You can also try out our new experimental <a href="{{ article.lens_url }}">online viewer</a>.</p>

<p>To help share the results, you can send <a href="{{ article.tweet_url }}">a tweet</a> about your paper, or you can like your paper on our <a href="{{ elife.facebook_url }}">facebook page</a>.</p>

<p>We hope you'll want to publish with eLife again in the future. In the meantime, please consider encouraging your colleagues to <a href="{{ elife.submit_url }}">submit</a> their best work to eLife too.</p>

<p>Best wishes,</p>

<p>Jenny</p>
{% include "email_footer.html" %}
```

* email header and footer files can be included because the templates provider sets the tmp_dir as its jinja environment
* author object has a first name, as well as the recipient email address used in the system logic code
* editor object is used in editor templates, in the same way author is used in author templates (e.g. author.first_nm in author email template, editor.first_nm in editor email templates)
* article object has data about the particular article
* elife object has some default elife values

# Article object

The data about the article to be used is currently limited, and is parsed out of the article XML.

# EJP provider, author and editor data

Author and editor data is exported daily from EJP (e Journal Press) to the ``ejp_bucket`` S3 bucket. It is CSV data. The EJP provider gets a list of all objects in the bucket. It filters the list of objects by file name for only a particular type of query that generated the file. It also sorts by last_modified date to find the latest of this file type.

Once the content from the particular file is downloaded from S3, the CSV is parsed. Column headers and data rows are extracted. These are used by the ``PublicationEmail`` activity to build author and editor data.






