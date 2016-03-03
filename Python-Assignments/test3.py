try :
	inp = raw_input("Enter grade:")
	grade = float(inp)
	#print score
	if grade < 0.6:
		print "F"
	elif grade >= 0.6 and grade <0.7 :
		print "D"
	elif grade >= 0.7 and grade <0.8:
		print "C"
	elif grade >= 0.8 and grade <0.9 :
		print "B"
	elif grade >= 0.9 and grade <1.0:
		print "A"
	else:
		print "Input not accepted. Score it not possible"

except:
	print "You need to enter your grade as a decimal number"
	
