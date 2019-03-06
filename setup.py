# -*- coding: utf-8 -*-

from setuptools import setup

import google_streetview as package

def readme():
  with open('README.md') as f:
    return ''.join(f.readlines())
        
setup(
  name=package.__name__,
  version=package.__version__,
  description=package.__description__,
  long_description=readme(),
  long_description_content_type=package.__long_description_content_type__,
  author=package.__author__,
  author_email=package.__email__,
  license=package.__license__,
  url=package.__url__,
  download_url=package.__download_url__,
  keywords =package. __keywords__,
  entry_points=package.__entry_points__,
  packages=package.__packages__,
  package_data=package.__package_data__,
  install_requires=package.__install_requires__
)
