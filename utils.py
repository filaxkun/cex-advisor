import re

def getGameNames():
    name_list = []
    with open('game_list.py', 'r') as game_list:
        for line in game_list:
            name_list.append(re.split(' ',line)[0])
    return name_list

def getLine( word, str_to_grep ):
        for line in str_to_grep.split('\n'):
            if re.search( word, line ):
                return(line)


def getPriceList( string_to_scrape ):
    return re.findall('\d\d?\.\d\d',string_to_scrape)
