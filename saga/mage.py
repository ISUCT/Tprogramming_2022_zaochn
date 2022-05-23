import random
from saga.player import Player

class Mage(Player):

    def __init__(self):
        self.health = round(random.random() * 100)
        self.power = round(random.random() * 50)
        self.damage = self.power
        self.class_name = "Маг"
        self.ability_name = "Заворожение"

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

    def damage(self, value):
        return value

    def special_ability(self):
        self.damage = round(self.power * 1.3)
        return self.damage
