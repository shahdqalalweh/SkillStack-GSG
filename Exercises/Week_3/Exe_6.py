import os

if os.path.exists("test1.txt"):
    f = open("test1.txt", mode="r") # r: for reading
    l = f.readline()

    print(f"The line is: {l}")

    f1 = open("out.txt", mode="a") # w: for writing, a: append

    f1.write("Hello World!\n")
    f1.write("Gaza Sky Geeks!")

    f.close()
    f1.close()

# Writing to a file:
with open("data.txt", "w") as f:
    f.write("Jenin !!!")
    


