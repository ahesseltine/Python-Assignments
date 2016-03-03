import re

fname = raw_input("Enter file name: ")
fh = open(fname)

#regex_sum_205737.txt

lst = list()

#x = '43 hi there 90 sucks cause 10 don;t understand 80'
#y = re.findall('[0-9]+', fh)
#print y


#Strip out the space in file, this prints out all lines. Only showing numbers and blank lines
for lines in fh:
    y = re.findall('[0-9]+',lines)
    for x in y:
        x = re.findall('[0-9]+', x)
        if len(x) == 0 :continue
        num = int(x[0])
        lst.append(num)
    
    
print sum(lst)