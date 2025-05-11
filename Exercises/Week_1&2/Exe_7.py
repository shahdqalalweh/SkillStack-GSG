"""
Write an algorithm to compute the factorial of a number. Ask the user to input a
positive integer n, then calculate and print the factorial value (n! = n × (n-1) × ... ×
1).
"""
# Solution

n = int(input("Enter a Psitive Number :"))
Fact = 1
if n < 0 :
    print ("Enter a positive number ")
    
else:
    for x in range (1,n):
        Fact = Fact +( Fact * x)


print (Fact)