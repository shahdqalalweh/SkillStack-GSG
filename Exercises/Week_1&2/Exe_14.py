"""
Check if a character is inside a string or not.
"""


text = input("Enter a string: ")
char = input("Enter a character to search for: ")

if char in text:
    print(f"The character '{char}' is in the string.")
else:
    print(f"The character '{char}' is NOT in the string.")
