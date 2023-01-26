import random

def guessing_game():
    number_x = random.randint(0,100)
    while True:
        user_guess = int(input("What is you guess:"))
        if user_guess == number_x :
            print(f' Your answer {user_guess} is correct')
            break
        if  user_guess < number_x:
             print(f' Your answer {user_guess} is too low')
        else:
              print(f' Your answer {user_guess} is too High')

guessing_game()
