programming_directory = {
    "Bug" : "Yellllllow",
    "Function" : "blueeee",
    "loop": "Circual",
}

print(programming_directory ["Bug"])


#Adding  new items  to dictinary
programming_directory ["Circle"] = "Shape  of the programme"
print(programming_directory)

#Empty dictinary
empty_dictionary = {}

#Wipe an exisisintg dictinary
# programming_directory = {}
# print(programming_directory)

#edit an item in a dict
programming_directory["Bug"] = "Blueeeeee"
print(programming_directory)

#loop through a dic
for key in programming_directory:
  print(key)
  print(programming_directory[key])
