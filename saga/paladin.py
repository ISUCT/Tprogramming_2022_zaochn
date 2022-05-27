import random
from saga.player import Player

class Paladin(Player):

    def __init__(self):
        self.health = round(random.random() * 100)
        self.power = round(random.random() * 50)
        self.damage = self.power
        self.class_name = "Паладин"
        self.ability_name = "Удар возмездия"
        self.is_ability_activated = False

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

    def is_ability_activated(self, value):
        return value

    def damage(self, value):
        return value

    def special_ability(self):
        self.damage = self.power
        return round(self.power * 1.3)
        
