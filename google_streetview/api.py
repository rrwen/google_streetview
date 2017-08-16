# -*- coding: utf-8 -*-

from google_streetview import helpers
from os import path, makedirs
from pprint import pprint
try:
  from urllib.parse import urlencode
except ImportError:
  from urllib import urlencode

import json
import requests

class results:
  """Google Street View Image API results.
  
  Uses the `Google Street View Image API <https://developers.google.com/maps/documentation/streetview/>`_ 
  to search for street level imagery.
  
  Args:
    params (listof dict):
      List of dict containing batch `street view URL parameters <https://developers.google.com/maps/documentation/streetview/intro>`_.
    site_api(str):
      The site for the URL request (example: https://maps.googleapis.com/maps/api/streetview).
    site_metadata(str):
      The site for the URL `metadata <https://developers.google.com/maps/documentation/streetview/metadata>`_ request (example: https://maps.googleapis.com/maps/api/streetview/metadata).
  
  Attributes:
    params (listof dict):
      Same as argument ``params`` for reference of inputs.
    links (listof str):
      List of str containing street view URL requests.
    metadata (listof dict):
      Objects returned from `street view metadata request <https://developers.google.com/maps/documentation/streetview/metadata>`_.
    metadata_links (listof str):
      List of str containing street view URL metadata requests.
  
  Examples: 
    ::
    
      # Import google_streetview for the api module
      import google_streetview.api
      
      # Define parameters for street view api
      params = [{
        'size': '600x300', # max 640x640 pixels
        'location': '46.414382,10.013988',
        'heading': '151.78',
        'pitch': '-0.76',
        'key': 'your_dev_key'
      }]
      
      # Create a results object
      results = google_streetview.api.results(params)
      
      # Preview results
      results.preview()
      
      # Download images to directory 'downloads'
      results.download_links('downloads')
      
      # Save links
      results.save_links('links.txt')
      
      # Save metadata
      results.save_metadata('metadata.json')
  """
  def __init__(
    self,
    params,
    site_api='https://maps.googleapis.com/maps/api/streetview',
    site_metadata='https://maps.googleapis.com/maps/api/streetview/metadata'):
    
    # (params) Set default params
    defaults = {
      'size': '640x640'
    }
    for i in range(len(params)):
      for k in defaults:
        if k not in params[i]:
          params[i][k] = defaults[k]
    self.params = params
    
    # (image) Create image api links from parameters
    self.links = [site_api + '?' + urlencode(p) for p in params]
    
    # (metadata) Create metadata api links and data from parameters
    self.metadata_links = [site_metadata + '?' + urlencode(p) for p in params]
    self.metadata = [requests.get(url, stream=True).json() for url in self.metadata_links]
      
  def download_links(self, dir_path, metadata_file='metadata.json', metadata_status='status', status_ok='OK'):
    """Download Google Street View images from parameter queries if they are available.
    
    Args:
      dir_path (str):
        Path of directory to save downloads of images from :class:`api.results`.links
      metadata_file (str):
         Name of the file with extension to save the :class:`api.results`.metadata
      metadata_status (str):
        Key name of the status value from :class:`api.results`.metadata response from the metadata API request.
      status_ok (str):
        Value from the metadata API response status indicating that an image is available.
    """
    metadata = self.metadata
    if not path.isdir(dir_path):
      makedirs(dir_path)
    
    # (download) Download images if status from metadata is ok
    for i, url in enumerate(self.links):
      if metadata[i][metadata_status] == status_ok:
        file_path = path.join(dir_path, 'gsv_' + str(i) + '.jpg')
        metadata[i]['_file'] = path.basename(file_path) # add file reference
        helpers.download(url, file_path)
    
    # (metadata) Save metadata with file reference
    metadata_path = path.join(dir_path, metadata_file)
    with open(metadata_path, 'w') as out_file:
      json.dump(metadata, out_file)
  
  def preview(self, n=10, k=['date', 'location', 'pano_id', 'status'], kheader='pano_id'):
    """Print a preview of the request results.
    
    Args:
      n (int):
        Maximum number of requests to preview
      k (str):
        Keys in :class:`api.results`.metadata to preview
      kheader (str):
        Key in :class:`api.results`.metadata[``k``] to use as the header
    """
    items = self.metadata
  
    # (cse_print) Print results
    for i, kv in enumerate(items[:n]):
      
      # (print_header) Print result header
      header = '\n[' + str(i) + '] ' + kv[kheader]
      print(header)
      print('=' * len(header))
        
      # (print_metadata) Print result metadata
      for ki in k:
        if ki in kv:
          if ki == 'location':
            print(ki + ': \n  lat: ' + str(kv[ki]['lat']) + '\n  lng: ' + str(kv[ki]['lng']))
          else:
            print(ki + ': ' + str(kv[ki]))
      
  def save_links(self, file_path):
    """Saves a text file of the search result links.
    
    Saves a text file of the search result links, where each link 
    is saved in a new line. An example is provided below::
      
      https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&heading=151.78&pitch=-0.76&key=yourdevkey
      https://maps.googleapis.com/maps/api/streetview?size=600x300&location=41.403609,2.174448&heading=100&pitch=28&scale=2&key=yourdevkey
    
    Args:
      file_path (str):
        Path to the text file to save links to.
    """
    data = '\n'.join(self.links)
    with open(file_path, 'w+') as out_file:
      out_file.write(data)
  
  def save_metadata(self, file_path):
    """Save Google Street View metadata from parameter queries.
    
    Args:
      file_path (str):
        Path of the file with extension to save the :class:`api.results`.metadata
    """
    with open(file_path, 'w+') as out_file:
      json.dump(self.metadata, out_file)
      
