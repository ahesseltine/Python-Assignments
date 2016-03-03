fname = raw_input("Enter file :")
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)

# Initializing a list
emails = list()


# Reading the file
for line in fhandle:
    # Discard the line if it doesn't begin by "From" etc.
    if not line.startswith("From ") : continue
    words = line.split()
	# Look for the sender email
    email = words[1]
    # Add the email to the list
    emails.append(email)

# Initializing the dictionary
senders = dict()
   
# Counting the mails sent by each email
for mail in emails:
	senders[mail] = senders.get(mail, 0) + 1

# Find the most active sender

maxmailsnum = 0
mailmailaddress = ""

# Convert our dictionary to a list of tuples
listSenders = senders.items()

for sender in listSenders:
	if sender[1] > maxmailsnum:
		maxmailsnum = sender[1]
		maxmailaddress = sender[0]
		
print maxmailaddress, maxmailsnum