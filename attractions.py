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


class Llama(Animal):

    def __init__(self, name, species, food, chip_num, shift):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

    
    def feed(self):
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')


class Donkey(Animal):

    def __init__(self, name, species, food, chip_num, shift):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift


class Goat(Animal):

    def __init__(self, name, species, food, chip_num, shift):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift


class Sheep(Animal):

    def __init__(self, name, species, food, chip_num, shift):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift


class Rabbit(Animal):

    def __init__(self, name, species, food, chip_num, shift):
        super().__init__(name, species, food, chip_num)
        self.walking = True
        self.shift = shift

class Copperhead(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Rat_Snake(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Python(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f"{self.name} did some coding today, and is ready to eat some {self.food}")

class Viper(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Anaconda(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Goldfish(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class Mallard(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class Koi(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


class Beta(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True



class Salmon(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True


    def feed(self):
        print(f"{self.name} did loads of swimming upstream today and deserves some {self.food}")


class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute and fuzzy critters to cuddle"
        self.animals = list()


    def __str__(self):
        print_string = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            print_string += f"\n{animal.name}"
        return print_string

    
    def addAnimals(self, animalList):
        self.animals.extend(animalList)


    def last_critter_added(self):
        return self.animals[-1]


class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "sneaky scary snek"
        self.animals = list()


    def __str__(self):
        print_string = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            print_string += f"\n{animal.name}"
        return print_string

    
    def addAnimals(self, animalList):
        self.animals.extend(animalList)

    
    def last_critter_added(self):
        return self.animals[-1]


class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "swim swim swim"
        self.animals = list()


    def __str__(self):
        print_string = f"{self.attraction_name} is where you'll find {self.description}, like"
        for animal in self.animals:
            print_string += f"\n{animal.name}"
        return print_string

    
    def addAnimals(self, animalList):
        self.animals.extend(animalList)

  
    def last_critter_added(self):
        return self.animals[-1]