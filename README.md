# google_streetview

Richard Wen  
rrwen.dev@gmail.com  

* [Documentation](https://rrwen.github.io/google_streetview)
  
A command line tool and module for Google Street View Image API.


[![pypi version](https://badge.fury.io/py/google-streetview.svg)](https://badge.fury.io/py/google-streetview)
[![Build Status](https://travis-ci.org/rrwen/google_streetview.svg?branch=master)](https://travis-ci.org/rrwen/google_streetview)
[![Coverage Status](https://coveralls.io/repos/github/rrwen/google_streetview/badge.svg?branch=master)](https://coveralls.io/github/rrwen/google_streetview?branch=master)
[![Stars](https://img.shields.io/github/stars/rrwen/google_streetview.svg)](https://github.com/google_streetview/stargazers)
[![GitHub license](https://img.shields.io/github/license/rrwen/google_streetview.svg)](https://github.com/rrwen/google_streetview/blob/master/LICENSE)
[![Donarbox Donate](https://img.shields.io/badge/donate-Donarbox-yellow.svg)](https://donorbox.org/rrwen)
[![PayPal Donate](https://img.shields.io/badge/donate-PayPal-yellow.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=NQNSAHK5X46D2)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/rrwen/google_streetview.svg?style=social)](https://twitter.com/intent/tweet?text=A%20command%20line%20tool%20and%20module%20for%20Google%20Street%20View%20Image%20API:%20https://github.com/rrwen/google_streetview%20%23python%20%23pip)

**Note**: Google changed [StreetView API pricing](https://developers.google.com/maps/documentation/streetview/usage-and-billing) and a billing plan may be required (checked March 5, 2019).

## Install

1. Install [Python](https://www.python.org/downloads/)
2. Install [google_streetview](https://pypi.python.org/pypi/google-streetview) via `pip`

```
pip install google_streetview
```
  
For the latest developer version, see [Developer Install](https://github.com/rrwen/google_streetview/blob/master/NOTES.rst#developer-install).
  
## Usage

For help in the console:

```
google_streetview -h
```
  
Ensure that a [Google API developer key](https://developers.google.com/api-client-library/python/auth/api-keys) is set:

```
google_streetview -s key="your_dev_key"
```

Search street view for latitude and longitude `46.414382,10.013988`:
  
```
google_streetview "46.414382,10.013988"
```
  
Save images to a directory:

```
google_streetview --location="46.414382,10.013988" --save_downloads=downloads
```
  
Obtain a 360 panorama by rotating the camera ``heading`` given a 90 degree field of vision `fov`::

```
google_streetview --location="46.414382,10.013988" --fov=90 --heading=0;90;180;270
```
  
Use as a Python module:

```python

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
```
  
For more usage details, see the [Documentation](https://rrwen.github.io/google_streetview).

## Contributions

1. Reports for issues and suggestions can be made using the [issue submission](https://github.com/rrwen/google_streetview/issues)
2. Code contributions are submitted via [pull requests](https://github.com/rrwen/google_streetview/pulls)

See [CONTRIBUTING.rst](https://github.com/rrwen/google_streetview/blob/master/CONTRIBUTING.rst) for more details.
  
## Implementation

The package [google_streetview](https://pypi.python.org/pypi/google-streetview) uses the following components:

| Component                                                                                                | Purpose                                                                 |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [Google Street View Image API](https://developers.google.com/maps/documentation/streetview)              | API for Google Street View images                                       |
| [google_streetview.api](https://github.com/rrwen/google_streetview/blob/master/google_streetview/api.py) | Module for interfacing with Google Street View Image API using requests |
| [requests](https://pypi.python.org/pypi/requests)                                                        | Download and get URLs from Google Street View Image API                 |

```
  
  Google Street View Image API     <-- API for Street View Images
               |
      google_streetview.api        <-- URL Request with query string
               |
            request                <-- Download URLs and images
```
For more information, see [NOTES.rst](https://github.com/rrwen/google_streetview/blob/master/NOTES.rst).
