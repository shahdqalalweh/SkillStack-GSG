"""
Types of Inheritance in Python:
Single Inheritance: A child class inherits from one parent class.
Multiple Inheritance: A child class inherits from more than one parent class. (Just in Python)
Multilevel Inheritance: A class inherits from a child class which in turn inherits from a parent class.
Hierarchical Inheritance: Multiple child classes inherit from one parent class.
Hybrid Inheritance: A combination of two or more types of inheritance.
"""

from person import Person
from student import Student



class Main:
# Usage
    def run(self):
        s = Student("Alice", "S123")
        s.greet() # Accessing parent method
        s.show_id() # Accessing subclass method
        print(s.name) # Accessing data member from parent class


if __name__ == "__main__":
    main = Main()
    main.run()



