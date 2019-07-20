import re

def getGameList():
    lista = []
    with open('game_list', 'r') as game_list:
        for line in game_list:
            lista.append(re.split(' ',line)[0])
    return lista

