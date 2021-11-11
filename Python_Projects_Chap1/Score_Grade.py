try :
    g = float(input ('Enter Grade:'))
    if g > 1 or g < 0 :
        print('Your Number is out of rage')
    elif g >= 0.9 :
        print('A')
    elif g >= 0.8 :
        print('B')
    elif g >= 0.7 :
        print('C')
    elif g >= 0.6 :
        print('D')
    elif g < 0.6 and g >= 0.0 :
        print('F')
except:
    print('Error, try valide number')
