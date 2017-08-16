google_streetview
=================

| Richard Wen
| rrwen.dev@gmail.com

* `Documentation <https://rrwen.github.io/google_streetview>`_
* `PyPi Package <https://pypi.python.org/pypi/google_streetview>`_

A command line tool and module for Google Street View Image API.

.. image:: https://badge.fury.io/py/google-streetview.svg
    :target: https://badge.fury.io/py/google-streetview
.. image:: https://img.shields.io/github/issues/rrwen/google_streetview.svg
    :target: https://github.com/rrwen/google_streetview/issues
.. image:: https://img.shields.io/github/forks/rrwen/google_streetview.svg
    :target: https://github.com/rrwen/google_streetview/network
.. image:: https://img.shields.io/github/stars/rrwen/google_streetview.svg
    :target: https://github.com/rrwen/google_streetview/stargazers
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/rrwen/google_streetview/master/LICENSE
.. image:: https://travis-ci.org/rrwen/google_streetview.svg?branch=master
    :target: https://travis-ci.org/rrwen/google_streetview
.. image:: https://img.shields.io/twitter/url/https/github.com/rrwen/google_streetview.svg?style=social
    :target: https://twitter.com/intent/tweet?text=%23python%20tool%20for%20%23GoogleStreetView%20Image%20API:%20https/github.com/rrwen/google_streetview

Install
-------

1. Install `Python <https://www.python.org/downloads/>`_
2. Install `google_streetview <https://pypi.python.org/pypi/google-streetview>`_ via ``pip``

::
  
  pip install google_streetview
  
For the latest developer version, see `Developer Install`_.
  
Usage
-----

For help in the console::
  
  google_streetview -h
  
Ensure that a `Google API developer key <https://developers.google.com/api-client-library/python/auth/api-keys>`_ is set::

  google_streetview -s key="your_dev_key"

Search street view for latitude and longitude ``46.414382,10.013988``::
  
  google_streetview "46.414382,10.013988"
  
Save images to a directory::

  google_streetview --location="46.414382,10.013988" --save_downloads=downloads
  
Obtain a 360 panorama by rotating the camera ``heading`` given a 90 degree field of vision ``fov``::

  google_streetview --location="46.414382,10.013988" --fov=90 --heading=0;90;180;270
  
Use as a Python module:

.. code-block:: python

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
  
  # Download images to directory 'downloads'
  results.download_links('downloads')
  
For more usage details, see the `Documentation <https://rrwen.github.io/google_streetview>`_.

Developer Notes
---------------

Developer Install
*****************

Install the latest developer version with ``pip`` from github::
  
  pip install git+https://github.com/rrwen/google_streetview
  
Install from ``git`` cloned source:

1. Ensure `git <https://git-scm.com/>`_ is installed
2. Clone into current path
3. Install via ``pip``

::

  git clone https://github.com/rrwen/google_streetview
  cd google_streetview
  pip install . -I
  
Tests
*****

1. Clone into current path ``git clone https://github.com/rrwen/google_streetview``
2. Enter into folder ``cd google_streetview``
3. Ensure `unittest <https://docs.python.org/2.7/library/unittest.html>`_ is available
4. Set your `Google API developer key <https://developers.google.com/api-client-library/python/auth/api-keys>`_
5. Run tests
6. Reset config file to defaults
7. Please note that this will use up 16 requests from your quota

::
  
  pip install . -I
  python -m google_streetview -s key=your_dev_key
  python -m unittest
  python -m google_streetview -d

Documentation Maintenance
*************************

1. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`_ is installed ``pip install -U sphinx``
2. Update the documentation in ``docs/``

::
  
  pip install . -I
  sphinx-build -b html docs/source docs

Upload to github
****************

1. Ensure `git <https://git-scm.com/>`_ is installed
2. Add all files and commit changes
3. Push to github

::
  
  git add .
  git commit -a -m "Generic update"
  git push
  
Upload to PyPi
**************

1. Ensure `twine <https://pypi.python.org/pypi/twine>`_ is installed ``pip install twine``
2. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`_ is installed ``pip install -U sphinx``
3. Run tests and check for OK status
4. Delete ``dist`` directory
5. Update the version ``google_streetview/__init__.py``
6. Update the documentation in ``docs/``
7. Create source distribution
8. Upload to `PyPi <https://pypi.python.org/pypi>`_

::
  
  pip install . -I
  python -m google_streetview -s key=your_dev_key
  python -m unittest
  python -m google_streetview -d
  sphinx-build -b html docs/source docs
  python setup.py sdist
  twine upload dist/*
  
