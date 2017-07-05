# -*- coding: utf-8 -*-

from google_streetview import helpers
from unittest import TestCase

class cliTest(TestCase):

  def test_api_list(self):
    apiargs = {
      'location': '46.414382,10.013988',
      'size': '640x300',
      'heading': '0'
    }
    api_list = helpers.api_list(apiargs)
    self.assertTrue(1 == len(api_list))
  
  def test_api_list_multi(self):
    apiargs = {
      'location': '46.414382,10.013988;40.720032,-73.988354',
      'size': '640x300;640x640',
      'heading': '0;90;180;270',
      'fov': '0;90;120',
      'pitch': '-90;0;90'
    }
    api_list = helpers.api_list(apiargs)
    self.assertTrue(144 == len(api_list))
    