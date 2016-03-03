fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print"Incorrect filename or file does not exist, try again.",fname
    exit()
    
lst = list()
for line in fh:
    word= line.rstrip().split()
    for words in word:
        if words in lst:
            continue
        else :
            lst.append(words)
lst.sort()                         
print lst                          
