fname = raw_input("Enter file name: ")
try:
    if len(fname) < 1 : fname = "mbox-short.txt"
    fh = open(fname)
except:
    print"Incorrect filename or file does not exist, try again.",fname
    exit()

names = list()
counts = dict()

for lines in fh:
    lines = lines.rstrip()
    words = lines.split()
    if words == [] : continue
    if words[0] != 'From' : continue
    names.append(words[1])
    
for name in names:
    counts[name] = counts.get(name,0)+1


highcount = None
for email,times in counts.items():
    if times > highcount:
        highcount = times
        emailaddress = email
print emailaddress, highcount