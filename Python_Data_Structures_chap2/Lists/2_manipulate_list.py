#Concatenation
a=[1,2,3]
b=[4,5,6]
c=a+b
print(a,'+',b,'=',c)
#c=[1,2,3,4,5,6]
#Slicing
t=['a','b','c','d','e','f']
print(t[0:3])
#print(t[:])
#print(t[3:])
#print(t[:3])
#Building A List:
stuff=list()
stuff.append('Book')
stuff.append('99')
stuff.append('cookie')
print(stuff)

t1=['a','b','c']
t2=['d','e']
t1.extend(t2)
print(t1)
#t1=['a','b','c','e','d']

t=['e','f','a','c','b','d']
t.sort()
print(t)
