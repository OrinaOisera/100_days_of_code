def prime_nmber(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not prime number")


n = int(input("Check this number:"))

prime_nmber(number=n)
