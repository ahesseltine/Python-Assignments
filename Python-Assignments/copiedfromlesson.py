smallest = None
print 'Before'
for value in [9,41,13,74,16,2]:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest  = value
	print smallest, value

print 'After', smallest