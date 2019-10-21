# Checks uni-coin market cap every 15 minutes
#_*_coding: utf-8_*_

import time
import json
import requests

while True:
    name = 'uni-coin'
    data = requests.get('https://api.coinmarketcap.com/v1/ticker/' + name + '/')
    cap = data.json()[0]['market_cap_usd']
    cap = '{:,}'.format(float(cap))
    cap = cap[:cap.index('.')] # remove dot
    print( name + " market cap = $ " + str(cap) )
    time.sleep(60*15)
