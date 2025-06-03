"""

Generate and print the multiplication table for a given number.
"""

num = int(input("Enter a number for its multiplication table: "))
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")
