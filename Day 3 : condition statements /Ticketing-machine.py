print("Welcome to the ticketing machine")

height = int(input("Please enter your height: "))
bill = 0

if height >= 120 :
    print("You can ride the Rollercoaster!")
    age = int(input("Please enter your age:"))

    if age < 12:
        bill = 5
        print("Child tickets are : $5 dollars.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7 dollars")
    else:
        bill = 12
        print("Adult  tickets are  $12 dollars")

    wants_photo = input("Do you want photo taken? Y or N  ")
    if wants_photo == "Y":
        bill += 3

    print(f'Your bill is {bill}')

else:
    print("Sorry you have to grow taller to ride the Rollercoaster!")
