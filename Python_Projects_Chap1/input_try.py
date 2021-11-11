numb = input('Enter Your Number: ')
try :
    test = int(numb)
except:
    test = -1
if test >= 0 :
    print('Nice Number!')
else :
    print('Wrong Input!')
