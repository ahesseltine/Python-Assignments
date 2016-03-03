fname = raw_input("Enter file name: ")
try:
    if len(fname) < 1 : fname = "mbox-short.txt"
    fh = open(fname)
except:
    print"Incorrect filename or file does not exist, try again.",fname
    exit()

hours = list()
counts = dict()
tmp = list()
    
for lines in fh:
    lines = lines.rstrip()
    words = lines.split()
    if words == [] : continue
    if words[0] != 'From' : continue
    time = words[5]
    hour = time.split(":")
    hour = hour[0]
    hours.append(hour)

for hourtime in hours:
    counts[hourtime] = counts.get(hourtime,0)+1
    
for a,b in counts.items():
    tmp.append((a,b))
    tmp.sort()
for a,b in tmp:
    print a, b


