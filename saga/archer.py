import random
from saga.player import Player

class Archer(Player):

    def __init__(self):
        self.health = round(random.random() * 100)
        self.power = round(random.random() * 50)
        self.damage = self.power
        self.class_name = "Лучник"
        self.ability_name = "Огненные стрелы"
        self._is_ability_activated = False

    def health(self, value):
        return value

    def power(self, value):
        return value

    def name(self, value):
        return value

    def class_name(self, value):
        return value

    def ability_name(self, value):
        return value  

    @property
    def is_ability_activated(self):
        return self._is_ability_activated

    @is_ability_activated.setter
    def is_ability_activated(self, newValue):
        if newValue == False:
            self.damage = self.power
        self._is_ability_activated = newValue

    def damage(self, value):
        return value

    def special_ability(self):
        if self.is_ability_activated == False:
            self.is_ability_activated = True
            self.damage = self.power + 2
            return 0
        else:
            return self.damage
