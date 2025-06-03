"""
Function Definitions and Types
"""
# Function without parameters and no return:

def say_hello():
    print("Hello!")

say_hello() # Calling the fuction

# Function with parameters but no return:

def greet_user(name):
    print("Hello,", name)

greet_user("Ali")

# Function with parameters and a return value:

def add(a, b):
    return a + b

result = add(3, 5)
print(result)


# Function without parameters but with return:

def get_number():
    return 42

print(get_number())