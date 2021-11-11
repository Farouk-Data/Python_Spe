text = "X-DSPAM-Confidence:    0.8475"
print(text)
#ipos=text.find(':')
#print(ipos)
place1=text.find('0')
print('The number starts at: ',place1)
#piece=text[ipos+2:]
#print(piece+42.0)
num=text[place1:]
number=float(num)
#print(piece+42.0)
print('num=',number)
