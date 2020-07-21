# import the python datetime module to help us create a timestamp
from animals import Anaconda
from animals import Copperhead
from animals import Python
from animals import Rat_Snake
from animals import Viper
from animals import Beta
from animals import Goldfish
from animals import Koi
from animals import Mallard
from animals import Salmon
from animals import Donkey
from animals import Goat
from animals import Llama
from animals import Rabbit
from animals import Sheep
from attractions import PettingZoo
from attractions import SnakePit
from attractions import Wetlands
from animals import Goose


snake1 = Anaconda("snake1", "snake", "food", 1)
snake2 = Copperhead("snake2", "snake", "food", 2)
snake3 = Python("snake3", "snake", "food", 3)
snake4 = Rat_Snake("snake4", "snake", "food", 4)
snake5 = Viper("snake5", "snake", "food", 5)
fish1 = Beta("fish1", "fish", "food", 6)
fish2 = Goldfish("fish2", "fish", "food", 7)
fish3 = Koi("fish3", "fish", "food", 8)
fish4 = Mallard("fish4", "fish", "food", 9)
fish5 = Salmon("fish5", "fish", "food", 10)
walking_animal1 = Donkey("walking_animal1", "mammal", "food", 11, "morning")
walking_animal2 = Goat("walking_animal2", "mammal", "food", 12, "morning")
walking_animal3 = Llama("walking_animal3", "mammal", "food", 13, "evening")
walking_animal4 = Rabbit("walking_animal4", "mammal", "food", 14, "noon")
walking_animal5 = Sheep("walking_animal5", "mammal", "food", 15, "noon")


petting_zoo = PettingZoo("Petting Zoo", "cute and fuzzy critters to cuddle")
snake_pit = SnakePit("Snake Pit", "slither slither slither")
wetlands = Wetlands("Wetlands", "swim swim swim")

# petting_zoo.addAnimals([walking_animal1, walking_animal2, walking_animal3, walking_animal4, walking_animal5])
# snake_pit.addAnimals([snake1, snake2, snake3, snake4, snake5])
# wetlands.addAnimals([fish1, fish2, fish3, fish4, fish5])

petting_zoo.add_animal(walking_animal1)
petting_zoo.add_animal(walking_animal2)
petting_zoo.add_animal(walking_animal3)
petting_zoo.add_animal(walking_animal4)
petting_zoo.add_animal(walking_animal5)

snake_pit.add_animal(snake1)
snake_pit.add_animal(snake2)
snake_pit.add_animal(snake3)
snake_pit.add_animal(snake4)
snake_pit.add_animal(snake5)

wetlands.add_animal(fish1)
wetlands.add_animal(fish2)
wetlands.add_animal(fish3)
wetlands.add_animal(fish4)
wetlands.add_animal(fish5)

bob = Anaconda("Bob", "Canada goose", "watercress sandwiches", 16)
# bob.run()
# bob.swim()


varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)

for animal in varmint_village.animals:
    print(animal)