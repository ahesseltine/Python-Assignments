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
tags = soup('a')
# Starts at 1
count = 1

#Loops through 7 times
while count <= 7:
    #empties the urlnames list for each loop
    del urlnames[:]
    for tag in tags:
        # Look at the href tags
        URL = tag.get('href', None)
        #Adds tags to the list
        urlnames.append(URL)
        #Finds the link in the 18th spot, list starts at 0 so the 18th spot is really number 17
        newurl = urlnames[17:18]
        #Converts newurl into a string
        newurl = str(newurl)
        #Cleans up http link
        numstart = newurl.find('h')
        numend = len(newurl) - 2
        url = newurl[numstart:numend]   
    # Retrieve all of the anchor tags
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    #Adds count to track how many loops
    count = count + 1

else:
    #Once loop count is at 7 prints the url
    print url
        
