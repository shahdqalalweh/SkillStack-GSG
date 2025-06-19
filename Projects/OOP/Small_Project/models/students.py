from models.humen import Humen

class Student (Humen):
    def __init__(self,id, name, year_of_birth, scores =[]):
        super().__init__(name, year_of_birth)
        self.id = id
        self.scores = scores

    def introduce(self):
        