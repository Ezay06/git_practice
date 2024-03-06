import random
counter = 0

upper = int(input("Enter the max range: "))
lower = int(input("Enter the min range: "))
num = random.randint(lower, upper)
guess = str(input('Is '+str(num)+' the number you were thinking of?: '))

while guess != 'Exit' or 'exit':
    counter += 1

    if guess == 'too high':
        num = random.randint(lower, num-1)
        guess = str(input('Is '+str(num)+' the number you were thinking of?: '))

    elif guess == 'too low':
        num = random.randint(num+1, upper)
        guess = str(input('Is '+str(num)+' the number you were thinking of?: '))

    elif guess == 'correct':
        print('It took from the program ', counter, ' times to guess right.')
        y = str(input('Would you like to play again?: '))

        if y == 'yes':
            counter = 0
            upper = int(input('Enter the max range: '))
            lower = int(input('Enter the min range: '))
            num = random.randint(lower, upper)
            guess = str(input('Is '+str(num)+' the number you were thinking of?:  '))
        else:
            break

    else:
        print('Error! You typed wrong. Please try again.')
        counter = counter-1
        guess = str(input('Is '+str(num)+' the number you were thinking of?: '))
print('Thanks for playing')
