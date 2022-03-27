# step 1
import Hangman_art
import Hangman_words


# Randomy choose a word from the list and assigning it to the variable chosen_word
import random

chosen_word = random.choice(Hangman_words .word_list)
print(Hangman_art.logo)
print(f'the chosen word is : {chosen_word}')

display = []
word_length = len(chosen_word)
for i in range(word_length):
    display += "_"
print(display)

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Enter your 1st guess:").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f'You guessed {guess}, that is not in the word  you lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f"{''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")
    print(lives)
    print(Hangman_art. stages[lives])
