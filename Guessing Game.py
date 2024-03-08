<<<<<<< HEAD
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
=======
import random
print('''
      Welcome to Ziad's guessing game. The rules are simple:
          1) The Program is going to choose a random number.
          2) You are going to chose the range from which the number will be chosen.
          3) You are going to guess the number
          4) The program will tell you if you guessed too high or too low
          6) Have Fun!
      ''')


def guessing_game():
     isplaying = True
     counter = 0
     #Any input taken from the user is reviewed to ensure it is valid
     while True:
         try:
             a = int(input('Choose the upper range: '))
             b = int(input('Choose the lower range: '))
             if a <= b:
                 print('The upper range is less than or equal to the lower range. Please try again.\n')
             else:
                break
         except:
             print('Invalid input. Try again.\n')

    #A random number is chosen
     num = random.randint(b, a)

     while True:
         try:
            guess = int(input('Write your guess: '))
         except:
            print('Invalid input. Try again.')
            continue

        # After the user succesfully entered a guess, it is documented
         counter += 1

         if guess > num:
            print('Wrong. Your guess was too high. Try again.\n')
            continue

         elif guess < num:
            print('Wrong. Your guess was too low. Try again.\n')
            continue

         elif guess == num:
            print('Congratulations! It took you ', counter, ' times to guess right!')

            while True:
                y = str(input('Would you like to play again?(y/n): '))
                if y.casefold() == 'y':
                    counter = 0
                    while True:
                        try:
                            a = int(input('Choose the upper range: '))
                            b = int(input('Choose the lower range: '))
                            if a < b:
                                print('The upper range is less than the lower range. Please try again.\n')
                            else:
                                break
                        except:
                            print('Invalid input. Try again.\n')
                    num = random.randint(b, a)
                    break
                elif y.casefold() == 'n':
                    print('Thanks for playing!')
                    isplaying = False
                    break

         if isplaying == False:
            break


guessing_game()
>>>>>>> 9bee5a935db4b50cd8d8f3b0edcfe50c067b3e3d
