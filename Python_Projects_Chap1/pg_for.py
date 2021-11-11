large = 0
for i in [2, -1, 7, 12, 5, 5.01, 12.01] :
    if large == 0 :
        large = i
    elif i > large :
        large = i
print('Large=',large)
