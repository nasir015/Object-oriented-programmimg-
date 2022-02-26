from frist_module import Nasir

class Rayhan(Nasir):
    def __init__(self, name, age, food, animal):
        super().__init__(name, age, food)
        self.animal = animal
    def show_animal(self):
        print(self.animal)