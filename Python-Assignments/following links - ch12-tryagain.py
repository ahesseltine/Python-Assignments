# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

#https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Jensen.html

soup = BeautifulSoup(html)
urlnames = list()
count = 0
tags = soup('a')


for tag in tags:
    # Look at the parts of a tag
    URL = tag.get('href', None)
    urlnames.append(URL)
    newurl = urlnames[17:18]
    newurl = str(newurl)
    numstart = newurl.find('h')
    numend = len(newurl) - 2
    url = newurl[numstart:numend]
        


print url