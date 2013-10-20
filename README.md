Arif and I explored how to create a new Google Docs Spreadsheet. We
discovered that the GSpread library was not capable of doing that by
itself, so we searched around to find a way to do it:

Install the Google Data library with `sudo apt-get install
python-gdata` and import the client library. This example was adapted
from http://pastebin.com/zADrcEJU which Arif and I discovered by
[searching](https://www.google.com/search?q=gspread+create+new+spreadsheet&oq=gspread+create+new+spreadsheet&aqs=chrome..69i57.4899j0j1&sourceid=chrome&ie=UTF-8)
for how to create a new Google Spreadsheet with GSpread. This issue
has some more background information:
https://github.com/burnash/gspread/issues/36

The next step for Arif & Alex is to move the filename variable from
the top-level into a configuration file and to remove the filename
hard-coded in the IPython Notebook. And then use gspread to insert the
USGS data into the newly created Google Spreadsheet.
