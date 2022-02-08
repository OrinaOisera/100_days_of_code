print("Welcome to the love calculator")

name1 = input("What is your name \n")
name2 = input("What is your name \n")


combined_string = name1 + name2


lowe_case_string = combined_string.lower()

t = lowe_case_string.count("t")
r = lowe_case_string.count("r")
u = lowe_case_string.count("u")
e = lowe_case_string.count("e")

true = t + r + u + e

l = lowe_case_string.count("l")
o = lowe_case_string.count("o")
v = lowe_case_string.count("v")
e = lowe_case_string.count("e")

love = l + o + v +  e

love_score = int(str(true) + str(love))

if (love_score < 10 ) or (love_score > 90):
     print(f"Your score is {love_score} , you go together like Coke and Mint")
elif (love_score >= 40) and (love_score>=50):
    print(f"Your score is {love_score} , you are alright together")

else:
    print(f"Your score is {love_score} ")
