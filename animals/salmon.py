from .animal import Animal
from movements import Swimming

class Salmon(Animal, Swimming):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)


    def feed(self):
        print(f"{self.name} did loads of swimming upstream today and deserves some {self.food}")