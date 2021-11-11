list1=[1,2,3,4,5]
list2=['farouk','Dante','Edgar Allan Poe','Tarkovsky']
list3=[1,'Jim Jarmush','Letterboxd',9.5,[1.2]]
#for i in list2 :
#    print(i)
#print(list1[0])
#print(list2[1])
print(list3)
print('Cinema App Before:',list3[2])
list3[2]='IMDB'
print('Cinema App After:',list3[2])

#print('Len(list1)=',len(list1))
#print('Len(list2)=',len(list2))
print('Len(list3)=',len(list3))
print(range(len(list3)))

for i in range(len(list1)) :
    list1[i]=list1[i]*2
    print(list1)

for list in list3 :
    print('This is:',list)

for i in range(len(list3)):
    list=list3[i]
    print('This is :',list)
