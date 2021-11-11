i=0
sum=0
while True :
    number = input('Enter a number: \n')
    if number == 'done' :
        break
    try :
        n = float(number)
        print(n)
        i=i+1
        sum = sum+n
    except :
        print('Error')
        continue

print('Total=',i,'Sum=',sum,'Average=',sum/i)
