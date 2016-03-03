fname = raw_input("Enter file name: ")
try:
    if len(fname) < 1 : fname = "mbox-short.txt"
    fh = open(fname)
except:
    print"Incorrect filename or file does not exist, try again.",fname
    exit()

lst = list()
count = 0

for lines in fh:
    lines = lines.rstrip()
    if lines.startswith("From:"):
        address = lines.split(" ")
        count = count + 1
        print address[1]


print "There were", count, "lines in the file with From as the first word"