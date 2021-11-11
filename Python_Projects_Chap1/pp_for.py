smallest = None
print('Before we have smallest= ',smallest)
for itervar in [1,-2,5,0,-2.01] :
    print(itervar,smallest)
    if smallest is None or itervar < smallest :
        smallest = itervar
print('Smallest=',smallest)
