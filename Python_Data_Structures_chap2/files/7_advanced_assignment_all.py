fname=input('Enter File Name: \n')
try :
    fhand=open(fname)
except :
    print('Error File!')
    quit()

count=0
total=0

for line in fhand :
    #if 'X-DSPAM-Confidence:    0.8475' in line :
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    line=line.strip()
    x=line.find('0')
    number=float(line[x:])
    count = count + 1
    total=total+number
average=total/count

print('Average spam confidence:',average)
