from sys import argv

script, filename = argv

print "This is a not a drill"
print "Are you sure that you can handle this!"
print "I don't know if you can...."

raw_input("?")

print "Your computer will shutdown now"
target=open(filename, 'w')

print "please fill out the reason for shutting down the computer now"
target.truncate()

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.write("HAHAHAHHAHAAA you fell for it")

print "done now"
target.close()
