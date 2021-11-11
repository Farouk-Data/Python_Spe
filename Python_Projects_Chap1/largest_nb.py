#largest_nb = -1
#print('Before',largest_nb)
#for nb in [9,41,12,3,74,99,33,15] :
#    if nb > largest_nb :
#        largest_nb = nb
#    print(largest_nb,nb)
#print('After',largest_nb)

largest = None
print('Before Largest=',largest)
for i in [9, 41, 12, 3, 74, 99, 33, 15] :
    if largest is None :
        largest = i
    elif i > largest :
        largest = i
print('After Largest=',largest)
