import random
from saga.archer import Archer
from saga.mage import Mage
from saga.paladin import Paladin
from saga.player import Player

def one_fight(player_1: Player, player_2: Player):

    print(f"({player_1.class_name}) {player_1.name} vs ({player_2.class_name}) {player_2.name}")

    while(player_1.health > 0 and player_2.health > 0):
        
        is_use_ability = random.choice([True, False])
        if is_use_ability:
            damage = player_1.special_ability()
            player_2.health -= damage
            print(f"({player_1.class_name}) {player_1.name} использует ({player_1.ability_name}) и наносит урон {damage} противнику ({player_2.class_name}) {player_2.name}")
            if player_2.health <= 0:
                print(f"({player_2.class_name}) {player_2.name} погибает\n")
                break
        else:
            player_2.health -= player_1.damage
            print(f"({player_1.class_name}) {player_1.name} наносит урон {player_1.damage} противнику ({player_2.class_name}) {player_2.name}")
            if player_2.health <= 0:
                print(f"({player_2.class_name}) {player_2.name} погибает\n")
                break
        
        is_use_ability = random.choice([True, False])
        if is_use_ability:
            damage = player_2.special_ability()
            player_1.health -= damage
            print(f"({player_2.class_name}) {player_2.name} использует ({player_2.ability_name}) и наносит урон {damage} противнику ({player_1.class_name}) {player_1.name}")
            if player_1.health <= 0:
                print(f"({player_1.class_name}) {player_1.name} погибает\n")
                break
        else:
            player_1.health -= player_2.damage
            print(f"({player_2.class_name}) {player_2.name} наносит урон {player_2.damage} противнику ({player_1.class_name}) {player_1.name}")
            if player_1.health <= 0:
                print(f"({player_1.class_name}) {player_1.name} погибает\n")
                break
    
    if player_1.health > 0:
        player_1.is_ability_activated = False
        return player_1
    else:
        player_2.is_ability_activated = False
        return player_2

def full_fight(players, round: int):
    winners = []
    print(f"Кон {round}.")
    while players:
        winners.append(one_fight(players.pop(), players.pop()))
    
    if len(winners) == 1:
        print(f"Наш победитель: {winners.pop().name}")
    else:
        round += 1
        full_fight(winners, round)
    

if __name__ == "__main__":
    names = ["Ричард", "Кэлен", "Зеддикус", "Даркен Рал", "Геральт", "Цири", "Сангвиний", "Фулгрим"]
    random.shuffle(names)
    round = 1
    count_players = 4
    players = []
    for i in range(count_players):
        players.append(random.choice([Paladin(), Archer(), Mage()]))

    for el in players:
        el.name = names.pop()
        print(f"Player: ({el.class_name}) {el.name}, {el.health}, {el.power}\n")
    
    full_fight(players, round)
