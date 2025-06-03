"""

Write an algorithm to check if a give number is prime or not.
"""
# Solution without Function


primeORnot = int(input("Enter a number to check if it is prime or not: "))

if primeORnot <= 1:
    print("Not Prime")
else:
    is_prime = True  
    for x in range(2, int(primeORnot / 2) + 1):
        if primeORnot % x == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime")
