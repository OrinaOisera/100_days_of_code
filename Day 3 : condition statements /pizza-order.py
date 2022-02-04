#Multiple if statements
print("Welcome to Pizza Hut!")

pizza_size = input("Please enter size of pizza you want; Enter : S- small  pizza , M  - medium , L - large: ")
add_pepperoni = input("Add pepperoni: Y or N:  ")
extra_cheese = input("Add extra cheese: Y or N:  ")
bill = 0


if pizza_size == "S":
    bill += 15

elif pizza_size == "M":
    bill += 20
elif pizza_size == "L":
    bill += 25

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f"Your total bill is ${bill}")
