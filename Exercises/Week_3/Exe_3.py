# Recursive function 

# factorial


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


x = int(input("Enter Number"))

print(factorial(x))


# Another way

def fact_loops(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = fact * i
    return fact


