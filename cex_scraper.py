from requests_html import HTMLSession as HTMLS
import sys
from bs4 import BeautifulSoup as bsup

# Game list
darkSoulRem = 'https://ie.webuy.com/product-detail?id=3391891997324&categoryName=playstation4-software&superCatName=gaming&title=dark-souls-remastered'
darkSoul3   = 'https://ie.webuy.com/product-detail?id=3391891987332&categoryName=playstation4-software&superCatName=gaming&title=dark-souls-iii'

myGamez = [ darkSoulRem , darkSoul3 ]


# -------------------------------------- #

if(len(sys.argv)>=2):
    url = ['http://'+sys.argv[1]]
else:
    url = myGamez
    print('getting from my gamez list...')

for game_url in url:
    print('url:',game_url)

    session = HTMLS()
    page = session.get(game_url)

    page.html.render()
    #print(page.html.html)

    soup = bsup(page.html.html,'html.parser')

    print(soup.prettify())

#cat result | grep -A 40 itemDetailsDiv
