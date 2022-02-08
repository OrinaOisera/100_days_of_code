print("Welcome to the love calculator")

name1 = input("What is your name \n")
name2 = input("What is your name \n")


first_name = name1.lower()
second_name = name2.lower()

t = 0
r = 0
u = 0
e = 0

l = 0
o = 0
v = 0
e = 0


#start for true

t = first_name.count("t") + second_name.count("t")
r = first_name.count("r") + second_name.count("r")
u = first_name.count("u") + second_name.count("u")
e = first_name.count("e") + second_name.count("e")


l = first_name.count("l") + second_name.count("l")
o = first_name.count("o") + second_name.count("o")
v = first_name.count("v") + second_name.count("v")
e = first_name.count("e") + second_name.count("e")


true_total =  t + r + u + e
love_total = l + o + v + e
print(true_total)
print(love_total)
overal_Score = int('{}{}'.format(true_total, love_total))
print(f"Your love score is: {overal_Score}")
# overal_Score = int('{}{}'.format(true_total, love_total))
# print(overal_Score)

if overal_Score < 10 or overal_Score > 90:
    print(f"Your score is {overal_Score} , you go together like Coke and Mint")

elif 40 < overal_Score < 50: 
    print(f"Your score is {overal_Score} , you are alright together")
else:
    print(f"Your scoore is {overal_Score} ")
