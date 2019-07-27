
# coding: utf-8

# In[1]:


import time, json, requests


# In[2]:


import yajl


# In[3]:


import sys
sys.stdout = open(1, 'w')


# In[4]:


def btstamp():
    bitStampTick = requests.get('https://www.bitstamp.net/api/ticker/')
    
    return bitStampTick.json()['last']


# In[5]:


def bitfinex():
    bitFinexTick = requests.get("https://api.bitfinex.com/v1/ticker/btcusd")
    
    return bitFinexTick.json()['last_price']
   
    


# In[9]:


def coinmarketcap():
    coinMarketCapTick = requests.get("https://api.coinmarketcap.com/v2/ticker/1/")
    
    return coinMarketCapTick.json()['data']['quotes']['USD']['price']


# In[7]:


while True:
    btstampUSDLive = float(btstamp())
    bitfinexUSDLive = float(bitfinex())
    # coinmarketcapUSDLive = float(coinmarketcap())
    
    diffBitfinexBitstamp = btstampUSDLive - bitfinexUSDLive
    
    # print("COINMARKETCAP USD = ", coinmarketcapUSDLive)
    print("BITFINEX USD = ", bitfinexUSDLive)
    print("BITSTAMP USD = ", btstampUSDLive)
    
    print(abs(diffBitfinexBitstamp))
    
    if diffBitfinexBitstamp > 10:
        print("BUY ORDER BITFINEX")
    
    elif diffBitfinexBitstamp < -10:
        print("BUY BITSTAMP")
        
        
    
    print("____________________________")
          
    
    
 
          
    time.sleep(1)


# ## 
