found = False
print('Before:',found)
for i in [8,44,4,15,41,3,3,4,8] :
    if i == 3 :
        found = True
    print(found,i)
    break
print('After:',found)
