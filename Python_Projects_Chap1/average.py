def div(a,b) :
    c=float(a)/int(b)
    return c
count=0
sum=0
for i in [2,5,-1,9,5,20,-10] :
    count = count + 1
    sum = sum + i
d=div(sum,count)
print('count=',count)
print('sum=',sum)
print('average=',d)
