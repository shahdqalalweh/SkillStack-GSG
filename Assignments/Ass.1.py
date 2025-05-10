
# Q1: Write pseudocode for checking if a year is a leap year.
 # Here the def. of leap year 
    # year % 400 ==0 => Leap
    # year % 4 ==0 && year % 100 !=0 => Leap
    # year % 4 !=0 => Not leap
    # year % 100 ==0 && year % 400 != 0 => Not leap

year = int(input("Enter a year: ")) #ask the user to get a year

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year") 
   
else:
    print("Not a leap year")  


#Q2: Write a loop that prints the multiplication of a given number.

Num = int(input("Enter a Number: ")) #Input : Number

for i in range(1, 11): #For loop to multi. the number in range bettwen 1-10
    print(f"{Num} x {i} = {Num * i}")
