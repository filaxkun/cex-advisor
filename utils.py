import re

def getGameNames():
    name_list = []
    with open('game_list.py', 'r') as game_list:
        for line in game_list:
            name_list.append(re.split(' ',line)[0])
    return name_list


def getLine( file_to_grep, word ):
    with open( file_to_grep, 'r') as result:
        for line in result:
            if re.search('itemDetail',line):
                return(line)

def getPriceList( string_to_scrape ):
    return re.findall('\d\d?\.\d\d',string_to_scrape)
