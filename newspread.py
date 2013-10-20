# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Import basic Python libraries for use in your program: [os.path](http://docs.python.org/2/library/os.path.html) and [ConfigParser](http://docs.python.org/2/library/configparser.html)

# <codecell>

import os.path
import ConfigParser

# <markdowncell>

# Define `take(n, iterable)` which is a convenience function to limit the amount of output that you print. Useful when you have lots of data that will clutter up your screen!

# <codecell>

from itertools import islice
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

# <markdowncell>

# Read the username and password from the `[google]` section of the `stat157.cfg` config file from your virtual machine home directory.

# <codecell>

home = os.path.expanduser("~")
configfile = os.path.join(home, 'stat157.cfg')
config = ConfigParser.SafeConfigParser()
config.read(configfile)
username = config.get('google', 'username')
password = config.get('google', 'password')
print username

# <markdowncell>

# An example of reading data from a Google Spreadsheet using the gspread library: http://stackoverflow.com/a/18296318/462302
# 
# First you'll need to install the gspread library on your virtual machine using: `sudo pip install gspread`

# <codecell>

import gspread
gspread_client = gspread.login(username, password)

# <markdowncell>

# Install the Google Data library with `sudo apt-get install python-gdata` and import the client library. This example was adapted from http://pastebin.com/zADrcEJU which Arif and I discovered by [searching](https://www.google.com/search?q=gspread+create+new+spreadsheet&oq=gspread+create+new+spreadsheet&aqs=chrome..69i57.4899j0j1&sourceid=chrome&ie=UTF-8) for how to create a new Google Spreadsheet with GSpread. This issue has some more background information: https://github.com/burnash/gspread/issues/36

# <codecell>

import gdata.docs.client
gdata_client = gdata.docs.client.DocsClient()
gdata_client.ClientLogin(username, password, 'Stat157 Client')
document = gdata.docs.data.Resource(type='spreadsheet', title=filename)
document = gdata_client.CreateResource(document)
document

# <codecell>

filename = "stat157-homework-02-quake-data"
try:
    gspread_client.open(filename)
except Exception, e:
    document = gdata.docs.data.Resource(type='spreadsheet', title=filename)
    document = gd_client.CreateResource(document)

# <codecell>

spreadsheet = gspread_client.open(filename)
spreadsheet

# <markdowncell>

# Use the documentation for the [GSpread API](https://github.com/burnash/gspread) to add data to the spreadsheet

# <codecell>

def foo():
    y = 3 + 1  # hard-coding is EVIL
    return y
foo()

# <codecell>

z = 3

def foo(x):
    y = x + 1
    return y 

foo(z)

# <markdowncell>

# Given the insigh of the levels of (hardcoded) hell above, what would you do next to lift the filename top-level variable into a configuration file?

# <codecell>


