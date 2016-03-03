fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print"Incorrect filename or file does not exist, try again.",fname
    exit()

lst = list()  

for line in fh:
    words = line.strip()
    words = line.split()
    for individual in words:
        if individual in lst: continue
        else:
            lst.append(individual)
lst.sort()
print lst
    
