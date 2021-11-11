def chc(c) :
    if c == 'Y' :
        return 'Yes'
    elif c == 'N' :
        return 'No'
    else :
        return 'Sorry'
try:
    choice=input('Choose Y/N : \n')
    print(chc(choice))
except:
    print('invalid choice!')
