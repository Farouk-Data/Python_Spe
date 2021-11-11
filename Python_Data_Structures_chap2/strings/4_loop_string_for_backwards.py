fruit='azertyuiop'
index = len(fruit)
for char in fruit :
    if index < 0 :
        break
    else :
        letter = fruit[index-1]
        print(index,char)
        index = index- 1
print('Done')
