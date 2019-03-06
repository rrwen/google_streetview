# -*- coding: utf-8 -*-

__name__ = 'google_streetview'
__author__ = 'Richard Wen'
__email__ = 'rrwen.dev@gmail.com'
__version__ = '1.2.9'
__license__ = 'MIT'
__description__ = 'A command line tool and module for Google Street View Image API.'
__long_description_content_type__='text/markdown'
__keywords__ = [
  'google',
  'api',
  'street',
  'view',
  'streetview',
  'image',
  'map',
  'address',
  'location',
  'road',
  'route',
  'city',
  'panorama',
  'photo',
  'cli',
  'command', 
  'line',
  'interface',
  'tool',
  'module']
__url__ = 'https://github.com/rrwen/google_streetview'
__download_url__ = 'https://github.com/rrwen/google_streetview/archive/master.zip'
__install_requires__ = [
  'kwconfig',
  'requests'
]
__packages__ = ['google_streetview']
__package_data__ = {'google_streetview': ['config.json']}
__entry_points__ = {'console_scripts': ['google_streetview=google_streetview.cli:run']}
