print("Welcome to the ticketing machine")

height = int(input("Please enter your height: "))
bill = 0

if height >= 120 :
    print("You can ride the Rollercoaster!")
    age = int(input("Please enter your age:"))

    if age < 12:
        bill = 5
        print(f"Child tickets are : ${bill}dollars.")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill} dollars")
     #Adds mild life crisis , uses logical operators
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Adult  tickets are  ${bill} dollars")
    else:
        bill = 12
        print(f"Adult  tickets are  ${bill} dollars")

    wants_photo = input("Do you want photo taken? Y or N  ")
    if wants_photo == "Y":
        bill += 3

    print(f'Your bill is {bill}')

else:
    print("Sorry you have to grow taller to ride the Rollercoaster!")
