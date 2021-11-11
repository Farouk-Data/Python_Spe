i=0
s=0.0
m=0.0
nb=input('Enter Number : ')
while nb != 'Done' :
    nb=input('Enter Number : ')
    try :
        n=int(nb)
        i=i+1
        s=s+n
    except :
        print('Error Entry!')
        continue
m=s/i
print(s,i,m)
