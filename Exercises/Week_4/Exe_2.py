class Human:
    def __init__(self, name):
        self.name = name # Instance variable

    def say_hello(self):
        print(f"Hi, I am {self.name}.")


person1 = Human("Alice")
person2 = Human("Bob")

person1.say_hello() # Output: Hi, I am Alice.
person2.say_hello() # Output: Hi, I am Bob.