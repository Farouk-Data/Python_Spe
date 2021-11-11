fname=input('Enter FIle Name: \n')
try :
    fhand=open(fname)
except :
    print('Error File')
    quit()

for line in fhand :
    line=line.rstrip()
    line=line.upper()
    print(line)
