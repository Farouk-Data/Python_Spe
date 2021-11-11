fruit = input('Enter a Fruit : \n')

#Index is initialized by the length of the word
index = len(fruit)

#We Start at the condition where the loop won't stop until the break bcs we are starting from the end of the word, if not , the loop will stop at the first circle
while True :

    #We Start from the last character [index-1]
    letter = fruit[index-1]
    
    print(index,letter,'\n')

    #going backwards
    index = index - 1

    #Condition to stop the loop from being infinite
    if index < 1 :
        break

print('Done')
