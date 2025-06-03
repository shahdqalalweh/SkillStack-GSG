"""

Print even numbers up to a user-defined number N.
"""

N = int(input("Enter a number: "))
print("Even numbers up to", N, ":")
for i in range(2, N+1, 2):
    print(i)
