def add(a,b) :
    s=float(a)+float(b)
    return s

try :
    n=float(input('Enter n: \n'))
except:
    print('Try Valid Number')
    quit()

try :
    m=float(input('Enter m: \n'))
except:
    print('Try Valid Number')
    quit()

s=add(n,m)
print('n+m=',s)


#def addtwo(a,b) :
#    add = float(a) + float(b)
#    return add

#n1 = input('Enter n1:')
#float(n1)
#n2 = input('Enter n2:')
#float(n2)
#r=float(addtwo(n1,n2))
#print('r=',r)
