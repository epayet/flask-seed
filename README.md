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

## License

MIT License

Copyright (c) [2017] [Emmanuel Payet]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.