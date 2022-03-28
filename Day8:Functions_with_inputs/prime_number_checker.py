def prime_n0_checker(number):
 if number > 1:
   for x in range (2, number):
       if number % x == 0:
            print("This is not a prime number")

       else:
            print(f" {number} this  a prime number")


 else:
    print(f" {number} this  a prime number")





n = int(input("Check this number:"))
prime_n0_checker(number=n)
