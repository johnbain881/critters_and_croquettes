from datetime import date

class Animal:
    
    def __init__(self, name, species, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        self.__chip_num = chip_num
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food

    @property
    def chip_num(self):
        return self.__chip_num

    @chip_num.setter
    def chip_num(self, num):
        pass

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
    
    def __str__(self):
        return f"{self.name} is a {self.species}"
