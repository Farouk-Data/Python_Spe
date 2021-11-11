data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
place1=data.find('@')
print(place1)
place2=data.find(' ',place1)
print(place2)
host=data[place1+1:place2]
print(host)
