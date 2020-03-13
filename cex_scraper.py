import re
import time
from selenium import webdriver

RED   = '\033[0;31m'
GREEN = '\033[0;32m'
ENDC  = '\033[0m'

# Game list
import games
gamez = games.games_dict_list
print('Loading my list of gamez...')

# Init "browser"
opt = webdriver.ChromeOptions()
opt.add_argument('headless')
br = webdriver.Chrome(options=opt)
 
for game in gamez:
    print('checking game:', game['name'], end='')
    
    br.get( game['url'] )
    
    # check status
    time.sleep(2)
    
    print('\t[render done]')

    try:
        sell_price    = br.find_element_by_id("Asellprice").text[1:] 
        cash_price    = br.find_element_by_id("Acashprice").text[1:] 
        voucher_price = br.find_element_by_id("Aexchprice").text[1:]

        cex_price_list = [sell_price, cash_price, voucher_price]
        print( cex_price_list , end = '  ')
    
        balance = float(voucher_price) - game['buy_price']
        if( balance > 0 ):
            print( GREEN + '\t+',abs(balance), end=ENDC+'\n' )
        else:
            print( RED   + '\t-',abs(balance), end=ENDC+'\n' )
 
        print('url done.')
    except:
        print('- problemz -')

br.quit()
