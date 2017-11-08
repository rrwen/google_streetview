google_streetview
=================

| Richard Wen
| rrwen.dev@gmail.com

* `Documentation <https://rrwen.github.io/google_streetview>`_
* `PyPi Package <https://pypi.python.org/pypi/google_streetview>`_

A command line tool and module for Google Street View Image API.

.. image:: https://badge.fury.io/py/google-streetview.svg
    :target: https://badge.fury.io/py/google-streetview
.. image:: https://travis-ci.org/rrwen/google_streetview.svg?branch=master
    :target: https://travis-ci.org/rrwen/google_streetview
.. image:: https://coveralls.io/repos/github/rrwen/google_streetview/badge.svg?branch=master
    :target: https://coveralls.io/github/rrwen/google_streetview?branch=master
.. image:: https://img.shields.io/github/issues/rrwen/google_streetview.svg
    :target: https://github.com/rrwen/google_streetview/issues
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/rrwen/google_streetview/master/LICENSE
.. image:: https://img.shields.io/github/stars/rrwen/google_streetview.svg
    :target: https://github.com/rrwen/google_streetview/stargazers
.. image:: https://img.shields.io/twitter/url/https/github.com/rrwen/google_streetview.svg?style=social
    :target: https://twitter.com/intent/tweet?text=%23python%20%23dataextraction%20tool%20for%20%23googlestreetview%20images:%20https://github.com/rrwen/google_streetview

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

Contributions
-------------

Report Contributions
********************

Reports for issues and suggestions can be made using the `issue submission <https://github.com/rrwen/google_streetview/issues>`_ interface.  
  
When possible, ensure that your submission is:

* **Descriptive**: has informative title, explanations, and screenshots
* **Specific**: has details of environment (such as operating system and hardware) and software used
* **Reproducible**: has steps, code, and examples to reproduce the issue

Code Contributions
******************

Code contributions are submitted via `pull requests <https://help.github.com/articles/about-pull-requests>`_:

1. Ensure that you pass the `Tests`_
2. Create a new `pull request <https://github.com/rrwen/search_google/pulls>`_
3. Provide an explanation of the changes

A template of the code contribution explanation is provided below:

::

  ## Purpose

  The purpose can mention goals that include fixes to bugs, addition of features, and other improvements, etc.

  ## Description

  The description is a short summary of the changes made such as improved speeds, implementation

  ## Changes

  The changes are a list of general edits made to the files and their respective components.
  
  * `file_path1`:
    * `function_module_etc`: changed loop to map
    * `function_module_etc`: changed variable value
  * `file_path2`:
    * `function_module_etc`: changed loop to map
    * `function_module_etc`: changed variable value

  ## Notes

  The notes provide any additional text that do not fit into the above sections.
  

For more information, see `Developer Install`_ and `Implementation`_.

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
  
Implementation
**************

The command line tool and module use query strings inside Uniform Resource Locators (URLs) that make requests to `Google Street View Image API <https://developers.google.com/maps/documentation/streetview>`_. The Python package `requests <https://pypi.python.org/pypi/requests>`_ were used to download the images from the URL requests from a dictionary passed to the ``google_streetview.api`` module.

::
  
  Google Street View Image API
               |
  URL Request with query string
               |
      google_streetview.api
               |
            request
  
