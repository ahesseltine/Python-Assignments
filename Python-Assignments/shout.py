filename = raw_input('Enter a file name : ')
filehand = open(filename)
for line in filehand :
	line = line.rstrip().upper()
	print line