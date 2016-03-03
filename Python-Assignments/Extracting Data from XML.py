import xml.etree.ElementTree as ET
import urllib


url = raw_input('Enter - ')
input = urllib.urlopen(url).read()
#http://python-data.dr-chuck.net/comments_205739.xml
print input


stuff = ET.fromstring(input)
lst = stuff.findall('comments/comment')
print type(lst)
count = list()


for item in lst:
    counts = item.find('count').text
    counts = int(counts)
    count.append(counts)


print 'Count Total', len(count)
print 'Sum', sum(count)

