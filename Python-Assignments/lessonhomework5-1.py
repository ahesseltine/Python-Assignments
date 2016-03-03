smallest = None
largest = None

while True:
	num = raw_input('Enter a number')
	
	if num == "done" : 
		print "Maximum is", largest
		print "Minimum is", smallest
		break
		
	try:
		num = int(num)
		
		if smallest is None:
			smallest = num
		elif num < smallest:
			smallest = num
				
		if largest is None:
			largest = num
		elif num > largest:
			largest = num
				

	except:
		print 'Invalid input'
		
	

