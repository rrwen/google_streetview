# -*- coding: utf-8 -*-

from itertools import product

import requests
import shutil

def api_list(apiargs):
  """Google Street View Image API results.
  
  Constructs a list of `Google Street View Image API queries <https://developers.google.com/maps/documentation/streetview/>`_
  from a dictionary.
  
  Args:
    apiargs (listof dict):
      Dict containing `street view URL parameters <https://developers.google.com/maps/documentation/streetview/intro>`_.
      Each parameter can have multiple values if separated by ``;``.
  
  Returns:
    A ``listof dict`` containing single query requests per dictionary for Google Street View Image API.
  
  Examples: 
    ::
    
      # Import google_streetview for the api and helper module
      import google_streetview.api
      import google_streetview.helpers
      
      # Create a dictionary with multiple parameters separated by ;
      apiargs = {
        'location': '46.414382,10.013988;40.720032,-73.988354',
        'size': '640x300;640x640',
        'heading': '0;90;180;270',
        'fov': '0;90;120',
        'pitch': '-90;0;90'
      }
      
      # Get a list of all possible queries from multiple parameters
      api_list = google_streetview.helpers.api_list(apiargs)
      
      # Create a results object for all possible queries
      results = google_streetview.api.results(api_list)
      
      # Preview results
      results.preview()
      
      # Download images to directory 'downloads'
      results.download_links('downloads')
      
      # Save metadata
      results.save_metadata('metadata.json')
  """
  
  # (api_query) Query combinations for each parameter
  api_queries = {}
  keywords = [k for k in apiargs]
  for k in keywords:
    if k in apiargs:
      api_queries[k] = apiargs[k].split(';')
      apiargs.pop(k, None)
  
  # (api_list) Build list of api requests based on query combinations
  out = []
  keys = [k for k in api_queries]
  queries = [api_queries[k] for k in api_queries]
  combinations = product(*queries)
  for combo in combinations:
    api_copy = apiargs.copy()
    for k, parameter in zip(keys, combo):
      api_copy[k] = parameter
    out.append(api_copy)
  return(out)

def download(url, file_path):
  r = requests.get(url, stream=True)
  if r.status_code == 200: # if request is successful
    with open(file_path, 'wb') as f:
      r.raw.decode_content = True
      shutil.copyfileobj(r.raw, f)
