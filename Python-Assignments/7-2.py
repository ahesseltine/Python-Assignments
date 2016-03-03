fname = raw_input("Enter file name:")
try:
    fh = open(fname,'r')
except:
    print"Incorrect filename or file does not exist, try again.",fname
    exit()
numbers = list()
  
for lines in fh:
    if lines.startswith('X-DSPAM-Confidence:'):
        numstart = lines.find(' ')
        num = lines[numstart:]
        num = num.strip()
        num = float(num)
        numbers.append(num)
average = sum(numbers) / len(numbers)
print 'Average spam confidence: ',average