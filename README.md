# Flask seed

This is my own python3 + flask starter-kit, it will be improved with time.
The goal is to keep it simple and have something to get started.

## Setup

I suggest using virtualenv, and more specifically 
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/index.html).

Once you have the command line installed, create your virtualenv:

`mkvirtualenv my-super-app --python=/usr/local/bin/python3` (your python binary might be elsewhere).

Then when you come back to the project later, you do:

`workon my-super-app`

Install the dependencies:

`pip install -r requirements.txt`

Start the server:

`python runserver.py`
