class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.age)


class Nasir(Robot):
    def __init__(self,name,age,food):
        super().__init__(name,age)

        self.food = food

    def show_food(self):
        print(self.food)


