print('''
*******************************************************************
 ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                           
                                                                           
                                                               
           88           88                                 88  
           ""           88                                 88  
                        88                                 88  
 ,adPPYba, 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
a8P_____88 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
8PP""""""" 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
"8b,   ,aa 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
 `"Ybbd8"' 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  

***********************************************************************

    ''')
print("Welcome to Treasure island ")
print("Your Mission is to find the Treasure")

cross_road = input('You\'re at a cross road do you want to got left or right. Type "left" or "right" \n ').lower()

if cross_road == "left":
    print("You have taken  the path less travelled and nowYou are at a river bank on at a river called river Nile. ")
    river = input(
        'You hear the pharaohs coming with their chariots from a far , You jump into the river.Do you want to  Swim  across or hide in the water and Wait? Type "swim" or "Wait"  \n ').lower()
    if river == "wait":
        print(
            "A cloud suddenly appears  and tells you to run to a cave nearby. Where you see three doors into the cave")
        door = input(
            'You see three doors one "Red"  the other "Blue" and the "Yellow".Which door do you choose to open ?  \n  ').lower()
        if door == "yellow":
            print("You win!")
        elif door == "red":
            print("Game over , burned by fire")
        elif door == "blue":
            print("Game over , eaten by beast")
        else:
            print("Game over!")
    else:
        print("You have been attacked by Trouts!!!! Game over")
else:
    print("Fall into a hole Game Over")
