#step 1
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']






word_list = ["ardvark", "babbon", "camel"]

#Randomy choose a word from the list and assing it to the variable chosen_word
import random

chosen_word = random.choice(word_list)
print(f'the chosen word is : {chosen_word}')

display = []
word_length = len(chosen_word)
for i in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Enter your 1st guess:").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
