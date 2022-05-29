programming_dictionary = {
    "Bug" : "A error in a program",
    "Loop" :  "never ending circles"
    }

# print(programming_dictionary["Loop"])

#Adding a new entry

programming_dictionary["function"] = "Piece of code you call especially over anf over again"
# print(programming_dictionary)

#Create an empty doctionarry
empty_dictionary = {}

#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictinary
programming_dictionary["Bug"] = "updated defintion!"
# print(programming_dictionary)

#loop through a dictinary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
