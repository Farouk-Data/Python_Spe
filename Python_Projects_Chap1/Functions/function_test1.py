#def hello() :
#    print('Hello Function')
#    print('Bye')
#hello()
#print('Hi Again')
#hello()

def booleen(choice) :
    if choice == 'YES' :
        print('AGREE')
    elif choice == 'NO' :
        print('DISAGREE')
    else :
        print('Please Choose Again')

name = input('Choose YES/NO :')
booleen(name)
