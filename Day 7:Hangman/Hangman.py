#step 1

word_list = ["ardvark", "babbon", "camel"]

#Randomy choose a word from the list and assing it to the variable chosen_word
import random

chosen_word = random.choice(word_list)

#Ask the user to assign their answer to a variable called gues.MAKE THE Guess lowr case.
guess = input("Enter your 1st guess:").lower()

#check if the leeter the uer guessed is one of the letters in the chosen_word


for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
