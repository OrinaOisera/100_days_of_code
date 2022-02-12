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
computer_hand = random.randint(0, 3)
user_hand = int(input("What do you choose ? Type 0 for Rock   0 for Paper    2 for Scissor"))
# 0 = rock
# 1 = Paper
# 2= Scissors

# 0 and  1    _-->  1 wins
# 0 and 2 ----> 0 wins
# 0 and 0   ----> tie
# 1 and  1    _-->  tie
# 1 and 2 ----> 2 wins
# 1 and 0   ---->  1 wins
# 2 and  1    _-->  2 wins
# 2 and 2 ---->   tie
# 2 and 0   ---->  0 wins



if user_hand == 0 :
    print(Rock)
    print(computer_hand)
    if user_hand == computer_hand:
        print("Computer plays Rock")
        print(Rock)
        print("It is a tie!")
    elif computer_hand == 1 :
        print("Computer plays Paper")
        print("")
        print("Computer Wins!")
    elif computer_hand == 2:
           print("Computer plays Scissors")
           print(Scissors)
           print("You Wins")

elif user_hand == 1 :
    print(Paper)
    print(computer_hand)
    if user_hand == computer_hand:
        print("Computer plays Paper")
        print(Paper)
        print("It is a tie!")
    elif computer_hand == 0 :
        print("Computer plays  Rock")
        print(Rock)
        print("You win")
    elif computer_hand == 2:
           print("Computer plays Scissors")
           print(Scissors)
           print("Computer wins")



elif user_hand == 2:
    print(Scissors)
    print(computer_hand)
    if user_hand == computer_hand:
            print("Computer plays Scissors")
            print(Scissors)
            print("It is a tie!")
    elif computer_hand == 0 :
            print("Computer plays Rock")
            print(Rock)
            print("Computer wins")
    elif computer_hand == 1:
            print("Computer plays Paper")
            print()
            print(" yOU win")
