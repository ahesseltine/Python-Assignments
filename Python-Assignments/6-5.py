text = "X-DSPAM-Confidence:    0.8475";
numstart = text.find('0')
numend = text.find('5',numstart)

num = text[numstart:numend+1]
num = float(num)
print num


