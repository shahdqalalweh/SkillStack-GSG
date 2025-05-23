"""

Recursive Calculator
Implement a recursive function to calculate the power of a number (e.g., ab).
Create a menu that allows the user to choose to calculate power, square, or exit.
"""
# solution

def power_recursive(a, b):
   
    if b == 0:
        return 1
    
    return a * power_recursive(a, b - 1)

def menu():
    while True:
        print("\n--- Recursive Calculator ---")
        print("1. Calculate Power (a^b)")
        print("2. Calculate Square (a^2)")
        print("3. Exit")

        choice = int(input("Enter your choice (1-3): "))

        if choice == 1:
            a = int(input("Enter base (a): "))
            b = int(input("Enter exponent (b): "))
            result = power_recursive(a, b)
            print(f"{a}^{b} = {result}")

        elif choice == 2:
            a = int(input("Enter number: "))
            result = power_recursive(a, 2)
            print(f"{a}^2 = {result}")

        elif choice == 3:
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


menu()
