from .animal import Animal
from movements import Slithering

class Python(Animal, Slithering):

    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        print(f"{self.name} did some coding today, and is ready to eat some {self.food}")
