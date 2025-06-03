"""

Count how many numbers are positive or negative

"""
numbers = [-5, 3, 0, -2, 8, -9, 1]
positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
