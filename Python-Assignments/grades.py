try:
    score = raw_input ("Enter score:")
    s = float(score)
except:
    print "Error, please enter a number"
    
if s >= 0.9:
    print "A"
elif s >= 0.8:
    print "B"
elif s >= 0.7:
    print "C"
elif s >= 0.6:
    print "D"
elif s < 0.6:
    print "F"