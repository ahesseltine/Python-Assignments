fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence: ") : continue
        numstart = line.find(":")
        print numstart


#num = line
#print len(line)