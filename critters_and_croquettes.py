# import the python datetime module to help us create a timestamp
from attractions import Anaconda
from attractions import Copperhead
from attractions import Python
from attractions import Rat_Snake
from attractions import Viper
from attractions import Beta
from attractions import Goldfish
from attractions import Koi
from attractions import Mallard
from attractions import Salmon
from attractions import Donkey
from attractions import Goat
from attractions import Llama
from attractions import Rabbit
from attractions import Sheep
from attractions import PettingZoo
from attractions import SnakePit
from attractions import Wetlands


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


petting_zoo = PettingZoo("Petting Zoo")
snake_pit = SnakePit("Snake Pit")
wetlands = Wetlands("Wetlands")

petting_zoo.addAnimals([walking_animal1, walking_animal2, walking_animal3, walking_animal4, walking_animal5])
snake_pit.addAnimals([snake1, snake2, snake3, snake4, snake5])
wetlands.addAnimals([fish1, fish2, fish3, fish4, fish5])

# print(fish2)

# print(petting_zoo.last_critter_added)
# print(petting_zoo)
# print(snake_pit)
# print(wetlands)
walking_animal3.feed()
snake3.feed()
fish5.feed()