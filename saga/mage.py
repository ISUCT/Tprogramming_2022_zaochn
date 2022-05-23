import random
from saga.player import Player

class Mage(Player):

    def __init__(self):
        self.health = round(random.random() * 100)
        self.power = round(random.random() * 50)
        self.class_name = "Маг"

    def health(self, value):
        return value

    def power(self, value):
        return value

    def name(self, value):
        return value

    def class_name(self, value):
        return value

    def special_ability(self, ability):
        print(f"Абилка: {ability}")
