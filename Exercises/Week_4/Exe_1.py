

class Dog:
    def __init__(self, name): #Constructor
        self.name = name # instance variable
    def bark(self):
        print("Woof!")

if __name__ == "__main__":
    my_dog = Dog("Rex")
    anotherDog = Dog("Boby")
    my_dog.bark()
    print(f"My Dog name is {my_dog.name}")
    print(f"Other Dog name is {anotherDog.name}")