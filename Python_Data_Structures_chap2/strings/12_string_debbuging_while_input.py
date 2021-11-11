while True :
    line=input('>> ')
    #if line[0] == '#' :
    if len(line) == 0 :
        continue
    elif line.startswith('#'):
        continue
    elif line == 'done' :
        break
    print(line)
print('Done!')
