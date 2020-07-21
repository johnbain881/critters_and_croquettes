from .animal import Animal
from datetime import date
from movements import Walking

class Llama(Animal, Walking):

    def __init__(self, name, species, food, chip_num, shift):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    
    def feed(self):
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')
