import random
from saga.player import Player

class Mage(Player):

    def __init__(self):
        self._health = round(random.random() * 100)
        self.power = round(random.random() * 50)
        self.damage = self.power
        self.class_name = "Маг"
        self.ability_name = "Заворожение"
        self.is_ability_activated = False

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        #print(f"HealthSetter: {value}, {self.health}")
        if self.is_ability_activated == True:
            self._health = self.health
            self.is_ability_activated = False
        else:
            self._health = value

    def power(self, value):
        return value

    def name(self, value):
        return value

    def class_name(self, value):
        return value

    def ability_name(self, value):
        return value

    def is_ability_activated(self, value):
        return value

    def damage(self, value):
        return value

    def special_ability(self):
        if self.is_ability_activated == False:
            self.is_ability_activated = True
            self.damage = self.power
            return 0
        else:
            return self.damage
