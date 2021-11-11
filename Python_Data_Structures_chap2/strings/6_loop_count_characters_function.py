def upper_case(char) :

    char >= 'A' and char <= 'Z'

def lower_case(char) :

    char >= 'a' and char <= 'a'

def count(s,l) :
    string=str(s)
    letter=str(l)
    let_lower=lower_case(letter)
    LET_UPPER=upper_case(letter)
    l_count=0
    u_count=0
    count = 0
    for char in string :
        if (char == let_lower) :
            l_count = l_count + 1
        elif (char == LET_UPPER) :
            u_count = u_count + 1
    count = l_count + u_count
    return count

string = input('Enter A String: \n')
letter=input('Enter the letter you wanna count: \n')
c=count(string,letter)
#count('teeest','e')
print('The number of ',letter,' is :',c)
