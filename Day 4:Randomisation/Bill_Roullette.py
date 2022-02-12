import random
#Split string methond
name_string = input("Give me everybody's names,separated by commas. ")
names = name_string.split(",")
print(names)
y = len(names)
x = random.randint(0, y - 1)

bill_payer = names[x]
print(f"{bill_payer} you are paying the bill!")

#Use choice
person_wo_will_pay = random.choice(names)
print(person_wo_will_pay)
