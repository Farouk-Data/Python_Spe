cls = input('Enter your degre in Celsius:\n')
try :
    fhr = float(cls)*(9/5)+32
except :
    fhr=-1
    print('Please Enter A Number ')
print('Your Degre in Fahrenheit:',fhr)
