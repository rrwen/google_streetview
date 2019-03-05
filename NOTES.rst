Developer Notes
---------------

Developer Install
*****************

Install the latest developer version with ``pip`` from github::
  
  pip install git+https://github.com/rrwen/google_streetview
  
Install from ``git`` cloned source:

1. Ensure `git <https://git-scm.com/>`__ is installed
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
4. Set your `Google API developer key <https://developers.google.com/api-client-library/python/auth/api-keys>`__
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

1. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`__ is installed ``pip install -U sphinx``
2. Update the documentation in ``docs/``

::
  
  pip install . -I
  sphinx-build -b html docs/source docs

Upload to github
****************

1. Ensure `git <https://git-scm.com/>`__ is installed
2. Add all files and commit changes
3. Push to github

::
  
  git add .
  git commit -a -m "Generic update"
  git push
  
Upload to PyPi
**************

1. Ensure `twine <https://pypi.python.org/pypi/twine>`_ is installed ``pip install twine``
2. Ensure `sphinx <https://github.com/sphinx-doc/sphinx/>`__ is installed ``pip install -U sphinx``
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