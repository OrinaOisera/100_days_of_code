print("Welcome to the tip calculator.")
total_bill = input("what was the total bill? ")
print(total_bill[1:])
x = total_bill[1:]
int_bill = float(x)

tip_perc = int(input("What percentage would you likee to give ? 10, 12 , or , 15 ?"))
people = int(input("How many people to split the bill? "))

final_bill = int_bill +((tip_perc/ 100) * int_bill)
print(final_bill)

each_bill = final_bill / people
final_each = round(each_bill, 2)
print(final_each )

