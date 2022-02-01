# A program that calculates whether a year is alep year or not.
#  A year is leap year if:
#   on every year that is evenly dividible by 4
#   exxept every year that is evenly divisible by 100
#    unless the year is aslso evenly divisble by  400

# year = 2000
#  2000 / 4 = 500 (leap)
#  2000 / 10 = 20 (not Leap)
#  2000 /400 = 5  (leap)

year = int(input("Enter the year: "))

print(year)


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
          print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")





