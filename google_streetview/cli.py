# -*- coding: utf-8 -*-

"""
  Usage:
    google_streetview [--optional]
    google_streetview [-positional] ...
  
  A command line tool for Google Street View search.
  
  Positional arguments:
    -h                show this help message and exit
    -i                show documentation in browser
    -a                show optional arguments in browser
    -s <arg>=<value>  set default optional arguments
    -r <arg>          remove default arguments
    -v                view default arguments
    -d                reset default arguments
  
  Optional arguments:
    --pano            panorama ids (req)
    --location        text or latitude/longitude (req)
    --size            image size (default: 640x640)
    --heading         camera heading 0 to 360
    --fov             camera zoom up 120 (default: 90)
    --pitch           camera angle 90 to -90 (default: 0)
    --site_api        base url for api site
    --site_metadata   base url for metadata site
    --save_links      path for links text file
    --save_metadata   path for metadata JSON file
    --save_downloads  path for directory of image downloads
    --option_silent   'True' to disable preview
    --option_preview  num of results to preview
    
    For more arguments use: google_streetview -a
    
  Examples:
    
    Set developer key arguments
      > google_streetview -s key="dev_key"
    
    Get street view image using location
      > google_streetview --location=46.414382,10.013988
      > google_streetview --location=46.414382,10.013988;40.720032,-73.988354
    
    Get street view image using panorama id
      > google_streetview --pano=vPnURflnc8AZu5NMLYRddw
      > google_streetview --pano=vPnURflnc8AZu5NMLYRddw;A1v2IdX_6HKnIQa2SPyyAg
      
    Get 360 panorama using heading
      > google_streetview --location=46.414382,10.013988 --heading=0;90;180;270 --fov=90
    
    Download street view images to "downloads" folder
      > google_streetview --location=46.414382,10.013988 --save_downloads=downloads
    
    Save street view links and metadata
      > google_streetview --location=46.414382,10.013988 --save_links=links.txt
      > google_streetview --location=46.414382,10.013988 --save_metadata=metadata.json
  
  For more information visit use: google_streetview -i
"""

from google_streetview import helpers
from os.path import isfile
from pkg_resources import resource_filename, Requirement
from pprint import pprint
from sys import argv
from webbrowser import open_new_tab

import kwconfig
import google_streetview.api

_doc_link = 'https://github.com/rrwen/google_streetview'
_api_link = 'https://developers.google.com/maps/documentation/streetview/intro#url_parameters'
    
def run(argv=argv):
  """Runs the google_streetview command line tool.
  
  This function runs the google_streetview command line tool 
  in a terminal. It was intended for use inside a py file 
  (.py) to be executed using python.
  
  Notes:
    * Optional arguments with ``ref_`` are for the ``site`` and ``site_metadata`` parameters in :class:`api.results`
  
    For distribution, this function must be defined in the following files::
      
      # In 'google_streetview/google_streetview/__main__.py'
      from .cli import run
      run()
      
      # In 'google_streetview/google_streetview.py'
      from google_streetview.cli import run
      if __name__ == '__main__':
        run()
      
      # In 'google_streetview/__init__.py'
      __entry_points__ = {'console_scripts': ['google_streetview=google_streetview.cli:run']}
  
  Examples::
    
    # Import google_streetview for the cli module
    import google_streetview.cli
    
    # Create command line arguments
    argv = [
      'cli.py',
      'google',
      '--searchType=image',
      '--build_developerKey=your_dev_key',
      '--cx=your_cx_id'
      '--num=1'
    ]
    
    # Run command line
    google_streetview.cli.run(argv)
    
  """
  config_file = kwconfig.manage(
    file_path=resource_filename(Requirement.parse('google_streetview'), 'google_streetview/config.json'),
    defaults={
      'size': '640x640',
      'fov': '90',
      'pitch': '0',
      'option_silent': 'false',
      'option_preview': '10'}
  )
  
  # (commands) Main command calls
  if len(argv) > 1:
    if argv[1] == '-i': # browse docs
      open_new_tab(_doc_link)
      exit()
    elif argv[1] == '-a': # browse arguments
      open_new_tab(_api_link)
      exit()
  config_file.command(argv, i=1, doc=__doc__, quit=True, silent=False)
  
  # (parse_args) Parse command arguments into dict
  kwargs = kwconfig.parse(argv[1:])
  kwargs = config_file.add(kwargs)
  
  # (split_args) Split args into build, cse, and save arguments
  siteargs = {}
  apiargs = {}
  saveargs = {}
  optionargs = {}
  for k, v in kwargs.items():
    if 'site_' == k[0:4]:
      siteargs[k[4:]] = v
    elif 'save_' == k[0:5]:
      saveargs[k[5:]] = v
    elif 'option_' == k[0:7]:
      optionargs[k[7:]] = v
    else:
      apiargs[k] = v
      
  # (api_results) Get google api results
  site_api = siteargs['api'] if 'api' in siteargs else 'https://maps.googleapis.com/maps/api/streetview'
  site_metadata = siteargs['site_metadata'] if 'metadata' in siteargs else 'https://maps.googleapis.com/maps/api/streetview/metadata'
  results = google_streetview.api.results(
    helpers.api_list(apiargs),
    site_api=site_api,
    site_metadata=site_metadata)
  
  # (api_print) Print a preview of results
  if 'silent' in optionargs:
    if optionargs['silent'].lower() != 'true':
      results.preview(n=int(optionargs['preview']))
  
  # (api_save) Save metadata
  if 'links' in saveargs:
    results.save_links(saveargs['links'])
  if 'metadata' in saveargs:
    results.save_metadata(saveargs['metadata'])
  
  # (api_download) Download links
  if 'downloads' in saveargs:
    results.download_links(saveargs['downloads'])
    