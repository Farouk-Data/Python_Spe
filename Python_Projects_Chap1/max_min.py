min = None
max = None
#i=0
#sum = 0
while True :
    number = input('Enter N: \n')
    if number == 'done':
        break
    try :
        n=float(number)
        print(n)
        #i=i+1
        #sum=sum+n
    except :
        print('Error')
        continue
    if min is None :
        min = n
    elif n < min :
        min = n
    if max is None :
        max = n
    elif n > max :
        max = n

print('Max= ',max,'\nMin= ',min)
