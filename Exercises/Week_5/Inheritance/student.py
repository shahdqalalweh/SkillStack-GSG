
from person import Person

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name) # Calling constructor of the parent class
        self.student_id = student_id

    def show_id(self):
        print(f"My ID is {self.student_id}.")

    def greet(self):
        super().greet() # Calling method from the parent class
        print("I am also a student.")

