"""
Write an algorithm to compute the average of an unknown number of grades. Ask
the user to input grades continuously until -1 is entered. Then, calculate and print
the average of all entered grades (excluding -1).

"""
# Solution
total = 0
count = 0

while True:
    x = int(input("Enter grades:"))
    if x == -1:
        break
    total = total + x
    count = count +1
   


print (float(total/count))
