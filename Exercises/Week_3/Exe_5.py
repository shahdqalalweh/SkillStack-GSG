# Local vs Global Example:

x = 10 # global variable

def func():
    x = 5 # local variable
    print("Local x:", x)
   
func()
print("Global x:", x)

M# odifying global variable inside function:

count = 0

def increment():
    global count
    count += 1

increment()
print(count)