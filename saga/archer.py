import random
from saga.player import Player

class Archer(Player):

    is_ability_activated = False 

    def __init__(self):
        self.health = round(random.random() * 100)
        self.power = round(random.random() * 50)
        self.damage = self.power
        self.class_name = "Лучник"
        self.ability_name = "Огненные стрелы"

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
        print(f"СТРЕЛЫ: {self.is_ability_activated}")
        if self.is_ability_activated == False:
            self.is_ability_activated = True
            self.damage = 0
            return 0
        else:
            self.damage = self.power + 2
            return self.damage
