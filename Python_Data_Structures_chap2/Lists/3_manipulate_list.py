t=['a','z','e','r','t','y','u','i','o','p']

x=t.pop(0)
print(t)
print(x)

del t[0]
print(t)

t.remove('p')
print(t)

del t[1:5]
print(t)
