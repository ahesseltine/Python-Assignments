import json
import urllib


url = raw_input('Enter - ')
input = urllib.urlopen(url).read()
#http://python-data.dr-chuck.net/comments_205743.json
#Second video to help understand what I was missing!!!! https://www.youtube.com/watch?v=pxofwuWTs7c


stuff = json.loads(input)
lst = list()

for item in stuff['comments']:
    x = item['count']
    lst.append(x)

print 'This is how many numbers were found:', len(lst)
print 'Sum', sum(lst)






    
    
    










