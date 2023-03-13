import  random

def guessing_game():
    number_x = random.randint(0,100)\

    while True:
        number_guessed = int(input("What is you number? "))

        if number_guessed == number_x:
            print(f"The number {number_guessed} is correct")
            break
        elif number_guessed < number_x:
            print(f"The number {number_guessed} is too low")
        else:
             print(f"The number {number_guessed} is too high")


guessing_game()
