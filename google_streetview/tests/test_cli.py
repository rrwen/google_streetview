# -*- coding: utf-8 -*-

from os import listdir, makedirs, remove
from os.path import isdir, isfile
from google_streetview.cli import run
from shutil import rmtree
from tempfile import TemporaryFile, TemporaryDirectory
from unittest import TestCase

import json

class cliTest(TestCase):

  def setUp(self):
    tempfile = TemporaryFile()
    self.tempfile = str(tempfile.name)
    tempfile.close()
    self.tempdir = str(TemporaryDirectory().name)
    
  def test_search_location(self):
    argv = [
      'cli.py',
      '--location=46.414382,10.013988'
    ]
    run(argv)
    
  def test_search_location_multi(self):
    argv = [
      'cli.py',
      '--location=46.414382,10.013988;40.720032,-73.988354'
    ]
    run(argv)
  
  def test_search_pano(self):
    argv = [
      'cli.py',
      '--pano=vPnURflnc8AZu5NMLYRddw'
    ]
    run(argv)
  
  def test_search_pano_multi(self):
    argv = [
      'cli.py',
      '--pano=vPnURflnc8AZu5NMLYRddw;A1v2IdX_6HKnIQa2SPyyAg'
    ]
    run(argv)
    
  def test_camera_multi(self):
    argv = [
      'cli.py',
      '--pano=vPnURflnc8AZu5NMLYRddw;A1v2IdX_6HKnIQa2SPyyAg',
      '--size=640x300',
      '--heading=0;90;180;270',
      '--fov=90',
      '--pitch=0'
    ]
    run(argv)
    
  def test_save_links(self):
    argv = [
      'cli.py',
      '--location=46.414382,10.013988',
      '--save_links=' + self.tempfile
    ]
    run(argv)
  
  def test_save_metadata(self):
    argv = [
      'cli.py',
      '--location=46.414382,10.013988',
      '--save_metadata=' + self.tempfile
    ]
    run(argv)
  
  def test_download_links(self):
    argv = [
      'cli.py',
      '--location=46.414382,10.013988',
      '--save_downloads=' + str(self.tempdir)
    ]
    run(argv)
    
  def tearDown(self):
    if isfile(self.tempfile):
      remove(self.tempfile)
    if isdir(self.tempdir):
      rmtree(self.tempdir)
    
