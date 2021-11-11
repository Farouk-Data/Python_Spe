string=input('Enter a string: \n')
a_count = 0
b_count = 0
c_count = 0
d_count = 0
for char in string :
    if char == 'a' :
        a_count= a_count + 1
    elif char == 'b' :
        b_count= b_count + 1
    elif char == 'c' :
        c_count= c_count + 1
    elif char == 'd' :
        d_count= d_count + 1
print('The number of the letter a is: ',a_count)
print('The number of the letter b is: ',b_count)
print('The number of the letter c is: ',c_count)
print('The number of the letter d is: ',d_count)
