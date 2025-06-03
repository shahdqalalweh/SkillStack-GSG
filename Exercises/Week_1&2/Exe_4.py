"""
Write an algorithm to find the maximum number in a list of integers. First, ask the
user how many numbers they want to enter. Then, input the numbers one by one
and determine the largest among them.

"""
# Solution

x = int(input("Enter how many numbers you want to enter: "))

Numbers = []

for l in range(x):
    num = int(input(f"Enter number {l+1}: "))
    Numbers.append(num)

Max_N = Numbers[0]

for i in range(1, x):
    if Numbers[i] > Max_N:
        Max_N = Numbers[i]

print("The maximum number is:", Max_N)

