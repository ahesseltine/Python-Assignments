# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
	line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print line
    count = count + 1
    print 'Line Count:', count
print "Done"



#x = 'X-DSPAM-Confidence: 0.8475'
#pos = x.find(':')
#print x[pos+1:]
#num = float(x[pos+1])
#print num, type(num)


#Output for project:

#x = 'X-DSPAM-Confidence: 0.8475'
#pos = x.find(':')
#print float(x[pos+2:])
