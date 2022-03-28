def greet():
    print("Hello child")
    print("Hello child")
    print("Hello child")


#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Hello {name}")
    print(f"Hello {name}")


greet_with_name("Tom")

#Function with more that one iput


def greet_with(name, location):
    print(f"hello {name} from {location}")

#Positional arguments
greet_with("Tom", "Kitale")

#Key word arguments
greet_with(location="London", name="Angela")


