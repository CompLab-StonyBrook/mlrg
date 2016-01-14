#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Graf'
SITENAME = u'MathLing@SBU'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
FEED_MAX_ITEMS = 8

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = 'themes/pelican-simplegrey'
HOME_NEWS_COUNT = 5


DELETE_OUTPUT_DIRECTORY = True
LOAD_CONTENT_CACHE = False
TYPOGRIFY = True

DEFAULT_DATE = 'fs'

INDEX_SAVE_AS = 'news.html'
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/README.md', 'extra/robots.txt']
STATIC_EXCLUDE_SOURCES = False
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/README.md': {'path': 'README.md'},
    'extra/CNAME': {'path': 'CNAME'},
}
