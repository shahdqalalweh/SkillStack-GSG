"""

Create a condition where a user is granted access only if both the username and password match predefined values. Use
logical operators to combine conditions:
"""

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Access granted ")
else:
    print("Access denied ")
