import os
import re
import utils
from requests_html import HTMLSession as HTMLS

# Game list
gameList = utils.getGameList()
print(gameList)

darkSoulRem = 'https://ie.webuy.com/product-detail?id=3391891997324&categoryName=playstation4-software&superCatName=gaming&title=dark-souls-remastered'
darkSoul3   = 'https://ie.webuy.com/product-detail?id=3391891987332&categoryName=playstation4-software&superCatName=gaming&title=dark-souls-iii'

myGamezUrls = [ darkSoulRem ]

print('getting from my gamez list...')

for url in myGamezUrls:
    print('url:',url)

    session = HTMLS()
    page = session.get(url)

    page.encoding = page.apparent_encoding
    
    print(page.encoding)

    page.html.render()
    print('render done.')

    renderedPage = page.html.html
    with open("results.txt","a+") as txt_file:
       txt_file.write(renderedPage)
    print('url done.')

#cat result | grep itemDetailsDiv

