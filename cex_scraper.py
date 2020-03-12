import os
import re
import sys
from utils import *
from time import sleep
from requests_html import HTMLSession as HTMLS

RED   = '\033[0;31m'
GREEN = '\033[0;32m'
ENDC  = '\033[0m'

# Game list
import games
gamez = games.games_dict_list
print('Loading my list of gamez...')

for game in gamez:
    print('checking game:', game['name'], end='')

    try:
         session = HTMLS()
         page = session.get( game['url'] )
         page.encoding = page.apparent_encoding
         page.html.render()
         print('\t[render done]')
         
         rendered_page = page.html.html
         
         focus_obj_on_page = getLine( 'itemDetailsDiv', rendered_page )
         
         cex_price_list = getPriceList( focus_obj_on_page )
         sell_price, cash_price, voucher_price = cex_price_list

         print( cex_price_list , end = '  ')
         
         balance = float(voucher_price) - game['buy_price']
         if( balance > 0 ):
             print( GREEN + '\t+',abs(balance), end=ENDC+'\n' )
         else:
             print( RED   + '\t-',abs(balance), end=ENDC+'\n' )

         print('url done.')
    except:
        print('- problemz -')
