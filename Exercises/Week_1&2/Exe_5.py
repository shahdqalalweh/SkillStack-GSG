"""
Write an algorithm that counts the number of passes and fails in a group of students.
Keep asking the user to enter student grades until the user enters -1 to stop. A
passing grade is considered 60 or higher. Print the number of passing and failing
students, and the failure percentage.

"""
# Solution

Numbers = []


while True:
    x = int(input("Enter student grade (-1 to stop): "))
    if x == -1:
        break
    Numbers.append(x)


passing = []
failing = []

for grade in Numbers:
    if grade >= 60:
        passing.append(grade)
    else:
        failing.append(grade)


if len(Numbers) > 0:
    fail_percentage = (len(failing) / len(Numbers)) * 100
else:
    fail_percentage = 0


print(f"Passing students: {len(passing)}")
print(f"Failing students: {len(failing)}")
print(f"Fail percentage: {fail_percentage:.2f}%")
