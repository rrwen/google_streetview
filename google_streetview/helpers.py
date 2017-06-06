# -*- coding: utf-8 -*-

import requests
import shutil

def api_list(apiargs):

  # (api_query) Extract location or pano queries
  if 'pano' in apiargs:
    api_queries = apiargs['pano'].split(';')
    apiargs.pop('location', None)
  elif 'location' in apiargs:
    api_queries = apiargs['location'].split(';')
    apiargs.pop('pano', None)
  else:
    print('Error: Parameters --pano or --location required.')
    exit()
  
  # (api_list) Build list of api requests based on multiple queries
  out = []
  for query in api_queries:
    api_copy = apiargs.copy()
    if 'pano' in apiargs:
      api_copy['pano'] = query
    elif 'location' in apiargs:
      api_copy['location'] = query
    out.append(api_copy)
  return(out)

def download(url, file_path):
  r = requests.get(url, stream=True)
  if r.status_code == 200: # if request is successful
    with open(file_path, 'wb') as f:
      r.raw.decode_content = True
      shutil.copyfileobj(r.raw, f)
