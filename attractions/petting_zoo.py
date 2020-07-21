from .attraction import Attraction

class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def last_critter_added(self):
        return self.animals[-1]