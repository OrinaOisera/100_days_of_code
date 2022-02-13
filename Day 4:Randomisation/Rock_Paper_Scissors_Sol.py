Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


import  random

game_images = [Rock, Paper, Scissors]

user_hand = int(input("What do you choose ? Type 0 for Rock   1 for Paper    2 for Scissor\n"))
if user_hand >= 3 or user_hand < 0:
    print("You typed am invalid number , You lose! ")
else:
    print(game_images[user_hand])

    computer_hand = random.randint(0,2)
    print(game_images[computer_hand])

    if user_hand == 0 and computer_hand == 2:
        print("You win")
    elif computer_hand == 0 and user_hand == 2:
        print("You lose")
    elif computer_hand == user_hand:
        print("it is a draw")
    elif computer_hand > user_hand:
        print("You lose")
    elif user_hand > computer_hand:
        print("You win")
    elif user_hand >= 3 or user_hand < 0:
        print("You typed am invalid number , You lose! ")
