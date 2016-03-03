def computepay(h,r):
	if h <= 40 :
		p = r * h
	else :
		p = r * 40 + (r * 1.5 * (h - 40))
	return p

try :
	inp = raw_input("Enter Hours:")
	hours = float(inp)
	inp = raw_input("Enter Rate:")
	rate = float(inp)
	#print rate, hours
	if hours <= 40 :
		pay = rate * hours
	else :
		pay = rate * 40 + (rate * 1.5 * (hours - 40))
	print pay

except:
	print "Error, enter a number"
	quit()
	
pay= computepay(hours, rate)
	
