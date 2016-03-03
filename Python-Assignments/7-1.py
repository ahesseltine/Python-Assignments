fname = raw_input("Enter file name:")
try:
    fh = open(fname)
except:
    print"Incorrect filename or file does not exist, try again.",fname
    exit()

#file = fh.read()    
for lines in fh:
    lines = lines.rstrip()
    print lines
    