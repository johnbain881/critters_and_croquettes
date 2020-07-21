from .animal import Animal
from movements import Walking

class Goat(Animal, Walking):

    def __init__(self, name, species, food, chip_num, shift):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
