import re
import urllib
from  BeautifulSoup import *

#fname = raw_input("Enter file name: ")
#fh = open(fname)
url = raw_input('Enter - ')
html = urllib.urlopen(url)

#regex_sum_205737.txt

lst = list()
count = 0

#x = '43 hi there 90 sucks cause 10 don;t understand 80'
#y = re.findall('[0-9]+', fh)
#print y


#Strip out the space in file, this prints out all lines. Only showing numbers and blank lines
for lines in html:
    lines = lines.rstrip()
    print lines
    if not lines.startswith('<tr>'): continue
    y = re.findall('[0-9]+',lines)
    for x in y:
        x = re.findall('[0-9]+', x)
        if len(x) == 0 :continue
        num = int(x[0])
        lst.append(num)
        count = count + 1
    
print "Count", count    
print "Sum", sum(lst)


  