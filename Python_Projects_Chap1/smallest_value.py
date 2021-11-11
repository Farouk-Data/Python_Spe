#use is for None,True,False
smallest = None
print('Before:',smallest)
for i in [45,2,53,6,-1,-1.5,7] :
    #getting started
    if smallest is None :
        smallest = i
    elif i < smallest :
        smallest = i

print('Smallest=',smallest)
