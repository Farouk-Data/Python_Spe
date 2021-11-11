i=0
s=0
while True :
    nb=input('Enter Number:')
    if nb == 'Done' :
        break
    try :
        n=float(nb)
        print(n)
        i=i+1
        s=s+n
    except :
        print('Error Entry')
        continue
print(s,i,s/i)
