import os
import re
from utils import *
from requests_html import HTMLSession as HTMLS

# Game list
import games
#gameNamesList = getGameNames()
gamez = games.games_list
print('Loading my list of gamez...')

#for url in myGamezUrls:
for game in gamez:
    print('checking game:',game['name'])
    #print('url:',url)

    session = HTMLS()
    page = session.get(game['url'])
    page.encoding = page.apparent_encoding
    page.html.render()
    print('render done.')

    renderedPage = page.html.html
    with open("results.txt","w") as txt_file:
       txt_file.write(renderedPage)
    
    stringa_dati = getLine( 'results.txt','itemDetailsDiv')
    
    print(getPriceList(stringa_dati))

    print('url done.')


