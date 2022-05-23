import random
from saga.archer import Archer
from saga.mage import Mage
from saga.paladin import Paladin
from saga.player import Player

names = ["Ричард", "Кэлен", "Зеддикус", "Даркен Рал"]

def fight(player_1: Player, player_2: Player):
    while(player_1.health > 0 and player_2.health > 0):
        print(f"({player_1.class_name}) {player_1.name} vs ({player_2.class_name}) {player_2.name}")

        player_2.health -= player_1.power
        print(f"({player_1.class_name}) {player_1.name} наносит урон {player_1.power} противнику ({player_2.class_name}) {player_2.name}")
        if player_2.health <= 0:
            print(f"({player_2.class_name}) {player_2.name} погибает")
            break

        player_1.health -= player_2.power
        print(f"({player_2.class_name}) {player_2.name} наносит урон {player_2.power} противнику ({player_1.class_name}) {player_1.name}")
        if player_1.health <= 0:
            print(f"({player_1.class_name}) {player_1.name} погибает")
            break
    
    if player_1.health > 0:
        return player_1
    else:
        return player_2

if __name__ == "__main__":
    count_players = 2
    classes = [Paladin(), Archer(), Mage()]
    players = []
    for i in range(count_players):
        players.append(random.choice(classes))

    for el in players:
        print(f"Players: ({el.class_name}) {el.name}, {el.health}, {el.power}")
    
    winner = fight(players.pop(), players.pop())

    print(winner.name)
