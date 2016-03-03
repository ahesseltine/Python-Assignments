fname = raw_input("Enter file name: ")
if len(fname) < 1: name = "mbox-short.txt"
fh = open(fname, 'r')
count = dict()

for line in fh.readlines():
	line = ((line.rstrip()).lstrip()).split()	
	if line.startswith("From:") continue
		for wrd in fname
			count[wrd] = count.get(wrd,0) +1
   
print "count"

for kee,val in count.items() :
	if maxval == none : maxval = val
	if maxval < val : 
		maxval = val
	print kee, val, maxval

max = None 
highest = None
for key in dictionary:
	if max < dictionary[key]:
	max = dictionary[key]
	highest = key
return highest



