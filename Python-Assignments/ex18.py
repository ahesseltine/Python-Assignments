#defining what print_two means
def print_two(*argv):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" %(arg1, arg2)

#Or we could just do this, another way of doing what's above this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" %(arg1, arg2)

#Takes no arguments, it will only 'print'
def print_none():
	print "Will only print this"

print_two("Zebra","Elephant")
print_two_again("horse","pig")
print_none()
