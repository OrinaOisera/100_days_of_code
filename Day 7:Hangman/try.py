import random


word_list = ["camel", "apple",  "tom", "axe"]

chosen_word = random.choice(word_list)

print(chosen_word)

display = []

for i in range(len(chosen_word)):
    display += "_"
print(display)

guess = input("Please guess your first letter: ").lower()

for position in range(len(chosen_word)):
     letter = chosen_word[position]
     if letter == guess:
         display[position] = letter
         print(display)

