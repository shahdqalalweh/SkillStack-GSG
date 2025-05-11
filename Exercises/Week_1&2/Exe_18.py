"""
Search for a specific value in a list
    
"""


numbers = [4, 8, 15, 23, 42, 16]
target = int(input("Enter number to search: "))

if target in numbers:
    print(f"{target} is in the list ")
else:
    print(f"{target} is NOT in the list ")
