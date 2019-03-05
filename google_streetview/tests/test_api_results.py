# -*- coding: utf-8 -*-

from os import listdir, remove
from os.path import isdir, isfile
from pkg_resources import resource_filename, Requirement
from unittest import TestCase
from shutil import rmtree
from tempfile import TemporaryFile, TemporaryDirectory

import google_streetview.api
import json

class apiTest(TestCase):

  def setUp(self):
    file_path = resource_filename(Requirement.parse('google_streetview'), 'google_streetview/config.json')
    with open(file_path, 'r') as in_file:
      defaults = json.load(in_file)
    params = [{
      'size': '600x300', # max 640x640 pixels
      'location': '46.414382,10.013988',
      'heading': '151.78',
      'pitch': '-0.76',
      'key': defaults['key']
    }]
    self.results = google_streetview.api.results(params)
    tempfile = TemporaryFile()
    self.tempfile = str(tempfile.name)
    tempfile.close()
    self.tempdir = str(TemporaryDirectory().name)
  
  def test_preview(self):
    results = self.results
    expected = None
    self.assertTrue(expected == results.preview())
  
  def test_download_links(self):
    self.results.download_links(self.tempdir)
    nfiles = len(listdir(self.tempdir))
    rmtree(self.tempdir)
    self.assertTrue(nfiles > 0)
  
  def test_metadata_status_ok(self):
    status = self.results.metadata[0]['status']
    expected = 'OK'
    self.assertTrue(status == expected)
  
  def test_save_links(self):
    results = self.results
    results.save_links(self.tempfile)
    with open(self.tempfile, 'r') as f:
      nlinks = len(f.readlines())
    self.assertTrue(nlinks == 1)
  
  def test_save_metadata(self):
    results = self.results
    results.save_metadata(self.tempfile)
    with open(self.tempfile, 'r') as f:    
      metadata = json.load(f)
    self.assertTrue(metadata == results.metadata)
  
  def tearDown(self):
    if isfile(self.tempfile):
      remove(self.tempfile)
    if isdir(self.tempdir):
      rmtree(self.tempdir)
    
