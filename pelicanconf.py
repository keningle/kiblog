#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import urllib, hashlib

AUTHOR = u'Ken Ingle'
SITENAME = u'KenIngle.com'
SITEURL = ''

# Conf for pulling Gravatar Image
EMAIL = u'kingle@gmail.com'
DEFAULT_GRV_URL = u'http://www.example.com/default.jpg'
GRV_SIZE = 120

# construct gravatar URL
GRV_URL = "http://www.gravatar.com/avatar/" + hashlib.md5(EMAIL.lower()).hexdigest() + "?"
GRV_URL += urllib.urlencode({'d':DEFAULT_GRV_URL, 's':str(GRV_SIZE)})

SITESUBTITLE = u'Random thoughts about technology, travel and other things that interest me.'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('Github', 'https://github.com/keningle'),
		  ('Twitter', 'http://twitter.com/ken_ingle'),
          ('LinkedIn', 'http://www.linkedin.com/in/kingle'),
          )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Selec the theme
THEME = 'themes/github-sundown'
