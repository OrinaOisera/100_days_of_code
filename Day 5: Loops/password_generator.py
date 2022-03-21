import  random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A" , "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"," L", "M", "N"," O",  "P"," Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ['o', "1", "2", "3", "4","5", "6", "7", "8", "9"]
symbols = ["!", '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword Generator!")


nr_letters = int(input("How many letters would like your password to have\n"))
nr_symbols = int(input("How many symbols would like your password to have\n"))
nr_numbers = int(input("How many numbers would like your pass word to have\n"))

# #Easylevel
password = ""

for char in range (1, nr_numbers + 1 ):
    password += random.choice(numbers)
for char in range(1, nr_letters):
    password += random.choice(letters)
for char in range(1, nr_symbols):
    password += random.choice(symbols)


pass_1 = ''.join(random.sample(password,  len(password)))
print(pass_1)
#Hard Level

password_list =  []

for char in range (1, nr_numbers + 1 ):
    password_list+= random.choice(numbers)
for char in range(1, nr_letters):
    password_list += random.choice(letters)
for char in range(1, nr_symbols):
    password_list += random.choice(symbols)
password_list_shuffle = random.shuffle(password_list)

#Converts back to string
pass_str = ""
for char in password_list:
    pass_str += char
print(pass_str)

