fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	word = line.rstrip()
	word = line.split()
	if words != ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder'] : continue
print words