data = 'X-DSPAM-Confidence: 0.8475'
atpos = data.find (':')
print atpos

host = data[atpos]
print host