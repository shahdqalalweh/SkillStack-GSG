"""
Compare two numbers and print the greater.

"""
num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else :
    print("They are equales")