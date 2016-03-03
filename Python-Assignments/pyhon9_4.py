fname = raw_input("Enter file :")
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)

# Creating a list
responder = list()

for line in fhandle:
    # Discard the line if it doesn't begin by "From" etc.
    if not line.startswith("From ") : continue
    words = line.split()
	# Look for the sender email
    email = words[1]
    # Add the email to the list
    responder.append(email)

# Creating a dictionary
people = dict()
   
for messages in responder:
	people[messages] = people.get(messages, 0) + 1

maxmailsnum = 0
mailmailaddress = ""

listSenders = people.items()

for person in listSenders:
	if person[1] > maxmailsnum:
		maxmailsnum = person[1]
		maxmailaddress = person[0]
		
print maxmailaddress, maxmailsnum