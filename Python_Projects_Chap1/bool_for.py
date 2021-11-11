number = input('Enter the number u re looking for: \n')
n=float(number)
s=[1,3,6,4.5,3,0,7,4,9,10,-4]
search = False
#count=0
for i in range(0,len(s)) :
    if s[i] == n :
        search = True
        print('The search is :',search,'and its position is',i )
        break
print('Search is :',search)
