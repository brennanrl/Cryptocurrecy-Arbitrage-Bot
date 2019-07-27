
# coding: utf-8

# In[1]:


import sys
sys.stdout = open(1, 'w')


# In[2]:


import time
import requests
import dateparser 

from binance.client import Client as BinanceClient
from kucoin.client import Client


# In[3]:


client = Client('5b63c73008d8b104b0add6b0', 'd239ffe0-0120-49eb-9a85-04e712244f47')
# client = Client('5b7c872808d8b15529c035c3', 'fc3810e5-462d-413b-9a88-aac40203f8cc')

bclient = BinanceClient('wZUkR3OrwI953kvURKvRXiwTT41xT0Qsh1G7UfB6rz5kbGM0t9qspLAYaUCpfk7z', 'ybvMtTm4PeOGT0bJ5CrQugI5Wpdi2OcvaIoB0wAD462lekazGP0wRirDXL5kIbJM')
# bclient = BinanceClient('EDSFRPjwir0HhT4oZhCUHace2wIVxtqKpmdtpjla47Dxlp07WRoRCAVVrtKjEXso', 'V6JY4yWcPbhMleYUWacgItMaECdxY0TcDW1mD3SZZje8pwYFepnjlzRcUabCwQxX')


# In[4]:


# KUCOIN
currencies = client.get_currencies()

orders = client.get_buy_orders('ETH-BTC', limit=50)
sellorders = client.get_sell_orders('ETH-BTC', limit=50)

# account balance
userFee = 0.002
# accountBalanceKucoin = 0.0009027 * (1 - userFee)# 0.0009145 * (1 - userFee) 
accountBalanceKucoinBTC = (float(client.get_coin_balance('BTC')['balance'])) * (1 - userFee)
FixedAccountBalanceKucoin = 0.0018 
accountBalanceKucoin = (float(client.get_coin_balance('ETH')['balance'])) * (1 - userFee) 


# In[5]:


# BINANCE
depth = bclient.get_order_book(symbol='ETHBTC')


# In[6]:


print(orders)
print(sellorders)
print(depth)


# In[7]:


coins = client.get_trading_symbols() # get all kucoin prices
prices = bclient.get_all_tickers() # get all binance prices
print(coins)


# In[8]:


kucoinDict = {} # create a dictionary

for coin in coins:
    print(coin['lastDealPrice'])

        


# In[ ]:


print(kucoinDict['ETHBTC'])


# In[ ]:


# does exact same for binance


binancePriceDict = {}

for price in prices:
    bsymbol = price['symbol']
    bprice = price['price']
    if bsymbol in kucoinDict:
        binancePriceDict[bsymbol] = bprice

for price, lol in binancePriceDict.items():
    print(price, lol)


# In[7]:


# this is a dict of all the fees
coinFeesDict = {'RPXETH': 1, 'ARNETH': 1.8, 'OMGETH': 0.1, 'GASETH': 0, 'MTHETH': 10, 'GVTETH': 0.1,
                'PPTETH': 0.1, 'CVCETH': 3, 'LOOMETH': 10, 'ZILETH': 50, 'HSRETH': 0.01,
                'VENETH': 2, 'WPRETH': 17, 'SNMETH': 5, 'QSPETH': 5, 'ENJETH': 10, 'ETCETH': 0.01,
                'NULSETH': 1, 'MANAETH': 15, 'BCDETH': 0.005, 'REQETH': 10, 'MODETH': 0.5, 'NEOETH': 0,
                'SNMETH': 5, 'IOSTETH': 50, 'LENDETH': 20, 'SUBETH': 2, 'AIONETH': 0.5, 'NEBLETH': 0.1,
                'ELFETH': 2, 'KNCETH': 0.5, 'INSETH': 0.5, 'AGIETH': 2, 'IOSTETH': 50, 'SNTETH': 20, 'BRDETH': 3, 
                'INSETH': 0.5, 'ONTETH': 0.1, 'DASHETH': 0.002, 'QKCETH': 10, 'ENJETH': 10,
                'IOTXETH': 30, 'RDNETH': 0.5, 'LTCETH': 0.001, 'QLCETH': 1,
                'AMBETH': 3, 'POWRETH': 1, 'RDNETH':0.5, 'DENTETH': 50, 'KEYETH': 50, 'QTUMETH': 0.1,
                'EOSETH': 0.5, 'KNCETH': 0.5, 'WANETH': 0.7, 'XLMETH': 9999999999,
                'SUBETH': 2, 'BTGETH': 0.01, 'CVCETH': 3, 'REQETH': 10, 'ARNETH': 1.8, 
                'GVTETH': 0.1, 'MTHETH': 10, 'AGIETH': 2, 'BCPTETH': 5, 'BRDETH': 3, 'EOSETH': 0.5, 
                'SNTETH': 20, 'WTCETH': 0.1, 'NANOETH': 0.5, 'DOCKETH': 20, 'VETETH': 9999999999}
coinFeesDictBTC =  {'RPXBTC': 1, 'ARNBTC': 1.8, 'OMGBTC': 0.1, 'GASBTC': 0, 'MTHBTC': 10, 'GVTBTC': 0.1,
                'PPTBTC': 0.1, 'CVCBTC': 3, 'LOOMBTC': 10, 'ZILBTC': 50, 'HSRBTC': 0.01,
                'VENBTC': 2, 'WPRBTC': 17, 'SNMBTC': 5, 'QSPBTC': 5, 'ENJBTC': 10, 'ETCBTC': 0.01,
                'NULSBTC': 1, 'MANABTC': 15, 'BCDBTC': 0.005, 'REQBTC': 10, 'MODBTC': 0.5, 'NEOBTC': 0,
                'SNMBTC': 5, 'IOSTBTC': 50, 'LENDBTC': 20, 'SUBBTC': 2, 'AIONBTC': 0.5, 'NEBLBTC': 0.1,
                'ELFBTC': 2, 'KNCBTC': 0.5, 'INSBTC': 0.5, 'AGIBTC': 2, 'IOSTBTC': 50, 'SNTBTC': 20, 'BRDBTC': 3, 
                'INSBTC': 0.5, 'ONTBTC': 0.1, 'DASHBTC': 0.002, 'QKCBTC': 10, 'ENJBTC': 10,
                'IOTXBTC': 30, 'RDNBTC': 0.5, 'LTCBTC': 0.001, 'QLCBTC': 1,
                'AMBBTC': 3, 'POWRBTC': 1, 'RDNBTC':0.5, 'DENTBTC': 50, 'KEYBTC': 50, 'QTUMBTC': 0.1,
                'EOSBTC': 0.5, 'KNCBTC': 0.5, 'WANBTC': 0.7, 'XLMBTC': 9999999999,
                'SUBBTC': 2, 'BTGBTC': 0.01, 'CVCBTC': 3, 'REQBTC': 10, 'ARNBTC': 1.8, 
                'GVTBTC': 0.1, 'MTHBTC': 10, 'AGIBTC': 2, 'BCPTBTC': 5, 'BRDBTC': 3, 'EOSBTC': 0.5, 
                'SNTBTC': 20, 'WTCBTC': 0.1, 'NANOBTC': 0.5, 'DOCKBTC': 20, 'VETBTC': 9999999999, 'ETHBTC': 999999999,
                'POLYBTC': 3}
coinfeesUSDT = {'NEOUSDT': 0, 'LTCUSDT': 0.001, 'EOSUSDT': 0.5}


# In[ ]:


differenceDictlol = {}

for price in prices:
    bsymbol = price['symbol']
    bprice = price['price']
    if bsymbol in kucoinDict and coinFeesDict:
        diff = float(bprice) - kucoinDict[bsymbol] # find the biggest diff. 
        if bsymbol[-3:] == 'ETH':
            differenceDictlol[bsymbol] = diff

print(differenceDictlol['ENJETH'])
# for coins in differenceDict:
#     if 'USDT' in coins:
#         print(coins)
# for price in prices:
#     bsymbol = price['symbol']
#     bprice = price['price']
#     if bsymbol in kucoinDict:
#         diff = kucoinDict[bsymbol] - float(bprice)  # find the biggest diff.
#         diffPercent = diff - float(bprice)
            
#         if bsymbol[-3:] == 'ETH': #only check things trading in ETH
#             diffPercent = abs(diffPercent)  # turn everything positive 
#             differenceDict[bsymbol] = diffPercent


# In[ ]:


# print(sorted(differenceDictlol.items(), key=lambda x: x[1])) #sort it
print(differenceDictlol)


# In[15]:


# just a test to find the diff between two coins and the % diff for both sites.  WIll implement into watch() function
# symbolTestKucoin = kucoinDict['IOTXETH']
# symbolTestBinance = float(binancePriceDict['IOTXETH'])
# print("KUCOIN: ", symbolTestKucoin)
# print("BINANCE: ", symbolTestBinance)
# diffIOTXETH = differenceDict['IOTXETH']
# print("DIFF IS: ", diffIOTXETH)
# percentageCompareKucoin = diffIOTXETH / symbolTestKucoin
# percentageCompareBinance = diffIOTXETH / symbolTestBinance
# print("KUCOIN %: ", percentageCompareKucoin)
# print("BINANCE %: ", percentageCompareBinance)


# In[16]:


# turns all the prices from binance into a dict
allBinanceCoins = {}

for price in prices:
    bsymbol = price['symbol']
    bprice = price['price']
    if bsymbol in kucoinDict:
        allBinanceCoins[bsymbol] = bprice
print(allBinanceCoins)


# In[24]:


randomCoinBalance = client.get_coin_balance('ENJ')
                          
                          
                          
                          
print(randomCoinBalance)


# In[33]:


# gets the bid and the asks to decide (major step) if the coin is good or not

# twentyHour = bclient.get_ticker()
# testTicker = twentyHour[1]
differenceList = []

for coins in differenceDictlol:
    differenceList.append(coins)
    
    
differenceListDash = []
# print(differenceList)

for coins in differenceList:
    
    if len(coins) == 7:
        newCoinName = coins[:4] + '-' + coins[4:]
    
    if len(coins) == 6:
        newCoinName = coins[:3] + '-' + coins[3:]
    
    differenceListDash.append(newCoinName)
    


# print(differenceListDash)

amountOfCoinsToBuy = {}
differenceDictFinal = {}
# sellorders = client.get_sell_orders('ENJ-ETH')
print('______________________________')
# print(sellorders)
# print('_________________________')
# print(amountOfCoinsToBuy)
amountOfCoins = 0
priceOfOrder = 0
differenceDictPre = {}
differenceDictVol = {}

coinToBuy = 0.5 / kucoinDict['ENJETH']
# print(differenceListDash)
for i in differenceListDash:
    sellorders = client.get_sell_orders('{}'.format(i), limit=10)
    amountOfCoins = 0
    priceOfOrder = 0
    
    for coins in sellorders:
        priceETH = float(coins[2])
        amountOfTheCoin = float(coins[1])
        priceOfCoinAsk = float(coins[0])
        
        priceOfOrderBeforeBid = priceOfOrder + priceETH
    
        if priceOfOrderBeforeBid >= accountBalanceKucoin:
            ETHLeft = (accountBalanceKucoin - priceOfOrder)
            
            
            amountToBuy = ETHLeft / priceOfCoinAsk
            
            finalOrder = (amountToBuy * priceOfCoinAsk) + priceOfOrder 
            
            
            amountOfCoinsFinal = amountToBuy + amountOfCoins
                          
                          
        
            symbolNoDash = i.replace('-', '')
            differenceDictPre[symbolNoDash] = finalOrder
            differenceDictVol[symbolNoDash] = amountOfCoinsFinal
            
            
            
        else:
            
            priceOfOrder += priceETH 
            
            amountOfCoins += amountOfTheCoin
        
        continue

# print(differenceDictPre)
differenceDictSemi = {}

amountOfCoinsBinance = 0
priceOrderBinance = 0
# FOR BINANCE 
for coins, vol in differenceDictVol.items():
    amountOfCoinsBinance = 0
    priceOrderBinance = 0
    depth = bclient.get_order_book(symbol='{}'.format(coins), limit=10)
    bbuy = depth['bids']


    for i in bbuy:
        
        amountCoinBinance = float(i[1])
        priceCoinBinance = float(i[0])
        priceETHBinance = priceCoinBinance * amountCoinBinance
        
        amountOfCoinsBefore = amountOfCoinsBinance + amountCoinBinance
        
        if amountOfCoinsBefore >= vol:
            
            amountOfCoinsLeft = vol - amountOfCoinsBinance
            
            priceOfSelectCoins = amountOfCoinsLeft * priceCoinBinance
            
            finalPriceBinance = priceOrderBinance + priceOfSelectCoins
            
            # print(finalPriceBinance)
            
            differenceInPrices = finalPriceBinance - differenceDictPre[coins]
            differenceDictSemi[coins] = differenceInPrices
            
            break
        
        else:
            
            amountOfCoinsBinance += amountCoinBinance
            priceOrderBinance += priceETHBinance
        
    
# depth = bclient.get_order_book(symbol='ENJETH', limit=5)    
# bbuy = depth['bids'][0][0]
# bsell = depth['asks'][0][0]

differenceDict = {}

for coins, prices in differenceDictSemi.items():
    if coins in coinFeesDict:
        differenceDict[coins] = prices

print(differenceDict['ENJETH'])


# In[ ]:



    
    


# In[18]:


print(differenceDict['ENJETH'])


# In[19]:


difference = differenceDict['ENJETH']
print(difference)


# In[20]:


# find % diff for all binance coins
# change this to work with account balance to calc how much money i would make
# percentDiffDictBinance = {}
# finalCoinsToTradePercentage = {}
# finalCoinsToTradeProfit = {}

# print(differenceDict['PPTETH'])
# for coins in differenceDict:
#     coinPriceBinance = float(allBinanceCoins[coins])
#     coinPriceKucoin = float(kucoinDict[coins])
#     coinPriceAverage = (coinPriceBinance + coinPriceKucoin) / 2
#     if coins in coinFeesDict:
        # diffPercentage = float(differenceDict[coins]) / float(coinPriceAverage)
#         amountOfCoinsToBuy = float(accountBalanceKucoin) / float(coinPriceKucoin)
#         profitOfCoin = (float(amountOfCoinsToBuy) * float(differenceDict[coins])) 
        # finalCoinsToTradePercentage[coins] = diffPercentage
#         finalCoinsToTradeProfit[coins] = profitOfCoin

# print(finalCoinsToTradeProfit)
# print('____________________________________________________')   

    



# In[31]:


# this cell is used to create the system which calculates the fees for every coin 
# basically, just index the chosen coin or all the similar coins to get the withdrawl fee
# after you have how many coins it takes, simply turn that into a percentage of the total coins that you have
# also change to work with a total account balance
tickerKucoinSpecial = client.get_tick('DENT-BTC')
# print(tickerKucoinSpecial)
theFinalList = {}




# ethDict = []
# btcDict = []
# usdtDict = []

# kucoinWithdrawlFee = 0

# # for coins in finalCoinsToTrade:
# #     newName = coins.replace('ETH', '')
# #     testDict[newName] = finalCoinsToTrade[coins]
# # for coin in finalCoinsToTrade:
# #     if 'BTC' in coin:
# #         newBitcoinName = coin.replace('BTC', '')
# #         if newBitcoinName not in testDict:
# #             testDict[newBitcoinName] = finalCoinsToTrade[coin] 
# # print(testDict)

# # trying: make all things just newName, then add function to for loop, then for loop continues on
# def makingNamesSimple(name):

#     if 'ETH' in name:
#         newName = coins.replace('ETH', '')
# #         ethDict.append(newName)
        
#     elif 'USDT' in name:
#         newName = coins.replace('USDT', '')
# #         usdtDict.append(newUSDTName)
        
#     else:
#         newName = coins.replace('BTC', '')
# #         btcDict.append(newBTCName)


# #     for coin in ethDict:
# #         if coin not in usdtDict:
# #             usdtDict.append(coin)
        
# #     for coin in usdtDict:
# #         if coin not in btcDict:
# #             btcDict.append(coin)

# #     listOfCoinNames = btcDict.remove('USDT')

# for coin in finalCoinsToTradePercentage:
#     name = coin
    
    
#     coinPriceBinance = float(allBinanceCoins[coin])
#     coinPriceKucoin = float(kucoinDict[coin])
#     coinPriceAverage = (coinPriceBinance + coinPriceKucoin) / 2 # extra step, when in function use old variable
#     makingNamesSimple(name) # just remake function to change just coin
#     amount = coinPriceAverage * float(coinFeesDict[newName])
#     totalPercentage = amount / coinPriceAverage
#     newFinalPercentage = finalCoinsToTradePercentage[coin] - totalPercentage
#     if coin not in theFinalList:
#             theFinalList[coin] = newFinalPercentage

# print(theFinalList)
    
# just trying to replace both BTC and ETH then i have to go back and get it to include BTC coins

    
finalCoinsAfterBaseFee = {}

for coins, prices in differenceDict.items():
#     newProfit = prices * (1 - baseFee)
    
    coinPriceKucoin = float(kucoinDict[coins])
    amountOfCoinsToBuy = differenceDictVol[coins]
    # nameWithoutBigCoin = coins.replace('ETH', '').replace('BTC', '').replace('USDT', '')
    # print(nameWithoutBigCoin)
    # if '' and 'ETH' and 'USDT' and 'BTC' not in nameWithoutBigCoin:
    withdrawlFee = coinFeesDict[coins]
    
    
    priceToWithdrawl = withdrawlFee * coinPriceKucoin
    
    
    finalProfit = prices - priceToWithdrawl
    
    finalCoinsAfterBaseFee[coins] = finalProfit


# In[32]:


# print(sorted(finalCoinsAfterBaseFee.items(), key=lambda x: x[1]))
print(finalCoinsAfterBaseFee['ENJETH'])


# In[ ]:


# test, delete once done

# orders prints out price, then amount of coin, then volume compared to the larger coin, ex. ETH
orders = client.get_buy_orders('WAN-ETH', limit=5)

# same for sell orders
sellorders = client.get_sell_orders('DASH-ETH', limit=5)

# just amount then volume of whole book, bids and asks, in ascending order
depth = bclient.get_order_book(symbol='ENJETH', limit=5)

# gets the lowest ask
bsell = depth['asks'][0][0]

# gets the lowest bid
bbuy = depth['bids'][0][0]

# just looks at the lowest sell order by price of coin, ascending order
ksell = sellorders[0][0]

# looks at the highest buy by amount
kbuy = orders[0][0]

# this just makes sure that our buy order goes to top of books so it is filled instantly
# consider limit orders b/c on one website they are free
kbuyAdd = kbuy + 0.01




# In[22]:


# order all difference coins by how much profit they make. best coin is named bestCoin, use that in all further operations for the final part

coinsAndStuff = sorted(finalCoinsAfterBaseFee, key=finalCoinsAfterBaseFee.__getitem__, reverse=True)
bestCoinFormer = coinsAndStuff[0]
bestCoin = {}
bestCoin[bestCoinFormer] = finalCoinsAfterBaseFee[bestCoinFormer] / accountBalanceKucoin
bestCoinETH = []

for coins in bestCoin:
    
    if len(coins) == 7:
        newCoinNameETH = coins[:4] + '-' + coins[4:]
    
    if len(coins) == 6:
        newCoinNameETH = coins[:3] + '-' + coins[3:]
    
    bestCoinETH.append(newCoinName)

# print('____________-----')
# print(bestCoin)


# In[23]:


# to sell on BINANCE

orderBinance = bclient.order_market_sell(symbol='{}'.format(bestCoinFormer), quantity=differenceDictVol[bestCoinFormer])

# check order status

orderStatus = bclient.get_order(symbol='{}'.format(bestCoinFormer), orderId='orderId')


# In[55]:


# input = input('Press q to quit: ')
i = 0
while True:
    
#     if input == 'q':
#         break
    #time.sleep(60)
    # i += 1
    try:
        # print('IT: {}'.format(i))
        watch()
    
    except:
        time.sleep(10)
        continue


# In[15]:


# this is a duplicated test cell for testing the above section using neo
import time
import math
from binance.enums import *

# sell 

# def makeSellTradeBinance():
#     orderBinance = bclient.order_market_sell(symbol='{}'.format(bestCoinFormer), quantity=differenceDictVol[bestCoinFormer])
            
            
# def maketrade(oid):
#     orders = client.get_active_orders('{}'.format(bestCoinETH))
        
#     if orders['BUY']:
#         print("ORDER NOT FILLED")
#     else:
#         print("ORDER FILLED")
#         balanceTradedCoin = client.get_coin_balance('{}'.format(bestCoinFormer[:3]))
#         address = bclient.get_deposit_address(asset='{}'.format(bestCoinFormer[:3]))
#         client.create_withdrawal('{}'.format(bestCoinFormer[:3]), float(balanceTradedCoin['balance']),
#                                     str(address['address']))
#         makeSellTradeBinance()


def theCoinBuyerETH():
    actualCoinToBuy = 0.0000057 # client.get_coin_balance('ETH')

    
    
    # this gets the prices
    coins = client.get_trading_symbols() # get all kucoin prices
    prices = bclient.get_all_tickers() # get all binance prices


    # this makes a dict of all kucoin coins
    kucoinDict = {} # create a dictionary

    for coin in coins:
        # print(coin['lastDealPrice'])
        coinsymbol = coin['symbol']
        coinsymbol = coinsymbol.replace('-', '') # we need to remove dash to ocmpare to binance
        lastDeal = coin['buy']
        
        kucoinDict[coinsymbol] = lastDeal # add to the dict to compare binance and kucoin

    
    # this makes a dict of all binance coins




    # makes a dict of all things that are the same

    differenceDictlol = {}

    for price in prices:
        bsymbol = price['symbol']
        bprice = price['price']
        if bsymbol in kucoinDict:
            if bsymbol in coinFeesDict:
                diff = float(bprice) - kucoinDict[bsymbol] # find the biggest diff. 
                if bsymbol[-3:] == 'ETH':
                    differenceDictlol[bsymbol] = diff


    # this is a multistage part.  this makes dict readable for both sites, get bids and asks, and determines the price difference
    # (eth) between bid and asks on both sites.  this only buy on kucoin sell on binance right now


    # gets the bid and the asks to decide (major step) if the coin is good or not

    # twentyHour = bclient.get_ticker()
    # testTicker = twentyHour[1]
    differenceList = []

    for coins in differenceDictlol:
        differenceList.append(coins)
    
    
    differenceListDash = []
        # print(differenceList)
    
    for coins in differenceList:
    
        if len(coins) == 7:
            newCoinName = coins[:4] + '-' + coins[4:]
    
        if len(coins) == 6:
            newCoinName = coins[:3] + '-' + coins[3:]
    
        differenceListDash.append(newCoinName)
    


    # print(differenceListDash)

    amountOfCoinsToBuy = {}
    differenceDictFinal = {}
    # sellorders = client.get_sell_orders('ENJ-ETH')
    print('______________________________')
    # print(sellorders)
    # print('_________________________')
    # print(amountOfCoinsToBuy)
    amountOfCoins = 0
    priceOfOrder = 0
    differenceDictPre = {}
    differenceDictVol = {}
    differenceDictVolActual = {}
    buyPrice = {}
    
    # coinToBuy = 0.5 / kucoinDict['ENJETH']
    # print(differenceListDash)
    for i in differenceListDash:
        sellorders = client.get_sell_orders('{}'.format(i), limit=10)

        amountOfCoins = 0
        priceOfOrder = 0
        
        for coins in sellorders:
            
            priceETH = float(coins[2])
            amountOfTheCoin = float(coins[1])
            priceOfCoinAsk = float(coins[0])
            
        
            priceOfOrderBeforeBid = priceOfOrder + priceETH
            
            if priceOfOrderBeforeBid >= accountBalanceKucoin:
                ETHLeft = (accountBalanceKucoin - priceOfOrder)
                
                priceOfCoinBuy = priceOfCoinAsk
                amountToBuy = ETHLeft / priceOfCoinAsk
            
                finalOrder = (amountToBuy * priceOfCoinAsk) + priceOfOrder 
            
                # print(finalOrder)
                amountOfCoinsFinal = amountToBuy + amountOfCoins
                      
                          
                
                symbolNoDash = i.replace('-', '')
                differenceDictPre[symbolNoDash] = finalOrder
                
                buyPrice[symbolNoDash] = priceOfCoinAsk
            
                differenceDictVol[symbolNoDash] = amountOfCoinsFinal
                
                differenceDictVolActual[symbolNoDash] = amountOfCoinsFinal + (0.002 * amountOfCoinsFinal)
                
                break
                
            else:
            
                priceOfOrder += priceETH 
            
                amountOfCoins += amountOfTheCoin
        
                continue
    
    # print(differenceDictPre)
    differenceDict = {}
    # print(differenceDictVol)
    amountOfCoinsBinance = 0
    priceOrderBinance = 0
    # FOR BINANCE 
    for coins, vol in differenceDictVol.items():
        amountOfCoinsBinance = 0
        priceOrderBinance = 0
        depth = bclient.get_order_book(symbol='{}'.format(coins), limit=10)

        bbuy = depth['bids']


        for i in bbuy:
        
            amountCoinBinance = float(i[1])
            priceCoinBinance = float(i[0])
            priceETHBinance = priceCoinBinance * amountCoinBinance
        
            amountOfCoinsBefore = amountOfCoinsBinance + amountCoinBinance
            
            if amountOfCoinsBefore >= vol:
                
                amountOfCoinsLeft = vol - amountOfCoinsBinance
            
                priceOfSelectCoins = amountOfCoinsLeft * priceCoinBinance
            
                finalPriceBinance = priceOrderBinance + priceOfSelectCoins
                # print(finalPriceBinance)
            
                # print(finalPriceBinance)
            
                differenceInPrices = finalPriceBinance - differenceDictPre[coins]
                differenceDict[coins] = differenceInPrices
            
                break
        
            else:
            
                amountOfCoinsBinance += amountCoinBinance
                priceOrderBinance += priceETHBinance
        
    
    # depth = bclient.get_order_book(symbol='ENJETH', limit=5)    
    # bbuy = depth['bids'][0][0]
    # bsell = depth['asks'][0][0]

    # print(differenceDict)


    
    # this calculates the remaining tax 
    finalCoinsAfterBaseFee = {}

    for coins, prices in differenceDict.items():
    #     newProfit = prices * (1 - baseFee)
        
        coinPriceKucoin = float(kucoinDict[coins])
        amountOfCoinsToBuy = differenceDictVol[coins]
        # nameWithoutBigCoin = coins.replace('ETH', '').replace('BTC', '').replace('USDT', '')
        # print(nameWithoutBigCoin)
        # if '' and 'ETH' and 'USDT' and 'BTC' not in nameWithoutBigCoin:
        withdrawlFee = coinFeesDict[coins]
    
    
        priceToWithdrawl = withdrawlFee * coinPriceKucoin
    
    
        finalProfit = prices - priceToWithdrawl
    
        finalCoinsAfterBaseFee[coins] = finalProfit


    
    print(buyPrice)
    # order all difference coins by how much profit they make. best coin is named bestCoin, use that in all further operations for the final part
    bestCoin = {}
    
    
    coinsAndStuff = sorted(finalCoinsAfterBaseFee, key=finalCoinsAfterBaseFee.__getitem__, reverse=True)
#     bestCoinFormer = coinsAndStuff[0]
#     bestCoinFirstThree = []  # add so that if it is a four it does that too
    
#     bestCoin[bestCoinFormer] = finalCoinsAfterBaseFee[bestCoinFormer] / accountBalanceKucoin
#     bestCoinPercentage = bestCoin[bestCoinFormer] / accountBalanceKucoin
#     bestCoinETH = []
    bestCoinFormer = str(coinsAndStuff[0])
    bestCoinFirstThree = []  # add so that if it is a four it does that too
    
    bestCoin[bestCoinFormer] = finalCoinsAfterBaseFee[bestCoinFormer] / accountBalanceKucoin
    bestCoinPercentage = bestCoin[bestCoinFormer]
    bestCoinETH = []
        
    for coins in bestCoin:
    
            if len(coins) == 7:
                newCoinNameETH = coins[:4] + '-' + coins[4:]
    
            if len(coins) == 6:
                newCoinNameETH = coins[:3] + '-' + coins[3:]
    
            bestCoinETH.append(newCoinNameETH)


        
    for coins in bestCoin:
    
            if len(coins) == 7:
                newCoinNameFirstThree = coins[:4]
    
            if len(coins) == 6:
                newCoinNameFirstThree = coins[:3]
    
            bestCoinFirstThree.append(newCoinNameFirstThree)
    bestCoinFirstThree = bestCoinFirstThree[0]
    bestCoinETH = bestCoinETH[0]
    print(str(bestCoinETH))
    print(bestCoin)
    print(bestCoinFirstThree)
    # print(bestCoinPercentage)


    #     getKucoinPrices()
    #     getBinancePrices()
    #     buyAndAsk()
    #     tax()
    #     bestCoinFuntion()
    
    
#         if bestCoinPercentage > 0.03:
#             print("BUY KUCOIN SELL BINANCE")
        
        
#             try:
#                 transaction = client.create_buy_order('{}'.format(bestCoinETH), 'BEST_PRICE', differenceDictVol[bestCoinFormer])
#                 print(transaction)
#                 maketrade(transaction[orderOid])
#             except:
#                 client.cancel_all_orders()
#                 print("PROBLEM WITH TRADE")
        
#         else:
#             time.sleep(120)
#             continue
    
    balanceBinanceBeforelol= bclient.get_asset_balance(asset=str(bestCoinFirstThree))['free']   
    balanceBinanceBefore = float(balanceBinanceBeforelol)

    print(5)
    vol = float(differenceDictVolActual[bestCoinFormer])
    
    buyPriceFinal = float(buyPrice[bestCoinFormer])
    print('----------------------')
    print(buyPriceFinal)
    print('-----------------------')
    print(vol)



# def maketrade(oid):
#     print('b')
#     for x in range(0,50):
#         time.sleep(1)
#         print('c')
#         orders = client.get_active_orders(str(bestCoinETH))
#         print(orders)
#         print('d')
#         # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
#         print('e')
#         if orders['BUY']:
#             print('order not filled')
#         else:
#             print('order filled')
#             for y in range(0,10)
#             randomCoinBalanceBefore = client.get_coin_balance(str(bestCoinFirstThree))
#             randomCoinBalance = float(randomCoinBalanceBefore['balance']) - 50
#             print('l')
#             address = bclient.get_deposit_address(asset=str(bestCoinFirstThree))
#             print('got to withdrawl')
#             withdrawal = client.create_withdrawal(str(bestCoinFirstThree), float(randomCoinBalance),
#                                  str(address['address']))
#             print('made with')
#             makeSellTradeBinance(withdrawal)
#         print(x)
#         if x == 8:
#             client.cancel_all_orders()
#         time.sleep(1)
#         print('WITHDRAWING')
    finalCommand = 1        
# def makeSellTradeBinance(y):
    
                

    
                
#             except:
#                 balanceRandoBinance = float(str(balanceRandoBinance)[:-1])
#                 print(balanceRandoBinance)
#                 continue
#             else:
#                 break
#             break
#         break
#     break
        
        
    #hile True:
       




    rdnVarFinal = 1

    if bestCoinPercentage > 0.05:
        print("BUY KUCOIN SELL BINANCE")
        print(bestCoinETH)
        print(buyPriceFinal)
        print(vol)
        # make the fancy loop to conitnually take off digits until order goes through
        print('buying')
        while True:
            try: 
               
                print(vol)
                transaction = client.create_buy_order(str(bestCoinETH), str(buyPriceFinal), str(vol))
                # orders = client.get_active_orders('{}'.format(bestCoinETH))
            
                if transaction['orderOid']:
                    print('next part')
                    rdnVarFinal = 3
                    print(transaction)  
                    orders = client.get_active_orders(str(bestCoinETH))
                    print(orders)
                    print('d')
                    # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
                    print('e')
                    time.sleep(1)
                    if orders['BUY']:
                        print('order not filled')
                        client.cancel_all_orders()
                    else:
                        print('order filled')
                        time.sleep(1)
                        randomCoinBalanceBefore = client.get_coin_balance(str(bestCoinFirstThree))
                        randomCoinBalance = float(randomCoinBalanceBefore['balance']) - 50
                        print('l')
                        address = bclient.get_deposit_address(asset=str(bestCoinFirstThree))
                        print('got to withdrawl')
                        time.sleep(0.5)
                        withdrawal = client.create_withdrawal(str(bestCoinFirstThree), float(randomCoinBalance),
                                     str(address['address']))
                        print('made with')
                    
                        for x in range(0,10000000000000000):
                            balanceRandoBinance = float(bclient.get_asset_balance(asset=str(bestCoinFirstThree))['free'])
                            # balanceRando = 1.234356788
                            # newBalance = float(balanceBinanceBefore)
                            print(balanceRandoBinance)
                            if float(balanceRandoBinance)  <= float(balanceBinanceBefore):
                                print('waitingggggg')
                                print(x)
                
    
                            else:
                                print('onto sell trade')
                                while True:
                                    # balanceRandoBinance = float(bclient.get_asset_balance(asset=str(bestCoinFirstThree))['free'])
                                    try:
               

                                        print(balanceRandoBinance)
                                        transact = bclient.order_market_sell(symbol=str(bestCoinFormer), quantity=balanceRandoBinance)
                                        time.sleep(0.5)
            
            
                                        if transact['status'] == 'FILLED':
                                            print('yay done boss')
                                            balanceETHBinance = bclient.get_asset_balance(asset='ETH')['free']
                                            print(balanceETHBinance)
                                            print('FU FINALY')
                                            finalCommand = 5
                                            break
                                    except:
                                        balanceRandoBinance = float(str(balanceRandoBinance)[:-1])
                                        print(balanceRandoBinance)
                                        continue
                    
                   
                            if finalCommand == 5:
                                break
        
                            if x == 10000:
                                client.cancel_all_orders()
                            time.sleep(1)
                
                # maketrade(transaction['orderOid'])
                    
                    
            
            
        
            except:
                vol = float(str(vol)[:-1])
            
            
               
                print('SOMETHING WENT WRONG')
            
        
            if rdnVarFinal == 3:
                print('FINISHING UP')
                break
         
    
    
        
    
       


# In[8]:



while True:
    theCoinBuyerETH()
    time.sleep(60)


# In[ ]:


# BTC REAL TING
import time
import math
from binance.enums import *

# sell 

# def makeSellTradeBinance():
#     orderBinance = bclient.order_market_sell(symbol='{}'.format(bestCoinFormer), quantity=differenceDictVol[bestCoinFormer])
            
            
# def maketrade(oid):
#     orders = client.get_active_orders('{}'.format(bestCoinETH))
        
#     if orders['BUY']:
#         print("ORDER NOT FILLED")
#     else:
#         print("ORDER FILLED")
#         balanceTradedCoin = client.get_coin_balance('{}'.format(bestCoinFormer[:3]))
#         address = bclient.get_deposit_address(asset='{}'.format(bestCoinFormer[:3]))
#         client.create_withdrawal('{}'.format(bestCoinFormer[:3]), float(balanceTradedCoin['balance']),
#                                     str(address['address']))
#         makeSellTradeBinance()


def theCoinBuyerBTC():
    # actualCoinToBuyBTC = 0.0000057 # client.get_coin_balance('ETH')

    
    
    # this gets the prices
    
    coinsBTC = client.get_trading_symbols() # get all kucoin prices
    pricesBTC = bclient.get_all_tickers() # get all binance prices

    # this makes a dict of all kucoin coins
    kucoinDictBTC = {} # create a dictionary

    for coinBTC in coinsBTC:
        coinsymbolBTC = coinBTC['symbol']
        coinsymbolBTC = coinsymbolBTC.replace('-', '') # we need to remove dash to ocmpare to binance
        lastDealBTC = coinBTC['buy']

        kucoinDictBTC[coinsymbolBTC] = lastDealBTC # add to the dict to compare binance and kucoin

    
    # this makes a dict of all binance coins




    # makes a dict of all things that are the same

    differenceDictlolBTC = {}

    for priceBTC in pricesBTC:
        bsymbolBTC = priceBTC['symbol']
        bpriceBTC = priceBTC['price']
        if bsymbolBTC in kucoinDictBTC:
            if bsymbolBTC in coinFeesDictBTC:
                diffBTC = float(bpriceBTC) - kucoinDictBTC[bsymbolBTC] # find the biggest diff. 
                if bsymbolBTC[-3:] == 'BTC':
                    differenceDictlolBTC[bsymbolBTC] = diffBTC


    # this is a multistage part.  this makes dict readable for both sites, get bids and asks, and determines the price difference
    # (eth) between bid and asks on both sites.  this only buy on kucoin sell on binance right now


    # gets the bid and the asks to decide (major step) if the coin is good or not

    # twentyHour = bclient.get_ticker()
    # testTicker = twentyHour[1]
    differenceListBTC = []

    for coinsBTC in differenceDictlolBTC:
        differenceListBTC.append(coinsBTC)
    
    
    differenceListDashBTC = []
        # print(differenceList)
    
    for coinsBTC in differenceListBTC:
    
        if len(coinsBTC) == 7:

            newCoinNameBTC = coinsBTC[:4] + '-' + coinsBTC[4:]
    
        if len(coinsBTC) == 6:
            newCoinNameBTC = coinsBTC[:3] + '-' + coinsBTC[3:]
    
        differenceListDashBTC.append(newCoinNameBTC)
    


    # print(differenceListDash)

    amountOfCoinsToBuyBTC = {}
    differenceDictFinalBTC = {}
    # sellorders = client.get_sell_orders('ENJ-ETH')
    print('______________________________')
    # print(sellorders)
    # print('_________________________')
    # print(amountOfCoinsToBuy)
    amountOfCoinsBTC = 0
    priceOfOrderBTC = 0
    differenceDictPreBTC = {}
    differenceDictVolBTC = {}
    differenceDictVolActualBTC = {}
    buyPriceBTC = {}
    
    # coinToBuy = 0.5 / kucoinDict['ENJETH']
    # print(differenceListDash)
    for iBTC in differenceListDashBTC:
        sellordersBTC = client.get_sell_orders('{}'.format(iBTC), limit=10)

        amountOfCoinsBTC = 0
        priceOfOrderBTC = 0
        
        for coinsBTC in sellordersBTC:
            

            priceBTC = float(coinsBTC[2])
            amountOfTheCoinBTC = float(coinsBTC[1])
            priceOfCoinAskBTC = float(coinsBTC[0])
            
        
            priceOfOrderBeforeBidBTC = priceOfOrderBTC + priceBTC
            
            if priceOfOrderBeforeBidBTC >= accountBalanceKucoinBTC:
                BTCLeft = (accountBalanceKucoinBTC - priceOfOrderBTC)
                
                priceOfCoinBuyBTC = priceOfCoinAskBTC
                amountToBuyBTC = BTCLeft / priceOfCoinAskBTC
            
                finalOrderBTC = (amountToBuyBTC * priceOfCoinAskBTC) + priceOfOrderBTC 
            
                # print(finalOrder)
                amountOfCoinsFinalBTC = amountToBuyBTC + amountOfCoinsBTC
                      
                          
                
                symbolNoDashBTC = iBTC.replace('-', '')
                differenceDictPreBTC[symbolNoDashBTC] = finalOrderBTC
                
                buyPriceBTC[symbolNoDashBTC] = priceOfCoinAskBTC
            
                differenceDictVolBTC[symbolNoDashBTC] = amountOfCoinsFinalBTC
                
                differenceDictVolActualBTC[symbolNoDashBTC] = amountOfCoinsFinalBTC + (0.002 * amountOfCoinsFinalBTC)
                
                break
                
            else:
            
                priceOfOrderBTC += priceBTC 
            
                amountOfCoinsBTC += amountOfTheCoinBTC
        
                continue
    
    # print(differenceDictPre)
    differenceDictBTC = {}

    amountOfCoinsBinanceBTC = 0
    priceOrderBinanceBTC = 0
    # FOR BINANCE 
    for coinsBTC, volBTC in differenceDictVolBTC.items():
        amountOfCoinsBinanceBTC = 0

        priceOrderBinanceBTC = 0
        depthBTC = bclient.get_order_book(symbol='{}'.format(coinsBTC), limit=10)

        bbuyBTC = depthBTC['bids']


        for iBTC in bbuyBTC:
        
            amountCoinBinanceBTC = float(iBTC[1])
            priceCoinBinanceBTC = float(iBTC[0])
            priceBTCBinance = priceCoinBinanceBTC * amountCoinBinanceBTC
        
            amountOfCoinsBeforeBTC = amountOfCoinsBinanceBTC + amountCoinBinanceBTC
            
            if amountOfCoinsBeforeBTC >= volBTC:
                
                amountOfCoinsLeftBTC = volBTC - amountOfCoinsBinanceBTC
            
                priceOfSelectCoinsBTC = amountOfCoinsLeftBTC * priceCoinBinanceBTC
            
                finalPriceBinanceBTC = priceOrderBinanceBTC + priceOfSelectCoinsBTC
                # print(finalPriceBinanceBTC)
            
                # print(finalPriceBinance)
            

                differenceInPricesBTC = finalPriceBinanceBTC - differenceDictPreBTC[coinsBTC]
                differenceDictBTC[coinsBTC] = differenceInPricesBTC
            
                break
        
            else:
            
                amountOfCoinsBinanceBTC += amountCoinBinanceBTC
                priceOrderBinanceBTC += priceBTCBinance
        
    
    # depth = bclient.get_order_book(symbol='ENJETH', limit=5)    
    # bbuy = depth['bids'][0][0]
    # bsell = depth['asks'][0][0]

    # print(differenceDictBTC)


    
    # this calculates the remaining tax 
    finalCoinsAfterBaseFeeBTC = {}

    for coinsBTC, pricesBTC in differenceDictBTC.items():
    #     newProfit = prices * (1 - baseFee)
        
        coinPriceKucoinBTC = float(kucoinDictBTC[coinsBTC])
        amountOfCoinsToBuyBTC = float(differenceDictVolBTC[coinsBTC])
        # nameWithoutBigCoin = coins.replace('ETH', '').replace('BTC', '').replace('USDT', '')
        # print(nameWithoutBigCoin)
        # if '' and 'ETH' and 'USDT' and 'BTC' not in nameWithoutBigCoin:
        withdrawlFeeBTC = coinFeesDictBTC[coinsBTC]
    
    
        priceToWithdrawlBTC = withdrawlFeeBTC * coinPriceKucoinBTC
    
    
        finalProfitBTC = pricesBTC - priceToWithdrawlBTC
    
        finalCoinsAfterBaseFeeBTC[coinsBTC] = finalProfitBTC

    print('--------------------------')
    # print(finalCoinsAfterBaseFeeBTC)    
    print(buyPriceBTC)
    # order all difference coins by how much profit they make. best coin is named bestCoin, use that in all further operations for the final part
    bestCoinBTC = {}
    
    
    coinsAndStuffBTC = sorted(finalCoinsAfterBaseFeeBTC, key=finalCoinsAfterBaseFeeBTC.__getitem__, reverse=True)
    print('COISN AND STUFF: ', coinsAndStuffBTC)

#     bestCoinFormer = coinsAndStuff[0]
#     bestCoinFirstThree = []  # add so that if it is a four it does that too
    
#     bestCoin[bestCoinFormer] = finalCoinsAfterBaseFee[bestCoinFormer] / accountBalanceKucoin
#     bestCoinPercentage = bestCoin[bestCoinFormer] / accountBalanceKucoin
#     bestCoinETH = []
    bestCoinFormerBTC = coinsAndStuffBTC[0]
    print('BEST COIN, ', bestCoinFormerBTC)
# bestCoinFirstThreeBTC = []  # add so that if it is a four it does that too
    
    bestCoinBTC[bestCoinFormerBTC] = finalCoinsAfterBaseFeeBTC[bestCoinFormerBTC] / accountBalanceKucoinBTC
    bestCoinPercentageBTC = bestCoinBTC[bestCoinFormerBTC]
    bestCoinBTCKucoin = []

        
    for coinsBTC in bestCoinBTC:
    
        if len(coinsBTC) == 7:
                newCoinNameBTC = coinsBTC[:4] + '-' + coinsBTC[4:]
    
        if len(coinsBTC) == 6:
                newCoinNameBTC = coinsBTC[:3] + '-' + coinsBTC[3:]
    
        bestCoinBTCKucoin.append(newCoinNameBTC)

    bestCoinBTCKucoin = str(bestCoinBTCKucoin[0])
    print('KUCOIN FORMAT: ', bestCoinBTCKucoin)        
    for coinsBTC in bestCoinBTC:
    
        if len(coinsBTC) == 7:

            newCoinNameFirstThreeBTC = coinsBTC[:4]
    
        if len(coinsBTC) == 6:
            newCoinNameFirstThreeBTC = coinsBTC[:3]
    
        bestCoinFirstThreeBTC = str(newCoinNameFirstThreeBTC)
    print('BBB: ', bestCoinFirstThreeBTC)
# bestCoinFirstThreeBTC = bestCoinFirstThreeBTC[0]
# bestCoinBTC = bestCoinBTC[0]
    print(bestCoinBTC)
#print(bestCoinBTC)
# print(bestCoinFirstThreeBTC)
# print(bestCoinPercentage)


    #     getKucoinPrices()
    #     getBinancePrices()
    #     buyAndAsk()
    #     tax()
    #     bestCoinFuntion()
    
    
#         if bestCoinPercentage > 0.03:
#             print("BUY KUCOIN SELL BINANCE")
        
        
#             try:
#                 transaction = client.create_buy_order('{}'.format(bestCoinETH), 'BEST_PRICE', differenceDictVol[bestCoinFormer])
#                 print(transaction)
#                 maketrade(transaction[orderOid])
#             except:
#                 client.cancel_all_orders()
#                 print("PROBLEM WITH TRADE")
        
#         else:
#             time.sleep(120)
#             continue
    
    balanceBinanceBeforelolBTC= bclient.get_asset_balance(asset=str(bestCoinFirstThreeBTC))['free']   
    balanceBinanceBeforeBTC = float(balanceBinanceBeforelolBTC)
    print(5)
    volBTC = float(differenceDictVolActualBTC[bestCoinFormerBTC])
    

    buyPriceFinalBTC = float(buyPriceBTC[bestCoinFormerBTC])

    print('----------------------')

    print(buyPriceFinalBTC)

    print('-----------------------')

    print(volBTC)



# def maketrade(oid):
#     print('b')
#     for x in range(0,50):
#         time.sleep(1)
#         print('c')
#         orders = client.get_active_orders(str(bestCoinETH))
#         print(orders)
#         print('d')
#         # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
#         print('e')
#         if orders['BUY']:
#             print('order not filled')
#         else:
#             print('order filled')
#             for y in range(0,10)
#             randomCoinBalanceBefore = client.get_coin_balance(str(bestCoinFirstThree))
#             randomCoinBalance = float(randomCoinBalanceBefore['balance']) - 50
#             print('l')
#             address = bclient.get_deposit_address(asset=str(bestCoinFirstThree))
#             print('got to withdrawl')
#             withdrawal = client.create_withdrawal(str(bestCoinFirstThree), float(randomCoinBalance),
#                                  str(address['address']))
#             print('made with')
#             makeSellTradeBinance(withdrawal)
#         print(x)
#         if x == 8:
#             client.cancel_all_orders()
#         time.sleep(1)
#         print('WITHDRAWING')

    finalCommandBTC = 1        
# def makeSellTradeBinance(y):
    
                

    
                
#             except:
#                 balanceRandoBinance = float(str(balanceRandoBinance)[:-1])
#                 print(balanceRandoBinance)
#                 continue
#             else:
#                 break
#             break
#         break
#     break
        
        
    #hile True:
       




    rdnVarFinalBTC = 1


    if bestCoinPercentageBTC > 0.05:

        print("BUY KUCOIN SELL BINANCE")
    
        print(bestCoinBTCKucoin)
    
        print(buyPriceFinalBTC)
    
        print(volBTC)
    
    # make the fancy loop to conitnually take off digits until order goes through
    
        print('buying')
    
        while True:
    
            try: 
               
                print(volBTC)
                print('dodododo')
                transactionBTC = client.create_buy_order(str(bestCoinBTCKucoin), str(buyPriceFinalBTC), str(volBTC))
                # orders = client.get_active_orders('{}'.format(bestCoinETH))
                print(transactionBTC)
                print('lalalala')
                if transactionBTC['orderOid']:
                    print('next part')
                    rdnVarFinalBTC = 3
                    print(transactionBTC)  
                    ordersBTC = client.get_active_orders(str(bestCoinBTCKucoin))
                    print(ordersBTC)
                    print('d')
                    # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
                    print('e')
                    time.sleep(1)

                    if ordersBTC['BUY']:
                        print('order not filled')
                        client.cancel_all_orders()
                    else:
                        print('order filled')
                        time.sleep(1)
                        randomCoinBalanceBeforeBTC = client.get_coin_balance(str(bestCoinFirstThreeBTC))
                        randomCoinBalanceBTC = float(randomCoinBalanceBeforeBTC['balance']) - 50
                        print('l')
                        addressBTC = bclient.get_deposit_address(asset=str(bestCoinFirstThreeBTC))
                        print('got to withdrawl')
                        time.sleep(0.5)
                        withdrawalBTC = client.create_withdrawal(str(bestCoinFirstThreeBTC), float(randomCoinBalanceBTC),
                                                                 str(addressBTC['address']))
                        print('made with')
                    
                        for xBTC in range(0,10000000000000000):
                            balanceRandoBinanceBTC = float(bclient.get_asset_balance(asset=str(bestCoinFirstThreeBTC))['free'])
                            # balanceRando = 1.234356788
                            # newBalance = float(balanceBinanceBefore)
                            print(balanceRandoBinanceBTC)
                            if float(balanceRandoBinanceBTC)  <= float(balanceBinanceBeforeBTC):
                                print('waitingggggg')
                                print(xBTC)
                
    
                            else:
                                print('onto sell trade')
                                while True:
                                    # balanceRandoBinance = float(bclient.get_asset_balance(asset=str(bestCoinFirstThree))['free'])
                                    try:
               

                                        print(balanceRandoBinanceBTC)
                                        transactBTC = bclient.order_market_sell(symbol=str(bestCoinFormerBTC), quantity=balanceRandoBinanceBTC)
                                        time.sleep(0.5)
            
            
                                        if transactBTC['status'] == 'FILLED':
                                            print('yay done boss')
                                            balanceBTCBinance = bclient.get_asset_balance(asset='BTC')['free']
                                            print(balanceBTCBinance)
                                            print('FU FINALY')
                                            finalCommandBTC = 5
                                            break
                                    except:
                                        balanceRandoBinanceBTC = float(str(balanceRandoBinanceBTC)[:-1])
                                        print(balanceRandoBinanceBTC)
                                        continue
                    
                   
                            if finalCommandBTC == 5:
                                break
        
                            if xBTC == 10000:
                                client.cancel_all_orders()
                            time.sleep(1)
                
                # maketrade(transaction['orderOid'])
                    
                    
            
            
        
            except:
                volBTC = float(str(volBTC)[:-1])
            
            
               
                print('SOMETHING WENT WRONG')
            
        
            if rdnVarFinalBTC == 3:
                print('FINISHING UP')
                break
    
    
        
    
       


# In[ ]:


while True:
    try:
        theCoinBuyerBTC()
        theCoinBuyerETH()
        time.sleep(30)
    except:
        continue 


# In[9]:


bestCoinBTCKucoin = 'DENT-BTC'
ordersBTC = client.get_active_orders(str(bestCoinBTCKucoin))
print(ordersBTC)


# In[8]:


# this is the balances for all starting pairs which are listed below

accountBalanceBinanceEthereum = 0.01 # (float(bclient.get_asset_balance(asset='ETH')['free']) / 2) 

accountBalanceBinanceBitcoin = 0.1# (float(bclient.get_asset_balance(asset='BTC')['free']) / 2) 
accountBalanceBinanceUSDT = 1000# (float(bclient.get_asset_balance(asset='USDT')['free']) / 2)  

accountBalanceBinanceDict = {'BTC': accountBalanceBinanceBitcoin, 'ETH': accountBalanceBinanceEthereum, 'USDT': accountBalanceBinanceUSDT}


print(accountBalanceBinanceDict)


# In[9]:


from binance.enums import *
order = bclient.create_test_order(
    symbol='TRIGBNB',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=0.51,
    price='0.014482')


# In[ ]:


prices = bclient.get_all_tickers() # get all binance prices



startingPairs = ['ETHBTC', 'BNBBTC', 'BNBETH', 'BTCUSDT', 'ETHUSDT', 'BNBUSDT']

# gets last 3/4 letters
minimumAmountDict = {'BNBBTC': 4, 'ETHBTC': 5, 'BNBETH': 4, 'BTCUSDT': 8, 'ETHUSDT': 7, 'BNBUSDT': 4}




x = 0
# calculates how much of the coin i can buy with my current reserves

amountOfMinorCoin = {}
amountOfMinorCoinBT = {}
amountOfCoinsBinanceTri = 0
priceOrderBinanceTri = 0
# FOR BINANCE 
for pairs in startingPairs:
    if len(pairs) == 6:
        lastLetters = pairs[-3:]
    
    if len(pairs) == 7:
        lastLetters = pairs[-4:]
    
        
    majorCoinBalance = float(accountBalanceBinanceDict[lastLetters])
    
    
    amountOfCoinsBinanceTri = 0
    
    

    priceOrderBinanceTri = 0
    depthBinanceTri = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

    bbuyTri = depthBinanceTri['bids']


    for ordersTri in bbuyTri:
        
        amountCoinBinanceTri = float(ordersTri[1])
        priceCoinBinanceTri = float(ordersTri[0])
        priceBinanceTri = priceCoinBinanceTri * amountCoinBinanceTri
        
        priceBeforeTri = priceOrderBinanceTri + priceBinanceTri
           
        if priceBeforeTri >= majorCoinBalance:
            
            majorCoinLeft = majorCoinBalance - priceOrderBinanceTri
            print('-------------------------')
            print(majorCoinLeft)
            amountOfCoinToStillBuy = majorCoinLeft / priceCoinBinanceTri
            print('-------------------------')
            print(amountOfCoinToStillBuy)
            priceOfSelectCoinsTri = amountOfCoinToStillBuy * priceCoinBinanceTri
            print('-------------------------')
            print(priceOfSelectCoinsTri)
            finalPriceBinanceTri = priceOrderBinanceTri + priceOfSelectCoinsTri
            print('-------------------------')
            print(finalPriceBinanceTri)
            amountOfCoins = (amountOfCoinToStillBuy + amountOfCoinsBinanceTri)
            # print(finalPriceBinance)
            minAmountDigits = minimumAmountDict[pairs]
            differenceInDigits = float(len(str(amountOfCoins))) - float(minAmountDigits)
            
            if differenceInDigits > 0:
                differenceInDigits = int(differenceInDigits * (-1))
                amountOfCoins = float(str(amountOfCoins)[:differenceInDigits])

            amountOfMinorCoin[pairs] = amountOfCoins * (1 - 0.001)
            amountOfMinorCoinBT[pairs] = amountOfCoins 
            
            break
        
        else:
            
            amountOfCoinsBinanceTri += amountCoinBinanceTri
            priceOrderBinanceTri += priceBinanceTri
print('-------------------------')
print(amountOfMinorCoin)
# a dict of all coins
# print(amountOfMinorCoin)

allCoinList = []
allCoinPrices = {}

for coin in prices:
    symbolTri = coin['symbol']
    priceTri = coin['price']
    allCoinList.append(symbolTri)
    allCoinPrices[symbolTri] = priceTri

    
    
coinListETH = []
coinListBTC = []
coinListUSDT = []
coinListBNB = []
ETHFirstThree = []
BTCFirstThree = []
BNBFirstThree = []
USDTFirstThree = []

for coins in allCoinList:
    
    
    
    
    if coins[-3:] == 'ETH':
        coinListETH.append(coins)
        if len(coins) == 8:
            coinNameTri = coins[:5]
        if len(coins) == 7:
            coinNameTri = coins[:4]
        
        if len(coins) == 6:
            coinNameTri = coins[:3]
        ETHFirstThree.append(coinNameTri)
        
    elif coins[-3:] == 'BTC':
        coinListBTC.append(coins)
        if len(coins) == 8:
            coinNameTri = coins[:5]
        if len(coins) == 7:
            coinNameTri = coins[:4]
        
        if len(coins) == 6:
            coinNameTri = coins[:3]
        BTCFirstThree.append(coinNameTri)
    elif coins[-3:] == 'BNB':
        coinListBNB.append(coins)
        if len(coins) == 8:
            coinNameTri = coins[:5]
        if len(coins) == 7:
            coinNameTri = coins[:4]
        
        if len(coins) == 6:
            coinNameTri = coins[:3]
        BNBFirstThree.append(coinNameTri)
    elif coins[-4:] == 'USDT':
        coinListUSDT.append(coins)
        if len(coins) == 8:
            coinNameTri = coins[:4]
        if len(coins) == 7:
            coinNameTri = coins[:3]
        
        if len(coins) == 9:
            coinNameTri = coins[:5]
        USDTFirstThree.append(coinNameTri)

        

      
BNBETHSimilar = []
    
for coins in ETHFirstThree:
    # create a dict of sim coins
    if coins in BNBFirstThree:
        coinsExtraBNBETH = coins + 'BNB'
        BNBETHSimilar.append(coinsExtraBNBETH)         

      
ETHBTCSimilar = []        
for coins in BTCFirstThree:
    if coins in ETHFirstThree:
        coinsExtraETHBTC = coins + 'ETH'
        ETHBTCSimilar.append(coinsExtraETHBTC)

BNBBTCSimilar = []
for coins in BTCFirstThree:
    if coins in BNBFirstThree:
        coinsExtraBNBBTC = coins + 'BNB'
        BNBBTCSimilar.append(coinsExtraBNBBTC)
        
BTCUSDTSimilar = []
for coins in USDTFirstThree:
    if coins in BTCFirstThree:
        coinsExtraBTCUSDT = coins + 'BTC'
        BTCUSDTSimilar.append(coinsExtraBTCUSDT)

ETHUSDTSimilar = []
for coins in USDTFirstThree:
    if coins in ETHFirstThree:
        coinsExtraETHUSDT = coins + 'ETH'
        ETHUSDTSimilar.append(coinsExtraETHUSDT)
    
BNBUSDTSimilar = []
for coins in USDTFirstThree:
    if coins in BNBFirstThree:
        coinsExtraBNBUSDT = coins + 'BNB'
        BNBUSDTSimilar.append(coinsExtraBNBUSDT)

       
# appends second coin name onto everything for looking at orders (above)
# this section goes through and calculates how much of a small coin i can buy then calculates how much of the big coin
# and calcs the profit 
# this one does eth bnb 
amountOfMiddleCoinBNBETH = {}
amountOfCoinsBinanceBNBETH = 0
priceOrderBinanceBNBETH = 0
# FOR BINANCE 
x = 0
for pairs in BNBETHSimilar:
    
    # print(pairs)
    
    amountOfCoinsBinanceBNBETH = 0
    
    

    priceOrderBinanceBNBETH = 0
    depthBinanceBNBETH = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

    bbuyBNBETH = depthBinanceBNBETH['bids']


    for orders in bbuyBNBETH:
        
        amountCoinBinanceBNBETH = float(orders[1])
        priceCoinBinanceBNBETH = float(orders[0])
        priceBinanceBNBETH = priceCoinBinanceBNBETH * amountCoinBinanceBNBETH
        
        priceBeforeBNBETH = priceOrderBinanceBNBETH + priceBinanceBNBETH
            
        if priceBeforeBNBETH >= amountOfMinorCoin['BNBETH']:
            x += 1
            print('-------------------------')
            print(x)
            minorCoinLeftBNBETH = amountOfMinorCoin['BNBETH'] - priceOrderBinanceBNBETH
            print('-------------------------')
            print(minorCoinLeftBNBETH)
            amountOfCoinToStillBuyBNBETH = minorCoinLeftBNBETH / priceCoinBinanceBNBETH
            print('-------------------------')
            print(amountOfCoinToStillBuyBNBETH)
            priceOfSelectCoinsBNBETH = amountOfCoinToStillBuyBNBETH * priceCoinBinanceBNBETH
            print('-------------------------')
            print(priceOfSelectCoinsBNBETH)
            finalPriceBinanceBNBETH = priceOrderBinanceBNBETH + priceOfSelectCoinsBNBETH
            print('-------------------------')
            print(finalPriceBinanceBNBETH)
            
            # print(finalPriceBinance)
            

            amountOfMiddleCoinBNBETH[pairs] = (amountOfCoinToStillBuyBNBETH + amountOfCoinsBinanceBNBETH) * (1 - 0.001) 
            
            break
        
        else:
            
            amountOfCoinsBinanceBNBETH += amountCoinBinanceBNBETH
            priceOrderBinanceBNBETH += priceBinanceBNBETH    
print('-------------------------')    
print(amountOfMiddleCoinBNBETH)
# this calcs for the final big coin, taking things back to the start and calcs the profit, also does trading fees
profitOfBigCoinBNBETH = {}
amountOfCoinsBinanceBNBETHF = 0
priceOrderBinanceBNBETHF = 0
# FOR BINANCE
x = 0
for pairs, vol in amountOfMiddleCoinBNBETH.items():
    if len(pairs) == 7:
        smallCoinNameBNBETH = pairs[:4] + 'ETH'
    if len(pairs) == 6:
        smallCoinNameBNBETH = pairs[:3] + 'ETH'
    if len(pairs) == 8:
        smallCoinNameBNBETH = pairs[:5] + 'ETH'
    
    
    # print(smallCoinNameBNBETH)
    amountOfCoinsBinanceBNBETHF = 0
    
    

    priceOrderBinanceBNBETHF = 0
    depthBinanceBNBETHF = bclient.get_order_book(symbol='{}'.format(smallCoinNameBNBETH), limit=10)

    bbuyBNBETHF = depthBinanceBNBETHF['asks']


    for orders in bbuyBNBETHF:
        
        amountCoinBinanceBNBETHF = float(orders[1])
        priceCoinBinanceBNBETHF = float(orders[0])
        priceBinanceBNBETHF = priceCoinBinanceBNBETHF * amountCoinBinanceBNBETHF
        
        amountCoinBeforeBNBETHF = amountOfCoinsBinanceBNBETHF + amountCoinBinanceBNBETHF
            
        if amountCoinBeforeBNBETHF >= float(amountOfMiddleCoinBNBETH[pairs]):
            x += 1
            print('-------------------------')
            print(smallCoinNameBNBETH)
            print('-------------------------')
            print(amountOfMiddleCoinBNBETH[pairs])
            print(x)
            print('-------------------------')
            print('-------------------------')
            print(priceOrderBinanceBNBETHF)
            middleCoinLeftBNBETHF = float(amountOfMiddleCoinBNBETH[pairs]) - amountOfCoinsBinanceBNBETHF
            print('-------------------------')
            print(middleCoinLeftBNBETHF)
            amountOfCoinToStillBuyBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
            print('-------------------------')
            print(priceCoinBinanceBNBETHF)
            
            # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
            print('-------------------------')
            print(amountOfCoinToStillBuyBNBETHF)
            finalPriceBinanceBNBETHF = priceOrderBinanceBNBETHF + amountOfCoinToStillBuyBNBETHF
            print('-------------------------')
            print(finalPriceBinanceBNBETHF)
            finalPriceATBNBETHF = finalPriceBinanceBNBETHF * (1 - 0.001)
            print('-------------------------')
            print(finalPriceATBNBETHF)
            
            # print(finalPriceBinance)
            

            profitOfBigCoinBNBETH[pairs] = finalPriceATBNBETHF
            
            break
        
        else:
            
            amountOfCoinsBinanceBNBETHF += amountCoinBinanceBNBETHF
            priceOrderBinanceBNBETHF += priceBinanceBNBETHF    
            print('PRICEORDER: ', priceOrderBinanceBNBETHF)
print('-------------------------')


# maybe do a quick system which then double checks just that coin to make
# sure the value of the coin has stayed the same b/f buying 


#
#
#
#
#
#







printThis = sorted(profitOfBigCoinBNBETH, key=profitOfBigCoinBNBETH.__getitem__, reverse=True)
bestCoinBNBETH = str(printThis[0])
smallCoinNameTestBNBETH = bestCoinBNBETH.replace('BNB', 'ETH')


print('-----------------------=-=-=')
print(smallCoinNameTestBNBETH)

amountOfMiddleCoinTestBNBETH = {}
amountOfCoinsBinanceTestBNBETHVol = 0
    
    

priceOrderBinanceTestBNBETHVol = 0
depthBinanceTestBNBETHVol = bclient.get_order_book(symbol=str(bestCoinBNBETH), limit=10)

bbuyTestBNBETHVol = depthBinanceTestBNBETHVol['bids']


for orders in bbuyTestBNBETHVol:
        
    amountCoinBinanceTestBNBETHVol = float(orders[1])
    priceCoinBinanceTestBNBETHVol = float(orders[0])
    priceBinanceTestBNBETHVol = priceCoinBinanceTestBNBETHVol * amountCoinBinanceTestBNBETHVol
        
    priceBeforeTestBNBETHVol = priceOrderBinanceTestBNBETHVol + priceBinanceTestBNBETHVol
            
    if priceBeforeTestBNBETHVol >= amountOfMinorCoin['BNBETH']:
        
            
        minorCoinLeftTestBNBETHVol = amountOfMinorCoin['BNBETH'] - priceOrderBinanceTestBNBETHVol
            
        amountOfCoinToStillBuyTestBNBETHVol = minorCoinLeftTestBNBETHVol / priceCoinBinanceTestBNBETHVol
            
        priceOfSelectCoinsTestBNBETHVol = amountOfCoinToStillBuyTestBNBETHVol * priceCoinBinanceTestBNBETHVol
            
        finalPriceBinanceTestBNBETHVol = priceOrderBinanceTestBNBETHVol + priceOfSelectCoinsTestBNBETHVol
           
            
            # print(finalPriceBinance)
           

        amountOfMiddleCoinTestBNBETH[bestCoinBNBETH] = (amountOfCoinToStillBuyTestBNBETHVol + amountOfCoinsBinanceTestBNBETHVol) * (1 - 0.001) 
            
        break
        
    else:
            
        amountOfCoinsBinanceTestBNBETHVol += amountCoinBinanceTestBNBETHVol
        priceOrderBinanceTestBNBETHVol += priceBinanceTestBNBETHVol    





# ---------------------------------------------------Part 2

# next it chekcs the coin again and then places a buy if above a couple percent


amountOfCoinsBinanceTestBNBETH = 0
priceOrderBinanceTestBNBETH = 0
finalCoinBNBETH = {}
depthBinanceTestBNBETH = bclient.get_order_book(symbol=str(smallCoinNameTestBNBETH), limit=10)
bbuyTestBNBETH = depthBinanceTestBNBETH['asks']
print('__________________________________________-')

for orders in bbuyTestBNBETH:
    amountCoinBinanceTestBNBETH = float(orders[1])
    priceCoinBinanceTestBNBETH = float(orders[0])
    priceBinanceTestBNBETH = priceCoinBinanceTestBNBETH * amountCoinBinanceTestBNBETH
    amountCoinBeforeTestBNBETH = amountOfCoinsBinanceTestBNBETH + amountCoinBinanceTestBNBETH
    print('AMOUNT ', amountCoinBeforeTestBNBETH)
           

    if amountCoinBeforeTestBNBETH >= float(amountOfMiddleCoinTestBNBETH[bestCoinBNBETH]):
        print(bbuyTestBNBETH)
        print(amountOfMiddleCoinTestBNBETH[bestCoinBNBETH])
        print(amountOfMiddleCoinBNBETH[bestCoinBNBETH])
    
        
        
        
        middleCoinLeftTestBNBETH = float(amountOfMiddleCoinTestBNBETH[bestCoinBNBETH]) - amountOfCoinsBinanceTestBNBETH
        print(amountOfCoinsBinanceTestBNBETH)
        print(middleCoinLeftTestBNBETH)
        
        amountOfCoinToStillBuyTestBNBETH = middleCoinLeftTestBNBETH * priceCoinBinanceTestBNBETH
        print(amountOfCoinToStillBuyTestBNBETH)
            
        # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
        
        finalPriceBinanceTestBNBETH = priceOrderBinanceTestBNBETH + amountOfCoinToStillBuyTestBNBETH
        print(finalPriceBinanceTestBNBETH)
        print(priceOrderBinanceTestBNBETH)
        
        finalPriceTestATBNBETH = finalPriceBinanceTestBNBETH * (1 - 0.001)
        
            
            # print(finalPriceBinance)
            

        finalCoinBNBETH[smallCoinNameTestBNBETH] = finalPriceTestATBNBETH
            

        break
        
    else:
            
        amountOfCoinsBinanceTestBNBETH += amountCoinBinanceTestBNBETH
        priceOrderBinanceTestBNBETH += priceBinanceTestBNBETH    
        


finalCoinPercentage = (finalCoinBNBETH[smallCoinNameTestBNBETH] - accountBalanceBinanceEthereum) / accountBalanceBinanceEthereum
print('_________________________')
print(finalCoinBNBETH)
print(finalCoinPercentage)
print(profitOfBigCoinBNBETH[bestCoinBNBETH])



if finalCoinPercentage > -1:
    
    
    print('1')
    
    while True:
        
        try:
            
        
            
            print('good op')

            
            
            print('a')
            transaction = bclient.order_market_buy(symbol='BNBETH', quantity=float(amountOfMinorCoinBT['BNBETH']))
            print(transaction)
            print('m')
            
            
            print('next part')
            rdnVarBNBETH = 3
                

            print('d')
            
            print('e')
            time.sleep(0.5)
            if transaction['status'] != 'FILLED':
                print('order not filled')
                break                    
                    
            else:
                print('order filled')
                print('n')
                accountBalanceMiddleCoinBNBETH = float(bclient.get_asset_balance(asset='BNB')['free'])
                    
                while True:
                   
                    try:
                        print('v')                      
                        transaction2 = bclient.order_market_buy(symbol=str(bestCoinBNBETH), quantity=float(amountOfMiddleCoinTestBNBETH[bestCoinBNBETH]))
                        print(transaction2)


                        
                        print('mm')
                        rdnVar2BNBETH = 2
                       
                        print('bb')
                        justFirstThreeBNBETH = smallCoinNameTestBNBETH.replace('ETH', '')
                        print('2442')
                            
                        print('final part')
                        if transaction2['status'] != 'FILLED':
                            
                            print('order not filled yet')
                        else:
                            print('order filled hoe')
                            print('ll')
                            accountBalanceFinalStepBNBETH = float(bclient.get_asset_balance(asset='BNB')['free'])
                            while True:
                                    
                                try:
                                        
                                    print('ii')
                                    transaction3 = bclient.order_market_sell(symbol=str(smallCoinNameTestBNBETH), quatity=accountBalanceFinalStepBNBETH)
                                    print('z')
                                    finalCommandBNBETH = 7
                                    print('DUN FINALY BOSS')
                                    break
                                except:
                                    accountBalanceFinalStepBNBETH = float(str(accountBalanceFinalStepBNBETH)[:-1])
                                    print(accountBalanceFinalStepBNBETH)
                                    continue
                            if finalCommandBNBETH == 7:
                                print('getting there')
                                break
                        if rdnVar2BNBETH == 2:
                            print('almost done')
                            break
                    except:
                        accountBalanceMiddleCoinBNBETH = float(str(accountBalanceMiddleCoinBNBETH)[:-1])
                        print(accountBalanceMiddleCoinBNBETH)
                        continue
       
            if rdnVarBNBETH == 3:
                print('dunzoooo')
                break
        except:
            print('error BOSS REPORT STATION 12')
            break
    
    
    

    
    

#
# 500 hundred 


# In[11]:



accountBalanceMajorCoinBNBETH = 0.001
transcation = bclient.order_market_buy(symbol='BNBETH', quantity=accountBalanceMajorCoinBNBETH)
print(transaction)


# In[15]:


# tri arbi binance 


prices = bclient.get_all_tickers() # get all binance prices



startingPairs = ['ETHBTC', 'BNBBTC', 'BNBETH', 'BTCUSDT', 'ETHUSDT', 'BNBUSDT']

# gets last 3/4 letters





x = 0
# calculates how much of the coin i can buy with my current reserves

amountOfMinorCoin = {}
amountOfCoinsBinanceTri = 0
priceOrderBinanceTri = 0
# FOR BINANCE 
for pairs in startingPairs:
    if len(pairs) == 6:
        lastLetters = pairs[-3:]
    
    if len(pairs) == 7:
        lastLetters = pairs[-4:]
    
        
    majorCoinBalance = float(accountBalanceBinanceDict[lastLetters])
    
    
    amountOfCoinsBinanceTri = 0
    
    

    priceOrderBinanceTri = 0
    depthBinanceTri = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

    bbuyTri = depthBinanceTri['bids']


    for ordersTri in bbuyTri:
        
        amountCoinBinanceTri = float(ordersTri[1])
        priceCoinBinanceTri = float(ordersTri[0])
        priceBinanceTri = priceCoinBinanceTri * amountCoinBinanceTri
        
        priceBeforeTri = priceOrderBinanceTri + priceBinanceTri
           
        if priceBeforeTri >= majorCoinBalance:
            x += 1
            print('-------------------------')
            print(x)
            majorCoinLeft = majorCoinBalance - priceOrderBinanceTri
            print('-------------------------')
            print(majorCoinLeft)
            amountOfCoinToStillBuy = majorCoinLeft / priceCoinBinanceTri
            print('-------------------------')
            print(amountOfCoinToStillBuy)
            priceOfSelectCoinsTri = amountOfCoinToStillBuy * priceCoinBinanceTri
            print('-------------------------')
            print(priceOfSelectCoinsTri)
            finalPriceBinanceTri = priceOrderBinanceTri + priceOfSelectCoinsTri
            print('-------------------------')
            print(finalPriceBinanceTri)
            
            # print(finalPriceBinance)
            

            amountOfMinorCoin[pairs] = (amountOfCoinToStillBuy + amountOfCoinsBinanceTri) * (1 - 0.001) 
            
            break
        
        else:
            
            amountOfCoinsBinanceTri += amountCoinBinanceTri
            priceOrderBinanceTri += priceBinanceTri
print('-------------------------')
print(amountOfMinorCoin)
# a dict of all coins
# print(amountOfMinorCoin)

allCoinList = []
allCoinPrices = {}

for coin in prices:
    symbolTri = coin['symbol']
    priceTri = coin['price']
    allCoinList.append(symbolTri)
    allCoinPrices[symbolTri] = priceTri

    
    
coinListETH = []
coinListBTC = []
coinListUSDT = []
coinListBNB = []
ETHFirstThree = []
BTCFirstThree = []
BNBFirstThree = []
USDTFirstThree = []

for coins in allCoinList:
    
    
    
    
    if coins[-3:] == 'ETH':
        coinListETH.append(coins)
        if len(coins) == 8:
            coinNameTri = coins[:5]
        if len(coins) == 7:
            coinNameTri = coins[:4]
        
        if len(coins) == 6:
            coinNameTri = coins[:3]
        ETHFirstThree.append(coinNameTri)
        
    elif coins[-3:] == 'BTC':
        coinListBTC.append(coins)
        if len(coins) == 8:
            coinNameTri = coins[:5]
        if len(coins) == 7:
            coinNameTri = coins[:4]
        
        if len(coins) == 6:
            coinNameTri = coins[:3]
        BTCFirstThree.append(coinNameTri)
    elif coins[-3:] == 'BNB':
        coinListBNB.append(coins)
        if len(coins) == 8:
            coinNameTri = coins[:5]
        if len(coins) == 7:
            coinNameTri = coins[:4]
        
        if len(coins) == 6:
            coinNameTri = coins[:3]
        BNBFirstThree.append(coinNameTri)
    elif coins[-4:] == 'USDT':
        coinListUSDT.append(coins)
        if len(coins) == 8:
            coinNameTri = coins[:4]
        if len(coins) == 7:
            coinNameTri = coins[:3]
        
        if len(coins) == 9:
            coinNameTri = coins[:5]
        USDTFirstThree.append(coinNameTri)

        

      
BNBETHSimilar = []
    
for coins in ETHFirstThree:
    # create a dict of sim coins
    if coins in BNBFirstThree:
        coinsExtraBNBETH = coins + 'BNB'
        BNBETHSimilar.append(coinsExtraBNBETH)         

      
ETHBTCSimilar = []        
for coins in BTCFirstThree:
    if coins in ETHFirstThree:
        coinsExtraETHBTC = coins + 'ETH'
        ETHBTCSimilar.append(coinsExtraETHBTC)

BNBBTCSimilar = []
for coins in BTCFirstThree:
    if coins in BNBFirstThree:
        coinsExtraBNBBTC = coins + 'BNB'
        BNBBTCSimilar.append(coinsExtraBNBBTC)
        
BTCUSDTSimilar = []
for coins in USDTFirstThree:
    if coins in BTCFirstThree:
        coinsExtraBTCUSDT = coins + 'BTC'
        BTCUSDTSimilar.append(coinsExtraBTCUSDT)

ETHUSDTSimilar = []
for coins in USDTFirstThree:
    if coins in ETHFirstThree:
        coinsExtraETHUSDT = coins + 'ETH'
        ETHUSDTSimilar.append(coinsExtraETHUSDT)
    
BNBUSDTSimilar = []
for coins in USDTFirstThree:
    if coins in BNBFirstThree:
        coinsExtraBNBUSDT = coins + 'BNB'
        BNBUSDTSimilar.append(coinsExtraBNBUSDT)

       
# appends second coin name onto everything for looking at orders (above)
# this section goes through and calculates how much of a small coin i can buy then calculates how much of the big coin
# and calcs the profit 
# this one does eth bnb 
amountOfMiddleCoinBNBETH = {}
amountOfCoinsBinanceBNBETH = 0
priceOrderBinanceBNBETH = 0
# FOR BINANCE 
x = 0
for pairs in BNBETHSimilar:
    
    # print(pairs)
    
    amountOfCoinsBinanceBNBETH = 0
    
    

    priceOrderBinanceBNBETH = 0
    depthBinanceBNBETH = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

    bbuyBNBETH = depthBinanceBNBETH['bids']


    for orders in bbuyBNBETH:
        
        amountCoinBinanceBNBETH = float(orders[1])
        priceCoinBinanceBNBETH = float(orders[0])
        priceBinanceBNBETH = priceCoinBinanceBNBETH * amountCoinBinanceBNBETH
        
        priceBeforeBNBETH = priceOrderBinanceBNBETH + priceBinanceBNBETH
            
        if priceBeforeBNBETH >= amountOfMinorCoin['BNBETH']:
            x += 1
            print('-------------------------')
            print(x)
            minorCoinLeftBNBETH = amountOfMinorCoin['BNBETH'] - priceOrderBinanceBNBETH
            print('-------------------------')
            print(minorCoinLeftBNBETH)
            amountOfCoinToStillBuyBNBETH = minorCoinLeftBNBETH / priceCoinBinanceBNBETH
            print('-------------------------')
            print(amountOfCoinToStillBuyBNBETH)
            priceOfSelectCoinsBNBETH = amountOfCoinToStillBuyBNBETH * priceCoinBinanceBNBETH
            print('-------------------------')
            print(priceOfSelectCoinsBNBETH)
            finalPriceBinanceBNBETH = priceOrderBinanceBNBETH + priceOfSelectCoinsBNBETH
            print('-------------------------')
            print(finalPriceBinanceBNBETH)
            
            # print(finalPriceBinance)
            

            amountOfMiddleCoinBNBETH[pairs] = (amountOfCoinToStillBuyBNBETH + amountOfCoinsBinanceBNBETH) * (1 - 0.001) 
            
            break
        
        else:
            
            amountOfCoinsBinanceBNBETH += amountCoinBinanceBNBETH
            priceOrderBinanceBNBETH += priceBinanceBNBETH    
print('-------------------------')    
print(amountOfMiddleCoinBNBETH)
# this calcs for the final big coin, taking things back to the start and calcs the profit, also does trading fees
profitOfBigCoinBNBETH = {}
amountOfCoinsBinanceBNBETHF = 0
priceOrderBinanceBNBETHF = 0
# FOR BINANCE
x = 0
for pairs, vol in amountOfMiddleCoinBNBETH.items():
    if len(pairs) == 7:
        smallCoinNameBNBETH = pairs[:4] + 'ETH'
    if len(pairs) == 6:
        smallCoinNameBNBETH = pairs[:3] + 'ETH'
    if len(pairs) == 8:
        smallCoinNameBNBETH = pairs[:5] + 'ETH'
    
    
    # print(smallCoinNameBNBETH)
    amountOfCoinsBinanceBNBETHF = 0
    
    

    priceOrderBinanceBNBETHF = 0
    depthBinanceBNBETHF = bclient.get_order_book(symbol='{}'.format(smallCoinNameBNBETH), limit=10)

    bbuyBNBETHF = depthBinanceBNBETHF['asks']


    for orders in bbuyBNBETHF:
        
        amountCoinBinanceBNBETHF = float(orders[1])
        priceCoinBinanceBNBETHF = float(orders[0])
        priceBinanceBNBETHF = priceCoinBinanceBNBETHF * amountCoinBinanceBNBETHF
        
        amountCoinBeforeBNBETHF = amountOfCoinsBinanceBNBETHF + amountCoinBinanceBNBETHF
            
        if amountCoinBeforeBNBETHF >= float(amountOfMiddleCoinBNBETH[pairs]):
            x += 1
            print('-------------------------')
            print(smallCoinNameBNBETH)
            print('-------------------------')
            print(amountOfMiddleCoinBNBETH[pairs])
            print(x)
            print('-------------------------')
            print('-------------------------')
            print(priceOrderBinanceBNBETHF)
            middleCoinLeftBNBETHF = float(amountOfMiddleCoinBNBETH[pairs]) - amountOfCoinsBinanceBNBETHF
            print('-------------------------')
            print(middleCoinLeftBNBETHF)
            amountOfCoinToStillBuyBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
            print('-------------------------')
            print(priceCoinBinanceBNBETHF)
            
            # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
            print('-------------------------')
            print(amountOfCoinToStillBuyBNBETHF)
            finalPriceBinanceBNBETHF = priceOrderBinanceBNBETHF + amountOfCoinToStillBuyBNBETHF
            print('-------------------------')
            print(finalPriceBinanceBNBETHF)
            finalPriceATBNBETHF = finalPriceBinanceBNBETHF * (1 - 0.001)
            print('-------------------------')
            print(finalPriceATBNBETHF)
            
            # print(finalPriceBinance)
            

            profitOfBigCoinBNBETH[pairs] = finalPriceATBNBETHF
            
            break
        
        else:
            
            amountOfCoinsBinanceBNBETHF += amountCoinBinanceBNBETHF
            priceOrderBinanceBNBETHF += priceBinanceBNBETHF    
            print('PRICEORDER: ', priceOrderBinanceBNBETHF)
print('-------------------------')


# maybe do a quick system which then double checks just that coin to make
# sure the value of the coin has stayed the same b/f buying 


#
#
#
#
#
#







printThis = sorted(profitOfBigCoinBNBETH, key=profitOfBigCoinBNBETH.__getitem__, reverse=True)
bestCoinBNBETH = str(printThis[0])
smallCoinNameTestBNBETH = bestCoinBNBETH.replace('BNB', 'ETH')


print('-----------------------=-=-=')
print(smallCoinNameTestBNBETH)

amountOfMiddleCoinTestBNBETH = {}
amountOfCoinsBinanceTestBNBETHVol = 0
    
    

priceOrderBinanceTestBNBETHVol = 0
depthBinanceTestBNBETHVol = bclient.get_order_book(symbol=str(bestCoinBNBETH), limit=10)

bbuyTestBNBETHVol = depthBinanceTestBNBETHVol['bids']


for orders in bbuyTestBNBETHVol:
        
    amountCoinBinanceTestBNBETHVol = float(orders[1])
    priceCoinBinanceTestBNBETHVol = float(orders[0])
    priceBinanceTestBNBETHVol = priceCoinBinanceTestBNBETHVol * amountCoinBinanceTestBNBETHVol
        
    priceBeforeTestBNBETHVol = priceOrderBinanceTestBNBETHVol + priceBinanceTestBNBETHVol
            
    if priceBeforeTestBNBETHVol >= amountOfMinorCoin['BNBETH']:
        
            
        minorCoinLeftTestBNBETHVol = amountOfMinorCoin['BNBETH'] - priceOrderBinanceTestBNBETHVol
            
        amountOfCoinToStillBuyTestBNBETHVol = minorCoinLeftTestBNBETHVol / priceCoinBinanceTestBNBETHVol
            
        priceOfSelectCoinsTestBNBETHVol = amountOfCoinToStillBuyTestBNBETHVol * priceCoinBinanceTestBNBETHVol
            
        finalPriceBinanceTestBNBETHVol = priceOrderBinanceTestBNBETHVol + priceOfSelectCoinsTestBNBETHVol
           
            
            # print(finalPriceBinance)
           

        amountOfMiddleCoinTestBNBETH[bestCoinBNBETH] = (amountOfCoinToStillBuyTestBNBETHVol + amountOfCoinsBinanceTestBNBETHVol) * (1 - 0.001) 
            
        break
        
    else:
            
        amountOfCoinsBinanceTestBNBETHVol += amountCoinBinanceTestBNBETHVol
        priceOrderBinanceTestBNBETHVol += priceBinanceTestBNBETHVol    





# ---------------------------------------------------Part 2

# next it chekcs the coin again and then places a buy if above a couple percent


amountOfCoinsBinanceTestBNBETH = 0
priceOrderBinanceTestBNBETH = 0
finalCoinBNBETH = {}
depthBinanceTestBNBETH = bclient.get_order_book(symbol=str(smallCoinNameTestBNBETH), limit=10)
bbuyTestBNBETH = depthBinanceTestBNBETH['asks']
print('__________________________________________-')

for orders in bbuyTestBNBETH:
    amountCoinBinanceTestBNBETH = float(orders[1])
    priceCoinBinanceTestBNBETH = float(orders[0])
    priceBinanceTestBNBETH = priceCoinBinanceTestBNBETH * amountCoinBinanceTestBNBETH
    amountCoinBeforeTestBNBETH = amountOfCoinsBinanceTestBNBETH + amountCoinBinanceTestBNBETH
    print('AMOUNT ', amountCoinBeforeTestBNBETH)
           

    if amountCoinBeforeTestBNBETH >= float(amountOfMiddleCoinTestBNBETH[bestCoinBNBETH]):
        print(bbuyTestBNBETH)
        print(amountOfMiddleCoinTestBNBETH[bestCoinBNBETH])
        print(amountOfMiddleCoinBNBETH[bestCoinBNBETH])
    
        
        
        
        middleCoinLeftTestBNBETH = float(amountOfMiddleCoinTestBNBETH[bestCoinBNBETH]) - amountOfCoinsBinanceTestBNBETH
        print(amountOfCoinsBinanceTestBNBETH)
        print(middleCoinLeftTestBNBETH)
        
        amountOfCoinToStillBuyTestBNBETH = middleCoinLeftTestBNBETH * priceCoinBinanceTestBNBETH
        print(amountOfCoinToStillBuyTestBNBETH)
            
        # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
        
        finalPriceBinanceTestBNBETH = priceOrderBinanceTestBNBETH + amountOfCoinToStillBuyTestBNBETH
        print(finalPriceBinanceTestBNBETH)
        print(priceOrderBinanceTestBNBETH)
        
        finalPriceTestATBNBETH = finalPriceBinanceTestBNBETH * (1 - 0.001)
        
            
            # print(finalPriceBinance)
            

        finalCoinBNBETH[smallCoinNameTestBNBETH] = finalPriceTestATBNBETH
            

        break
        
    else:
            
        amountOfCoinsBinanceTestBNBETH += amountCoinBinanceTestBNBETH
        priceOrderBinanceTestBNBETH += priceBinanceTestBNBETH    
        


finalCoinPercentage = (finalCoinBNBETH[smallCoinNameTestBNBETH] - accountBalanceBinanceEthereum) / accountBalanceBinanceEthereum
print('_________________________')
print(finalCoinBNBETH)
print(finalCoinPercentage)
print(profitOfBigCoinBNBETH[bestCoinBNBETH])
if finalCoinPercentage > 0.04:
    # buy 3 way around.  Add a part which transfers USDT into the coin first so that my balance will be stable 
    print('good op')


    transaction = client.bclient.order_market_sell(symbol='BNBETH', quantity=BALANCEFIX)
                # orders = client.get_active_orders('{}'.format(bestCoinETH))
            
    if transaction['orderOid']:
        print('next part')
        rdnVarFinal = 3
        print(transaction)  
        orders = client.get_active_orders(str(bestCoinETH))
        print(orders)
        print('d')
        # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
        print('e')
        time.sleep(1)
        if orders['BUY']:
            print('order not filled')
            client.cancel_all_orders()
        else:
            print('order filled')
            time.sleep(1)
            transaction2 = bclient.order_market_sell(symbol=str(), quantity=BALANCEFIX)


    
    
    

    
    

    
    

    

     
# # BNB BINANCE 

# amountOfMiddleCoinBNBBTC = {}

# for pairs in BNBBTCSimilar:
    
#     print(pairs)
    
#     amountOfCoinsBinanceBNBBTC = 0
    
    

#     priceOrderBinanceBNBBTC = 0
#     depthBinanceBNBBTC = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

#     bbuyBNBBTC = depthBinanceBNBBTC['bids']


#     for orders in bbuyBNBBTC:
        
#         amountCoinBinanceBNBBTC = float(orders[1])
#         priceCoinBinanceBNBBTC = float(orders[0])
#         priceBinanceBNBBTC = priceCoinBinanceBNBBTC * amountCoinBinanceBNBBTC
        
#         priceBeforeBNBBTC = priceOrderBinanceBNBBTC + priceBinanceBNBBTC
            
#         if priceBeforeBNBBTC >= amountOfMinorCoin['BNBBTC']:
#             x += 1
#             print('-------------------------')
#             print(x)
#             minorCoinLeftBNBBTC = amountOfMinorCoin['BNBBTC'] - priceOrderBinanceBNBBTC
#             print('-------------------------')
#             print(minorCoinLeftBNBBTC)
#             amountOfCoinToStillBuyBNBBTC = minorCoinLeftBNBBTC / priceCoinBinanceBNBBTC
#             print('-------------------------')
#             print(amountOfCoinToStillBuyBNBBTC)
#             priceOfSelectCoinsBNBBTC = amountOfCoinToStillBuyBNBBTC * priceCoinBinanceBNBBTC
#             print('-------------------------')
#             print(priceOfSelectCoinsBNBBTC)
#             finalPriceBinanceBNBBTC = priceOrderBinanceBNBBTC + priceOfSelectCoinsBNBBTC
#             print('-------------------------')
#             print(finalPriceBinanceBNBBTC)
            
#             # print(finalPriceBinance)
            

#             amountOfMiddleCoinBNBBTC[pairs] = (amountOfCoinToStillBuyBNBBTC + amountOfCoinsBinanceBNBBTC) * (1 - 0.001) 
            
#             break
        
#         else:
            
#             amountOfCoinsBinanceBNBBTC += amountCoinBinanceBNBBTC
#             priceOrderBinanceBNBBTC += priceBinanceBNBBTC    
# print('-------------------------')    
# print(amountOfMiddleCoinBNBBTC)
# # this calcs for the final big coin, taking things back to the start and calcs the profit, also does trading fees
# profitOfBigCoinBNBBTC = {}
# amountOfCoinsBinanceBNBBTCF = 0
# priceOrderBinanceBNBBTCF = 0
# # FOR BINANCE
# x = 0
# for pairs, vol in amountOfMiddleCoinBNBBTC.items():
#     if len(pairs) == 7:
#         smallCoinNameBNBBTC = pairs[:4] + 'BTC'
#     if len(pairs) == 6:
#         smallCoinNameBNBBTC = pairs[:3] + 'BTC'
#     if len(pairs) == 8:
#         smallCoinNameBNBBTC = pairs[:5] + 'BTC'
    
    
#     # print(smallCoinNameBNBETH)
#     amountOfCoinsBinanceBNBBTCF = 0
    
    

#     priceOrderBinanceBNBBTCF = 0
#     depthBinanceBNBBTCF = bclient.get_order_book(symbol='{}'.format(smallCoinNameBNBBTC), limit=10)

#     bbuyBNBBTCF = depthBinanceBNBBTCF['asks']


#     for orders in bbuyBNBBTCF:
        
#         amountCoinBinanceBNBBTCF = float(orders[1])
#         priceCoinBinanceBNBBTCF = float(orders[0])
#         priceBinanceBNBBTCF = priceCoinBinanceBNBBTCF * amountCoinBinanceBNBBTCF
        
#         amountCoinBeforeBNBBTCF = amountOfCoinsBinanceBNBBTCF + amountCoinBinanceBNBBTCF
            
#         if amountCoinBeforeBNBBTCF >= float(amountOfMiddleCoinBNBBTC[pairs]):
#             x += 1
#             print('-------------------------')
#             print(smallCoinNameBNBBTC)
#             print('-------------------------')
#             print(amountOfMiddleCoinBNBBTC[pairs])
#             print(x)
#             print('-------------------------')
#             print('-------------------------')
#             print(priceOrderBinanceBNBBTCF)
#             middleCoinLeftBNBBTCF = float(amountOfMiddleCoinBNBBTC[pairs]) - amountOfCoinsBinanceBNBBTCF
#             print('-------------------------')
#             print(middleCoinLeftBNBBTCF)
#             amountOfCoinToStillBuyBNBBTCF = middleCoinLeftBNBBTCF * priceCoinBinanceBNBBTCF
#             print('-------------------------')
#             print(priceCoinBinanceBNBBTCF)
            
#             # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
#             print('-------------------------')
#             print(amountOfCoinToStillBuyBNBBTCF)
#             finalPriceBinanceBNBBTCF = priceOrderBinanceBNBBTCF + amountOfCoinToStillBuyBNBBTCF
#             print('-------------------------')
#             print(finalPriceBinanceBNBBTCF)
#             finalPriceATBNBBTCF = finalPriceBinanceBNBBTCF * (1 - 0.001)
#             print('-------------------------')
#             print(finalPriceATBNBBTCF)
            
#             # print(finalPriceBinance)
            

#             profitOfBigCoinBNBBTC[pairs] = finalPriceATBNBBTCF
            
#             break
        
#         else:
            
#             amountOfCoinsBinanceBNBBTCF += amountCoinBinanceBNBBTCF
#             priceOrderBinanceBNBBTCF += priceBinanceBNBBTCF    
#             print('PRICEORDER: ', priceOrderBinanceBNBBTCF)
# print('-------------------------')


# # maybe do a quick system which then double checks just that coin to make
# # sure the value of the coin has stayed the same b/f buying 


# #
# #
# #
# #
# #
# #







# printThisBNBBTC = sorted(profitOfBigCoinBNBBTC, key=profitOfBigCoinBNBBTC.__getitem__, reverse=True)
# bestCoinBNBBTC = str(printThisBNBBTC[0])
# smallCoinNameTestBNBBTC = bestCoinBNBBTC.replace('BNB', 'BTC')


# print('-----------------------=-=-=')
# print(smallCoinNameTestBNBBTC)

# amountOfMiddleCoinTestBNBBTC = {}
# amountOfCoinsBinanceTestBNBBTCVol = 0
    
    

# priceOrderBinanceTestBNBBTCVol = 0
# depthBinanceTestBNBBTCVol = bclient.get_order_book(symbol=str(bestCoinBNBBTC), limit=10)

# bbuyTestBNBBTCVol = depthBinanceTestBNBBTCVol['bids']


# for orders in bbuyTestBNBBTCVol:
        
#     amountCoinBinanceTestBNBBTCVol = float(orders[1])
#     priceCoinBinanceTestBNBBTCVol = float(orders[0])
#     priceBinanceTestBNBBTCVol = priceCoinBinanceTestBNBBTCVol * amountCoinBinanceTestBNBBTCVol
        
#     priceBeforeTestBNBBTCVol = priceOrderBinanceTestBNBBTCVol + priceBinanceTestBNBBTCVol
            
#     if priceBeforeTestBNBBTCVol >= amountOfMinorCoin['BNBBTC']:
        
            
#         minorCoinLeftTestBNBBTCVol = amountOfMinorCoin['BNBBTC'] - priceOrderBinanceTestBNBBTCVol
            
#         amountOfCoinToStillBuyTestBNBBTCVol = minorCoinLeftTestBNBBTCVol / priceCoinBinanceTestBNBBTCVol
            
#         priceOfSelectCoinsTestBNBBTCVol = amountOfCoinToStillBuyTestBNBBTCVol * priceCoinBinanceTestBNBBTCVol
            
#         finalPriceBinanceTestBNBBTCVol = priceOrderBinanceTestBNBBTCVol + priceOfSelectCoinsTestBNBBTCVol
           
            
#             # print(finalPriceBinance)
           

#         amountOfMiddleCoinTestBNBBTC[bestCoinBNBBTC] = (amountOfCoinToStillBuyTestBNBBTCVol + amountOfCoinsBinanceTestBNBBTCVol) * (1 - 0.001) 
            
#         break
        
#     else:
            
#         amountOfCoinsBinanceTestBNBBTCVol += amountCoinBinanceTestBNBBTCVol
#         priceOrderBinanceTestBNBBTCVol += priceBinanceTestBNBBTCVol    





# # ---------------------------------------------------Part 2

# # next it chekcs the coin again and then places a buy if above a couple percent


# amountOfCoinsBinanceTestBNBBTC = 0
# priceOrderBinanceTestBNBBTC = 0
# finalCoinBNBBTC = {}
# depthBinanceTestBNBBTC = bclient.get_order_book(symbol=str(smallCoinNameTestBNBBTC), limit=10)
# bbuyTestBNBBTC = depthBinanceTestBNBBTC['asks']
# print('__________________________________________-')

# for orders in bbuyTestBNBBTC:
#     amountCoinBinanceTestBNBBTC = float(orders[1])
#     priceCoinBinanceTestBNBBTC = float(orders[0])
#     priceBinanceTestBNBBTC = priceCoinBinanceTestBNBBTC * amountCoinBinanceTestBNBBTC
#     amountCoinBeforeTestBNBBTC = amountOfCoinsBinanceTestBNBBTC + amountCoinBinanceTestBNBBTC
#     print('AMOUNT ', amountCoinBeforeTestBNBBTC)
           

#     if amountCoinBeforeTestBNBBTC >= float(amountOfMiddleCoinTestBNBBTC[bestCoinBNBBTC]):
#         print(bbuyTestBNBBTC)
#         print(amountOfMiddleCoinTestBNBBTC[bestCoinBNBBTC])
#         print(amountOfMiddleCoinBNBBTC[bestCoinBNBBTC])
    
        
        
        
#         middleCoinLeftTestBNBBTC = float(amountOfMiddleCoinTestBNBBTC[bestCoinBNBBTC]) - amountOfCoinsBinanceTestBNBBTC
#         print(amountOfCoinsBinanceTestBNBBTC)
#         print(middleCoinLeftTestBNBBTC)
        
#         amountOfCoinToStillBuyTestBNBBTC = middleCoinLeftTestBNBBTC * priceCoinBinanceTestBNBBTC
#         print(amountOfCoinToStillBuyTestBNBBTC)
            
#         # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
        
#         finalPriceBinanceTestBNBBTC = priceOrderBinanceTestBNBBTC + amountOfCoinToStillBuyTestBNBBTC
#         print(finalPriceBinanceTestBNBBTC)
#         print(priceOrderBinanceTestBNBBTC)
        
#         finalPriceTestATBNBBTC = finalPriceBinanceTestBNBBTC * (1 - 0.001)
        
            
#             # print(finalPriceBinance)
            

#         finalCoinBNBBTC[smallCoinNameTestBNBBTC] = finalPriceTestATBNBBTC
            

#         break
        
#     else:
            
#         amountOfCoinsBinanceTestBNBBTC += amountCoinBinanceTestBNBBTC
#         priceOrderBinanceTestBNBBTC += priceBinanceTestBNBBTC    
        


# finalCoinPercentageBNBBTC = (finalCoinBNBBTC[smallCoinNameTestBNBBTC] - accountBalanceBinanceBitcoin) / accountBalanceBinanceBitcoin
# print('_________________________')
# print(finalCoinBNBBTC)
# print(finalCoinPercentageBNBBTC)
# print(profitOfBigCoinBNBBTC[bestCoinBNBBTC])
# if finalCoinPercentageBNBBTC > 0.04:
#     # buy 3 way around.  Add a part which transfers USDT into the coin first so that my balance will be stable 
#     print('good op')


#     transactionBNBBTC = client.bclient.order_market_sell(symbol='BNBBTC', quantity=BALANCEFIX)
#                 # orders = client.get_active_orders('{}'.format(bestCoinETH))
            
#     if transaction['orderOid']:
#         print('next part')
#         rdnVarFinal = 3
#         print(transaction)  
#         orders = client.get_active_orders(str(bestCoinETH))
#         print(orders)
#         print('d')
#         # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
#         print('e')
#         time.sleep(1)
#         if orders['BUY']:
#             print('order not filled')
#             client.cancel_all_orders()
#         else:
#             print('order filled')
#             time.sleep(1)
#             transaction2BNBBTC = bclient.order_market_sell(symbol=str(), quantity=BALANCEFIX)

 
    
    
    
    
    
    
    
    
    
    
    
    
# ETHBTC BABY


# amountOfMiddleCoinETHBTC = {}
# amountOfCoinsBinanceETHBTC = 0
# priceOrderBinanceETHBTC = 0
# # FOR BINANCE 
# x = 0
# for pairs in ETHBTCSimilar:
    
#     # print(pairs)
    
#     amountOfCoinsBinanceETHBTC = 0
    
    

#     priceOrderBinanceETHBTC = 0
#     depthBinanceETHBTC = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

#     bbuyETHBTC = depthBinanceETHBTC['bids']


#     for orders in bbuyETHBTC:
        
#         amountCoinBinanceETHBTC = float(orders[1])
#         priceCoinBinanceETHBTC = float(orders[0])
#         priceBinanceETHBTC = priceCoinBinanceETHBTC * amountCoinBinanceETHBTC
        
#         priceBeforeETHBTC = priceOrderBinanceETHBTC + priceBinanceETHBTC
            
#         if priceBeforeETHBTC >= amountOfMinorCoin['ETHBTC']:
#             x += 1
#             print('-------------------------')
#             print(x)
#             minorCoinLeftETHBTC = amountOfMinorCoin['ETHBTC'] - priceOrderBinanceETHBTC
#             print('-------------------------')
#             print(minorCoinLeftETHBTC)
#             amountOfCoinToStillBuyETHBTC = minorCoinLeftETHBTC / priceCoinBinanceETHBTC
#             print('-------------------------')
#             print(amountOfCoinToStillBuyETHBTC)
#             priceOfSelectCoinsETHBTC = amountOfCoinToStillBuyETHBTC * priceCoinBinanceETHBTC
#             print('-------------------------')
#             print(priceOfSelectCoinsETHBTC)
#             finalPriceBinanceETHBTC = priceOrderBinanceETHBTC + priceOfSelectCoinsETHBTC
#             print('-------------------------')
#             print(finalPriceBinanceETHBTC)
            
#             # print(finalPriceBinance)
            

#             amountOfMiddleCoinETHBTC[pairs] = (amountOfCoinToStillBuyETHBTC + amountOfCoinsBinanceETHBTC) * (1 - 0.001) 
            
#             break
        
#         else:
            
#             amountOfCoinsBinanceETHBTC += amountCoinBinanceETHBTC
#             priceOrderBinanceETHBTC += priceBinanceETHBTC    
# print('-------------------------')    
# print(amountOfMiddleCoinETHBTC)
# # this calcs for the final big coin, taking things back to the start and calcs the profit, also does trading fees
# profitOfBigCoinETHBTC = {}
# amountOfCoinsBinanceETHBTCF = 0
# priceOrderBinanceETHBTCF = 0
# # FOR BINANCE
# x = 0
# for pairs, vol in amountOfMiddleCoinETHBTC.items():
#     if len(pairs) == 7:
#         smallCoinNameETHBTC = pairs[:4] + 'BTC'
#     if len(pairs) == 6:
#         smallCoinNameETHBTC = pairs[:3] + 'BTC'
#     if len(pairs) == 8:
#         smallCoinNameETHBTC = pairs[:5] + 'BTC'
    
    
#     # print(smallCoinNameBNBETH)
#     amountOfCoinsBinanceETHBTCF = 0
    
    

#     priceOrderBinanceETHBTCF = 0
#     depthBinanceETHBTCF = bclient.get_order_book(symbol='{}'.format(smallCoinNameETHBTC), limit=10)

#     bbuyETHBTCF = depthBinanceETHBTCF['asks']


#     for orders in bbuyETHBTCF:
        
#         amountCoinBinanceETHBTCF = float(orders[1])
#         priceCoinBinanceETHBTCF = float(orders[0])
#         priceBinanceETHBTCF = priceCoinBinanceETHBTCF * amountCoinBinanceETHBTCF
        
#         amountCoinBeforeETHBTCF = amountOfCoinsBinanceETHBTCF + amountCoinBinanceETHBTCF
            
#         if amountCoinBeforeETHBTCF >= float(amountOfMiddleCoinETHBTC[pairs]):
#             x += 1
#             print('-------------------------')
#             print(smallCoinNameETHBTC)
#             print('-------------------------')
#             print(amountOfMiddleCoinETHBTC[pairs])
#             print(x)
#             print('-------------------------')
#             print('-------------------------')
#             print(priceOrderBinanceETHBTCF)
#             middleCoinLeftETHBTCF = float(amountOfMiddleCoinETHBTC[pairs]) - amountOfCoinsBinanceETHBTCF
#             print('-------------------------')
#             print(middleCoinLeftETHBTCF)
#             amountOfCoinToStillBuyETHBTCF = middleCoinLeftETHBTCF * priceCoinBinanceETHBTCF
#             print('-------------------------')
#             print(priceCoinBinanceETHBTCF)
            
#             # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
#             print('-------------------------')
#             print(amountOfCoinToStillBuyETHBTCF)
#             finalPriceBinanceETHBTCF = priceOrderBinanceETHBTCF + amountOfCoinToStillBuyETHBTCF
#             print('-------------------------')
#             print(finalPriceBinanceETHBTCF)
#             finalPriceATETHBTCF = finalPriceBinanceETHBTCF * (1 - 0.001)
#             print('-------------------------')
#             print(finalPriceATETHBTCF)
            
#             # print(finalPriceBinance)
            

#             profitOfBigCoinETHBTC[pairs] = finalPriceATETHBTCF
            
#             break
        
#         else:
            
#             amountOfCoinsBinanceETHBTCF += amountCoinBinanceETHBTCF
#             priceOrderBinanceETHBTCF += priceBinanceETHBTCF    
#             print('PRICEORDER: ', priceOrderBinanceETHBTCF)
# print('-------------------------')


# # maybe do a quick system which then double checks just that coin to make
# # sure the value of the coin has stayed the same b/f buying 


# #
# #
# #
# #
# #
# #







# printThisETHBTC = sorted(profitOfBigCoinETHBTC, key=profitOfBigCoinETHBTC.__getitem__, reverse=True)
# bestCoinETHBTC = str(printThisETHBTC[0])
# smallCoinNameTestETHBTC = bestCoinETHBTC.replace('ETH', 'BTC')


# print('-----------------------=-=-=')
# print(smallCoinNameTestETHBTC)

# amountOfMiddleCoinTestETHBTC = {}
# amountOfCoinsBinanceTestETHBTCVol = 0
    
    

# priceOrderBinanceTestETHBTCVol = 0
# depthBinanceTestETHBTCVol = bclient.get_order_book(symbol=str(bestCoinETHBTC), limit=10)

# bbuyTestETHBTCVol = depthBinanceTestETHBTCVol['bids']


# for orders in bbuyTestETHBTCVol:
        
#     amountCoinBinanceTestETHBTCVol = float(orders[1])
#     priceCoinBinanceTestETHBTCVol = float(orders[0])
#     priceBinanceTestETHBTCVol = priceCoinBinanceTestETHBTCVol * amountCoinBinanceTestETHBTCVol
        
#     priceBeforeTestETHBTCVol = priceOrderBinanceTestETHBTCVol + priceBinanceTestETHBTCVol
            
#     if priceBeforeTestETHBTCVol >= amountOfMinorCoin['ETHBTC']:
        
            
#         minorCoinLeftTestETHBTCVol = amountOfMinorCoin['ETHBTC'] - priceOrderBinanceTestETHBTCVol
            
#         amountOfCoinToStillBuyTestETHBTCVol = minorCoinLeftTestETHBTCVol / priceCoinBinanceTestETHBTCVol
            
#         priceOfSelectCoinsTestETHBTCVol = amountOfCoinToStillBuyTestETHBTCVol * priceCoinBinanceTestETHBTCVol
            
#         finalPriceBinanceTestETHBTCVol = priceOrderBinanceTestETHBTCVol + priceOfSelectCoinsTestETHBTCVol
           
            
#             # print(finalPriceBinance)
           

#         amountOfMiddleCoinTestETHBTC[bestCoinETHBTC] = (amountOfCoinToStillBuyTestETHBTCVol + amountOfCoinsBinanceTestETHBTCVol) * (1 - 0.001) 
            
#         break
        
#     else:
            
#         amountOfCoinsBinanceTestETHBTCVol += amountCoinBinanceTestETHBTCVol
#         priceOrderBinanceTestETHBTCVol += priceBinanceTestETHBTCVol    





# # ---------------------------------------------------Part 2

# # next it chekcs the coin again and then places a buy if above a couple percent


# amountOfCoinsBinanceTestETHBTC = 0
# priceOrderBinanceTestETHBTC = 0
# finalCoinETHBTC = {}
# depthBinanceTestETHBTC = bclient.get_order_book(symbol=str(smallCoinNameTestETHBTC), limit=10)
# bbuyTestETHBTC = depthBinanceTestETHBTC[asks]
# print('__________________________________________-')

# for orders in bbuyTestETHBTC:
#     amountCoinBinanceTestETHBTC = float(orders[1])
#     priceCoinBinanceTestETHBTC = float(orders[0])
#     priceBinanceTestETHBTC = priceCoinBinanceTestETHBTC * amountCoinBinanceTestETHBTC
#     amountCoinBeforeTestETHBTC = amountOfCoinsBinanceTestETHBTC + amountCoinBinanceTestETHBTC
#     print('AMOUNT ', amountCoinBeforeTestETHBTC)
           

#     if amountCoinBeforeTestETHBTC >= float(amountOfMiddleCoinTestETHBTC[bestCoinETHBTC]):
#         print(bbuyTestETHBTC)
#         print(amountOfMiddleCoinTestETHBTC[bestCoinETHBTC])
#         print(amountOfMiddleCoinETHBTC[bestCoinETHBTC])
    
        
        
        
#         middleCoinLeftTestETHBTC = float(amountOfMiddleCoinTestETHBTC[bestCoinETHBTC]) - amountOfCoinsBinanceTestETHBTC
#         print(amountOfCoinsBinanceTestETHBTC)
#         print(middleCoinLeftTestETHBTC)
        
#         amountOfCoinToStillBuyTestETHBTC = middleCoinLeftTestETHBTC * priceCoinBinanceTestETHBTC
#         print(amountOfCoinToStillBuyTestETHBTC)
            
#         # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
        
#         finalPriceBinanceTestETHBTC = priceOrderBinanceTestETHBTC + amountOfCoinToStillBuyTestETHBTC
#         print(finalPriceBinanceTestETHBTC)
#         print(priceOrderBinanceTestETHBTC)
        
#         finalPriceTestATETHBTC = finalPriceBinanceTestETHBTC * (1 - 0.001)
        
            
#             # print(finalPriceBinance)
            

#         finalCoinETHBTC[smallCoinNameTestETHBTC] = finalPriceTestATETHBTC
            

#         break
        
#     else:
            
#         amountOfCoinsBinanceTestETHBTC += amountCoinBinanceTestETHBTC
#         priceOrderBinanceTestETHBTC += priceBinanceTestETHBTC    
        


# finalCoinPercentageETHBTC = (finalCoinETHBTC[smallCoinNameTestETHBTC] - accountBalanceBinanceBitcoin) / accountBalanceBinanceBitcoin
# print('_________________________')
# print(finalCoinETHBTC)
# print(finalCoinPercentageETHBTC)
# print(profitOfBigCoinETHBTC[bestCoinETHBTC])
# if finalCoinPercentageETHBTC > 0.04:
#     # buy 3 way around.  Add a part which transfers USDT into the coin first so that my balance will be stable 
#     print('good op')


#     transaction = client.bclient.order_market_sell(symbol='ETHBTC', quantity=BALANCEFIX)
#                 # orders = client.get_active_orders('{}'.format(bestCoinETH))
            
#     if transaction['orderOid']:
#         print('next part')
#         rdnVarFinal = 3
#         print(transaction)  
#         orders = client.get_active_orders(str(bestCoinETH))
#         print(orders)
#         print('d')
#         # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
#         print('e')
#         time.sleep(1)
#         if orders['BUY']:
#             print('order not filled')
#             client.cancel_all_orders()
#         else:
#             print('order filled')
#             time.sleep(1)
#             transaction2 = bclient.order_market_sell(symbol=str(), quantity=BALANCEFIX)


    
    
    

    
    

    

    
# BTCUSDT BABY


amountOfMiddleCoinBTCUSDT = {}

for pairs in BTCUSDTSimilar:
    
    # print(pairs)
    
    amountOfCoinsBinanceBTCUSDT = 0
    
    

    priceOrderBinanceBTCUSDT = 0
    depthBinanceBTCUSDT = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

    bbuyBTCUSDT = depthBinanceBTCUSDT['bids']


    for orders in bbuyBTCUSDT:
        
        amountCoinBinanceBTCUSDT = float(orders[1])
        priceCoinBinanceBTCUSDT = float(orders[0])
        priceBinanceBTCUSDT = priceCoinBinanceBTCUSDT * amountCoinBinanceBTCUSDT
        
        priceBeforeBTCUSDT = priceOrderBinanceBTCUSDT + priceBinanceBTCUSDT
            
        if priceBeforeBTCUSDT >= amountOfMinorCoin['BTCUSDT']:
            x += 1
            print('-------------------------')
            print(x)
            minorCoinLeftBTCUSDT = amountOfMinorCoin['BTCUSDT'] - priceOrderBinanceBTCUSDT
            print('-------------------------')
            print(minorCoinLeftBTCUSDT)
            amountOfCoinToStillBuyBTCUSDT = minorCoinLeftBTCUSDT / priceCoinBinanceBTCUSDT
            print('-------------------------')
            print(amountOfCoinToStillBuyBTCUSDT)
            priceOfSelectCoinsBTCUSDT = amountOfCoinToStillBuyBTCUSDT * priceCoinBinanceBTCUSDT
            print('-------------------------')
            print(priceOfSelectCoinsBTCUSDT)
            finalPriceBinanceBTCUSDT = priceOrderBinanceBTCUSDT + priceOfSelectCoinsBTCUSDT
            print('-------------------------')
            print(finalPriceBinanceBTCUSDT)
            
            # print(finalPriceBinance)
            

            amountOfMiddleCoinBTCUSDT[pairs] = (amountOfCoinToStillBuyBTCUSDT + amountOfCoinsBinanceBTCUSDT) * (1 - 0.001) 
            
            break
        
        else:
            
            amountOfCoinsBinanceBTCUSDT += amountCoinBinanceBTCUSDT
            priceOrderBinanceBTCUSDT += priceBinanceBTCUSDT    
print('-------------------------')    
print(amountOfMiddleCoinBTCUSDT)
# this calcs for the final big coin, taking things back to the start and calcs the profit, also does trading fees
profitOfBigCoinBTCUSDT = {}
amountOfCoinsBinanceBTCUSDTF = 0
priceOrderBinanceBTCUSDTF = 0
# FOR BINANCE
x = 0
for pairs, vol in amountOfMiddleCoinBTCUSDT.items():
    if len(pairs) == 7:
        smallCoinNameBTCUSDT = pairs[:4] + 'USDT'
    if len(pairs) == 6:
        smallCoinNameBTCUSDT = pairs[:3] + 'USDT'
    if len(pairs) == 8:
        smallCoinNameBTCUSDT = pairs[:5] + 'USDT'
    
    
    # print(smallCoinNameBNBETH)
    amountOfCoinsBinanceBTCUSDTF = 0
    
    

    priceOrderBinanceBTCUSDTF = 0
    depthBinanceBTCUSDTF = bclient.get_order_book(symbol='{}'.format(smallCoinNameBTCUSDT), limit=10)

    bbuyBTCUSDTF = depthBinanceBTCUSDTF['asks']


    for orders in bbuyBTCUSDTF:
        
        amountCoinBinanceBTCUSDTF = float(orders[1])
        priceCoinBinanceBTCUSDTF = float(orders[0])
        priceBinanceBTCUSDTF = priceCoinBinanceBTCUSDTF * amountCoinBinanceBTCUSDTF
        
        amountCoinBeforeBTCUSDTF = amountOfCoinsBinanceBTCUSDTF + amountCoinBinanceBTCUSDTF
            
        if amountCoinBeforeBTCUSDTF >= float(amountOfMiddleCoinBTCUSDT[pairs]):
            x += 1
            print('-------------------------')
            print(smallCoinNameBTCUSDT)
            print('-------------------------')
            print(amountOfMiddleCoinBTCUSDT[pairs])
            print(x)
            print('-------------------------')
            print('-------------------------')
            print(priceOrderBinanceBTCUSDTF)
            middleCoinLeftBTCUSDTF = float(amountOfMiddleCoinBTCUSDT[pairs]) - amountOfCoinsBinanceBTCUSDTF
            print('-------------------------')
            print(middleCoinLeftBTCUSDTF)
            amountOfCoinToStillBuyBTCUSDTF = middleCoinLeftBTCUSDTF * priceCoinBinanceBTCUSDTF
            print('-------------------------')
            print(priceCoinBinanceBTCUSDTF)
            
            # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
            print('-------------------------')
            print(amountOfCoinToStillBuyBTCUSDTF)
            finalPriceBinanceBTCUSDTF = priceOrderBinanceBTCUSDTF + amountOfCoinToStillBuyBTCUSDTF
            print('-------------------------')
            print(finalPriceBinanceBTCUSDTF)
            finalPriceATBTCUSDTF = finalPriceBinanceBTCUSDTF * (1 - 0.001)
            print('-------------------------')
            print(finalPriceATBTCUSDTF)
            
            # print(finalPriceBinance)
            

            profitOfBigCoinBTCUSDT[pairs] = finalPriceATBTCUSDTF
            
            break
        
        else:
            
            amountOfCoinsBinanceBTCUSDTF += amountCoinBinanceBTCUSDTF
            priceOrderBinanceBTCUSDTF += priceBinanceBTCUSDTF    
            print('PRICEORDER: ', priceOrderBinanceBTCUSDTF)
print('-------------------------')


# maybe do a quick system which then double checks just that coin to make
# sure the value of the coin has stayed the same b/f buying 


#
#
#
#
#
#







printThisBTCUSDT = sorted(profitOfBigCoinBTCUSDT, key=profitOfBigCoinBTCUSDT.__getitem__, reverse=True)
bestCoinBTCUSDT = str(printThisBTCUSDT[0])
smallCoinNameTestBTCUSDT = bestCoinBTCUSDT.replace('BTC', 'USDT')


print('-----------------------=-=-=')
print(smallCoinNameTestBTCUSDT)

amountOfMiddleCoinTestBTCUSDT = {}
amountOfCoinsBinanceTestBTCUSDTVol = 0
    
    

priceOrderBinanceTestBTCUSDTVol = 0
depthBinanceTestBTCUSDTVol = bclient.get_order_book(symbol=str(bestCoinBTCUSDT), limit=10)

bbuyTestBTCUSDTVol = depthBinanceTestBTCUSDTVol['bids']


for orders in bbuyTestBTCUSDTVol:
        
    amountCoinBinanceTestBTCUSDTVol = float(orders[1])
    priceCoinBinanceTestBTCUSDTVol = float(orders[0])
    priceBinanceTestBTCUSDTVol = priceCoinBinanceTestBTCUSDTVol * amountCoinBinanceTestBTCUSDTVol
        
    priceBeforeTestBTCUSDTVol = priceOrderBinanceTestBTCUSDTVol + priceBinanceTestBTCUSDTVol
            
    if priceBeforeTestBTCUSDTVol >= amountOfMinorCoin['BTCUSDT']:
        
            
        minorCoinLeftTestBTCUSDTVol = amountOfMinorCoin['BTCUSDT'] - priceOrderBinanceTestBTCUSDTVol
            
        amountOfCoinToStillBuyTestBTCUSDTVol = minorCoinLeftTestBTCUSDTVol / priceCoinBinanceTestBTCUSDTVol
            
        priceOfSelectCoinsTestBTCUSDTVol = amountOfCoinToStillBuyTestBTCUSDTVol * priceCoinBinanceTestBTCUSDTVol
            
        finalPriceBinanceTestBTCUSDTVol = priceOrderBinanceTestBTCUSDTVol + priceOfSelectCoinsTestBTCUSDTVol
           
            
            # print(finalPriceBinance)
           

        amountOfMiddleCoinTestBTCUSDT[bestCoinBTCUSDT] = (amountOfCoinToStillBuyTestBTCUSDTVol + amountOfCoinsBinanceTestBTCUSDTVol) * (1 - 0.001) 
            
        break
        
    else:
            
        amountOfCoinsBinanceTestBTCUSDTVol += amountCoinBinanceTestBTCUSDTVol
        priceOrderBinanceTestBTCUSDTVol += priceBinanceTestBTCUSDTVol    





# ---------------------------------------------------Part 2

# next it chekcs the coin again and then places a buy if above a couple percent


amountOfCoinsBinanceTestBTCUSDT = 0
priceOrderBinanceTestBTCUSDT = 0
finalCoinBTCUSDT = {}
depthBinanceTestBTCUSDT = bclient.get_order_book(symbol=str(smallCoinNameTestBTCUSDT), limit=10)
bbuyTestBTCUSDT = depthBinanceTestBTCUSDT['asks']
print('__________________________________________-')

for orders in bbuyTestBTCUSDT:
    amountCoinBinanceTestBTCUSDT = float(orders[1])
    priceCoinBinanceTestBTCUSDT = float(orders[0])
    priceBinanceTestBTCUSDT = priceCoinBinanceTestBTCUSDT * amountCoinBinanceTestBTCUSDT
    amountCoinBeforeTestBTCUSDT = amountOfCoinsBinanceTestBTCUSDT + amountCoinBinanceTestBTCUSDT
    print('AMOUNT ', amountCoinBeforeTestBTCUSDT)
           

    if amountCoinBeforeTestBTCUSDT >= float(amountOfMiddleCoinTestBTCUSDT[bestCoinBTCUSDT]):
        print(bbuyTestBTCUSDT)
        print(amountOfMiddleCoinTestBTCUSDT[bestCoinBTCUSDT])
        print(amountOfMiddleCoinBTCUSDT[bestCoinBTCUSDT])
    
        
        
        
        middleCoinLeftTestBTCUSDT = float(amountOfMiddleCoinTestBTCUSDT[bestCoinBTCUSDT]) - amountOfCoinsBinanceTestBTCUSDT
        print(amountOfCoinsBinanceTestBTCUSDT)
        print(middleCoinLeftTestBTCUSDT)
        
        amountOfCoinToStillBuyTestBTCUSDT = middleCoinLeftTestBTCUSDT * priceCoinBinanceTestBTCUSDT
        print(amountOfCoinToStillBuyTestBTCUSDT)
            
        # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
        
        finalPriceBinanceTestBTCUSDT = priceOrderBinanceTestBTCUSDT + amountOfCoinToStillBuyTestBTCUSDT
        print(finalPriceBinanceTestBTCUSDT)
        print(priceOrderBinanceTestBTCUSDT)
        
        finalPriceTestATBTCUSDT = finalPriceBinanceTestBTCUSDT * (1 - 0.001)
        
            
            # print(finalPriceBinance)
            

        finalCoinBTCUSDT[smallCoinNameTestBTCUSDT] = finalPriceTestATBTCUSDT
            

        break
        
    else:
            
        amountOfCoinsBinanceTestBTCUSDT += amountCoinBinanceTestBTCUSDT
        priceOrderBinanceTestBTCUSDT += priceBinanceTestBTCUSDT   
        


finalCoinPercentageBTCUSDT = (finalCoinBTCUSDT[smallCoinNameTestBTCUSDT] - accountBalanceBinanceUSDT) / accountBalanceBinanceUSDT
print('_________________________')
print(finalCoinBTCUSDT)
print(finalCoinPercentageBTCUSDT)
print(profitOfBigCoinBTCUSDT[bestCoinBTCUSDT])
if finalCoinPercentageBTCUSDT > 0.04:
    # buy 3 way around.  Add a part which transfers USDT into the coin first so that my balance will be stable 
    print('good op')


    transactionBTCUSDT = client.bclient.order_market_sell(symbol='BNBETH', quantity=BALANCEFIX)
                # orders = client.get_active_orders('{}'.format(bestCoinETH))
            
    if transaction['orderOid']:
        print('next part')
        rdnVarFinal = 3
        print(transaction)  
        orders = client.get_active_orders(str(bestCoinETH))
        print(orders)
        print('d')
        # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
        print('e')
        time.sleep(1)
        if orders['BUY']:
            print('order not filled')
            client.cancel_all_orders()
        else:
            print('order filled')
            time.sleep(1)
            transaction2BTCUSDT = bclient.order_market_sell(symbol=str(), quantity=BALANCEFIX)


    
    
    

    
 

# ETHUSDT

amountOfMiddleCoinETHUSDT = {}
amountOfCoinsBinanceETHUSDT = 0
priceOrderBinanceETHUSDT = 0
# FOR BINANCE 
x = 0
for pairs in ETHUSDTSimilar:
    
    # print(pairs)
    
    amountOfCoinsBinanceETHUSDT = 0
    
    

    priceOrderBinanceETHUSDT = 0
    depthBinanceETHUSDT = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

    bbuyETHUSDT = depthBinanceETHUSDT['bids']


    for orders in bbuyETHUSDT:
        
        amountCoinBinanceETHUSDT = float(orders[1])
        priceCoinBinanceETHUSDT = float(orders[0])
        priceBinanceETHUSDT = priceCoinBinanceETHUSDT * amountCoinBinanceETHUSDT
        
        priceBeforeETHUSDT = priceOrderBinanceETHUSDT + priceBinanceETHUSDT
            
        if priceBeforeETHUSDT >= amountOfMinorCoin['ETHUSDT']:
            x += 1
            print('-------------------------')
            print(x)
            minorCoinLeftETHUSDT = amountOfMinorCoin['ETHUSDT'] - priceOrderBinanceETHUSDT
            print('-------------------------')
            print(minorCoinLeftETHUSDT)
            amountOfCoinToStillBuyETHUSDT = minorCoinLeftETHUSDT / priceCoinBinanceETHUSDT
            print('-------------------------')
            print(amountOfCoinToStillBuyETHUSDT)
            priceOfSelectCoinsETHUSDT = amountOfCoinToStillBuyETHUSDT * priceCoinBinanceETHUSDT
            print('-------------------------')
            print(priceOfSelectCoinsETHUSDT)
            finalPriceBinanceETHUSDT = priceOrderBinanceETHUSDT + priceOfSelectCoinsETHUSDT
            print('-------------------------')
            print(finalPriceBinanceETHUSDT)
            
            # print(finalPriceBinance)
            

            amountOfMiddleCoinETHUSDT[pairs] = (amountOfCoinToStillBuyETHUSDT + amountOfCoinsBinanceETHUSDT) * (1 - 0.001) 
            
            break
        
        else:
            
            amountOfCoinsBinanceETHUSDT += amountCoinBinanceETHUSDT
            priceOrderBinanceETHUSDT += priceBinanceETHUSDT   
print('-------------------------')    
print(amountOfMiddleCoinETHUSDT)
# this calcs for the final big coin, taking things back to the start and calcs the profit, also does trading fees
profitOfBigCoinETHUSDT = {}
amountOfCoinsBinanceETHUSDTF = 0
priceOrderBinanceETHUSDTF = 0
# FOR BINANCE
x = 0
for pairs, vol in amountOfMiddleCoinETHUSDT.items():
    if len(pairs) == 7:
        smallCoinNameETHUSDT = pairs[:4] + 'USDT'
    if len(pairs) == 6:
        smallCoinNameETHUSDT = pairs[:3] + 'USDT'
    if len(pairs) == 8:
        smallCoinNameETHUSDT = pairs[:5] + 'USDT'
    
    
    # print(smallCoinNameBNBETH)
    amountOfCoinsBinanceETHUSDTF = 0
    
    

    priceOrderBinanceETHUSDTF = 0
    depthBinanceETHUSDTF = bclient.get_order_book(symbol='{}'.format(smallCoinNameETHUSDT), limit=10)

    bbuyETHUSDTF = depthBinanceETHUSDTF['asks']


    for orders in bbuyETHUSDTF:
        
        amountCoinBinanceETHUSDTF = float(orders[1])
        priceCoinBinanceETHUSDTF = float(orders[0])
        priceBinanceETHUSDTF = priceCoinBinanceETHUSDTF * amountCoinBinanceETHUSDTF
        
        amountCoinBeforeETHUSDTF = amountOfCoinsBinanceETHUSDTF + amountCoinBinanceETHUSDTF
            
        if amountCoinBeforeETHUSDTF >= float(amountOfMiddleCoinETHUSDT[pairs]):
            x += 1
            print('-------------------------')
            print(smallCoinNameETHUSDT)
            print('-------------------------')
            print(amountOfMiddleCoinETHUSDT[pairs])
            print(x)
            print('-------------------------')
            print('-------------------------')
            print(priceOrderBinanceETHUSDTF)
            middleCoinLeftETHUSDTF = float(amountOfMiddleCoinETHUSDT[pairs]) - amountOfCoinsBinanceETHUSDTF
            print('-------------------------')
            print(middleCoinLeftETHUSDTF)
            amountOfCoinToStillBuyETHUSDTF = middleCoinLeftETHUSDTF * priceCoinBinanceETHUSDTF
            print('-------------------------')
            print(priceCoinBinanceETHUSDTF)
            
            # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
            print('-------------------------')
            print(amountOfCoinToStillBuyETHUSDTF)
            finalPriceBinanceETHUSDTF = priceOrderBinanceETHUSDTF + amountOfCoinToStillBuyETHUSDTF
            print('-------------------------')
            print(finalPriceBinanceETHUSDTF)
            finalPriceATETHUSDTF = finalPriceBinanceETHUSDTF * (1 - 0.001)
            print('-------------------------')
            print(finalPriceATETHUSDTF)
            
            # print(finalPriceBinance)
            

            profitOfBigCoinETHUSDT[pairs] = finalPriceATETHUSDTF
            
            break
        
        else:
            
            amountOfCoinsBinanceETHUSDTF += amountCoinBinanceETHUSDTF
            priceOrderBinanceETHUSDTF += priceBinanceETHUSDTF    
            print('PRICEORDER: ', priceOrderBinanceETHUSDTF)
print('-------------------------')


# maybe do a quick system which then double checks just that coin to make
# sure the value of the coin has stayed the same b/f buying 


#
#
#
#
#
#







printThis = sorted(profitOfBigCoinETHUSDT, key=profitOfBigCoinETHUSDT.__getitem__, reverse=True)
bestCoinETHUSDT = str(printThis[0])
smallCoinNameTestETHUSDT = bestCoinETHUSDT.replace('ETH', 'USDT')


print('-----------------------=-=-=')
print(smallCoinNameTestETHUSDT)

amountOfMiddleCoinTestETHUSDT = {}
amountOfCoinsBinanceTestETHUSDTVol = 0
    
    

priceOrderBinanceTestETHUSDTVol = 0
depthBinanceTestETHUSDTVol = bclient.get_order_book(symbol=str(bestCoinETHUSDT), limit=10)

bbuyTestETHUSDTVol = depthBinanceTestETHUSDTVol['bids']


for orders in bbuyTestETHUSDTVol:
        
    amountCoinBinanceTestETHUSDTVol = float(orders[1])
    priceCoinBinanceTestETHUSDTVol = float(orders[0])
    priceBinanceTestETHUSDTVol = priceCoinBinanceTestETHUSDTVol * amountCoinBinanceTestETHUSDTVol
        
    priceBeforeTestETHUSDTVol = priceOrderBinanceTestETHUSDTVol + priceBinanceTestETHUSDTVol
            
    if priceBeforeTestETHUSDTVol >= amountOfMinorCoin['ETHUSDT']:
        
            
        minorCoinLeftTestETHUSDTVol = amountOfMinorCoin['ETHUSDT'] - priceOrderBinanceTestETHUSDTVol
            
        amountOfCoinToStillBuyTestETHUSDTVol = minorCoinLeftTestETHUSDTVol / priceCoinBinanceTestETHUSDTVol
            
        priceOfSelectCoinsTestETHUSDTVol = amountOfCoinToStillBuyTestETHUSDTVol * priceCoinBinanceTestETHUSDTVol
            
        finalPriceBinanceTestETHUSDTVol = priceOrderBinanceTestETHUSDTVol + priceOfSelectCoinsTestETHUSDTVol
           
            
            # print(finalPriceBinance)
           

        amountOfMiddleCoinTestETHUSDT[bestCoinETHUSDT] = (amountOfCoinToStillBuyTestETHUSDTVol + amountOfCoinsBinanceTestETHUSDTVol) * (1 - 0.001) 
            
        break
        
    else:
            
        amountOfCoinsBinanceTestBNBETHVol += amountCoinBinanceTestBNBETHVol
        priceOrderBinanceTestBNBETHVol += priceBinanceTestBNBETHVol    





# ---------------------------------------------------Part 2

# next it chekcs the coin again and then places a buy if above a couple percent


amountOfCoinsBinanceTestETHUSDT = 0
priceOrderBinanceTestETHUSDT = 0
finalCoinETHUSDT = {}
depthBinanceTestETHUSDT = bclient.get_order_book(symbol=str(smallCoinNameTestETHUSDT), limit=10)
bbuyTestETHUSDT = depthBinanceTestETHUSDT['asks']
print('__________________________________________-')

for orders in bbuyTestETHUSDT:
    amountCoinBinanceTestETHUSDT = float(orders[1])
    priceCoinBinanceTestETHUSDT = float(orders[0])
    priceBinanceTestETHUSDT = priceCoinBinanceTestETHUSDT * amountCoinBinanceTestETHUSDT
    amountCoinBeforeTestETHUSDT = amountOfCoinsBinanceTestETHUSDT + amountCoinBinanceTestETHUSDT
    print('AMOUNT ', amountCoinBeforeTestETHUSDT)
           

    if amountCoinBeforeTestETHUSDT >= float(amountOfMiddleCoinTestETHUSDT[bestCoinETHUSDT]):
        print(bbuyTestETHUSDT)
        print(amountOfMiddleCoinTestETHUSDT[bestCoinETHUSDT])
        print(amountOfMiddleCoinETHUSDT[bestCoinETHUSDT])
    
        
        
        
        middleCoinLeftTestETHUSDT = float(amountOfMiddleCoinTestETHUSDT[bestCoinETHUSDT]) - amountOfCoinsBinanceTestETHUSDT
        print(amountOfCoinsBinanceTestETHUSDT)
        print(middleCoinLeftTestETHUSDT)
        
        amountOfCoinToStillBuyTestETHUSDT = middleCoinLeftTestETHUSDT * priceCoinBinanceTestETHUSDT
        print(amountOfCoinToStillBuyTestBNBETH)
            
        # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
        
        finalPriceBinanceTestETHUSDT = priceOrderBinanceTestETHUSDT + amountOfCoinToStillBuyTestETHUSDT
        print(finalPriceBinanceTestETHUSDT)
        print(priceOrderBinanceTestETHUSDT)
        
        finalPriceTestATETHUSDT = finalPriceBinanceTestETHUSDT * (1 - 0.001)
        
            
            # print(finalPriceBinance)
            

        finalCoinETHUSDT[smallCoinNameTestETHUSDT] = finalPriceTestATETHUSDT
            

        break
        
    else:
            
        amountOfCoinsBinanceTestETHUSDT += amountCoinBinanceTestETHUSDT
        priceOrderBinanceTestETHUSDT += priceBinanceTestETHUSDT    
        


finalCoinPercentageETHUSDT = (finalCoinETHUSDT[smallCoinNameTestETHUSDT] - accountBalanceBinanceUSDT) / accountBalanceBinanceUSDT
print('_________________________')
print(finalCoinETHUSDT)
print(finalCoinPercentageETHUSDT)
print(profitOfBigCoinETHUSDT[bestCoinETHUSDT])
if finalCoinPercentageETHUSDT > 0.04:
    # buy 3 way around.  Add a part which transfers USDT into the coin first so that my balance will be stable 
    print('good op')


    transactionETHUSDT = client.bclient.order_market_sell(symbol='ETHUSDT', quantity=BALANCEFIX)
                # orders = client.get_active_orders('{}'.format(bestCoinETH))
            
    if transaction['orderOid']:
        print('next part')
        rdnVarFinal = 3
        print(transaction)  
        orders = client.get_active_orders(str(bestCoinETH))
        print(orders)
        print('d')
        # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
        print('e')
        time.sleep(1)
        if orders['BUY']:
            print('order not filled')
            client.cancel_all_orders()
        else:
            print('order filled')
            time.sleep(1)
            transaction2ETHUSDT = bclient.order_market_sell(symbol=str(), quantity=BALANCEFIX)


    
    
    

    
    

    

    
# BNBUSDT

amountOfMiddleCoinBNBUSDT = {}
amountOfCoinsBinanceBNBUSDT = 0
priceOrderBinanceBNBUSDT = 0
# FOR BINANCE 
x = 0
for pairs in BNBUSDTSimilar:
    
    # print(pairs)
    
    amountOfCoinsBinanceBNBUSDT = 0
    
    

    priceOrderBinanceBNBUSDT = 0
    depthBinanceBNBUSDT = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

    bbuyBNBUSDT = depthBinanceBNBUSDT['bids']


    for orders in bbuyBNBUSDT:
        
        amountCoinBinanceBNBUSDT = float(orders[1])
        priceCoinBinanceBNBUSDT = float(orders[0])
        priceBinanceBNBUSDT = priceCoinBinanceBNBUSDT * amountCoinBinanceBNBUSDT
        
        priceBeforeBNBUSDT = priceOrderBinanceBNBUSDT+ priceBinanceBNBUSDT
            
        if priceBeforeBNBUSDT >= amountOfMinorCoin['BNBUSDT']:
            x += 1
            print('-------------------------')
            print(x)
            minorCoinLeftBNBUSDT = amountOfMinorCoin['BNBUSDT'] - priceOrderBinanceBNBUSDT
            print('-------------------------')
            print(minorCoinLeftBNBUSDT)
            amountOfCoinToStillBuyBNBUSDT = minorCoinLeftBNBUSDT / priceCoinBinanceBNBUSDT
            print('-------------------------')
            print(amountOfCoinToStillBuyBNBUSDT)
            priceOfSelectCoinsBNBUSDT = amountOfCoinToStillBuyBNBUSDT * priceCoinBinanceBNBUSDT
            print('-------------------------')
            print(priceOfSelectCoinsBNBUSDT)
            finalPriceBinanceBNBUSDT = priceOrderBinanceBNBUSDT + priceOfSelectCoinsBNBUSDT
            print('-------------------------')
            print(finalPriceBinanceBNBUSDT)
            
            # print(finalPriceBinance)
            

            amountOfMiddleCoinBNBUSDT[pairs] = (amountOfCoinToStillBuyBNBUSDT + amountOfCoinsBinanceBNBUSDT) * (1 - 0.001) 
            
            break
        
        else:
            
            amountOfCoinsBinanceBNBUSDT += amountCoinBinanceBNBUSDT
            priceOrderBinanceBNBUSDT += priceBinanceBNBUSDT    
print('-------------------------')    
print(amountOfMiddleCoinBNBUSDT)
# this calcs for the final big coin, taking things back to the start and calcs the profit, also does trading fees
profitOfBigCoinBNBUSDT = {}
amountOfCoinsBinanceBNBUSDTF = 0
priceOrderBinanceBNBUSDTF = 0
# FOR BINANCE
x = 0
for pairs, vol in amountOfMiddleCoinBNBUSDT.items():
    if len(pairs) == 7:
        smallCoinNameBNBUSDT = pairs[:4] + 'USDT'
    if len(pairs) == 6:
        smallCoinNameBNBUSDT = pairs[:3] + 'USDT'
    if len(pairs) == 8:
        smallCoinNameBNBUSDT = pairs[:5] + 'USDT'
    
    
    # print(smallCoinNameBNBETH)
    amountOfCoinsBinanceBNBUSDTF = 0
    
    

    priceOrderBinanceBNBUSDTF = 0
    depthBinanceBNBUSDTF = bclient.get_order_book(symbol='{}'.format(smallCoinNameBNBUSDT), limit=10)

    bbuyBNBUSDTF = depthBinanceBNBUSDTF['asks']


    for orders in bbuyBNBUSDTF:
        
        amountCoinBinanceBNBUSDTF = float(orders[1])
        priceCoinBinanceBNBUSDTF = float(orders[0])
        priceBinanceBNBUSDTF = priceCoinBinanceBNBUSDTF * amountCoinBinanceBNBUSDTF
        
        amountCoinBeforeBNBUSDTF = amountOfCoinsBinanceBNBUSDTF + amountCoinBinanceBNBUSDTF
            
        if amountCoinBeforeBNBUSDTF >= float(amountOfMiddleCoinBNBUSDT[pairs]):
            x += 1
            print('-------------------------')
            print(smallCoinNameBNBUSDT)
            print('-------------------------')
            print(amountOfMiddleCoinBNBUSDT[pairs])
            print(x)
            print('-------------------------')
            print('-------------------------')
            print(priceOrderBinanceBNBUSDTF)
            middleCoinLeftBNBUSDTF = float(amountOfMiddleCoinBNBUSDT[pairs]) - amountOfCoinsBinanceBNBUSDTF
            print('-------------------------')
            print(middleCoinLeftBNBUSDTF)
            amountOfCoinToStillBuyBNBUSDTF = middleCoinLeftBNBUSDTF * priceCoinBinanceBNBUSDTF
            print('-------------------------')
            print(priceCoinBinanceBNBUSDTF)
            
            # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
            print('-------------------------')
            print(amountOfCoinToStillBuyBNBUSDTF)
            finalPriceBinanceBNBUSDTF = priceOrderBinanceBNBUSDTF + amountOfCoinToStillBuyBNBUSDTF
            print('-------------------------')
            print(finalPriceBinanceBNBUSDTF)
            finalPriceATBNBUSDTF = finalPriceBinanceBNBUSDTF * (1 - 0.001)
            print('-------------------------')
            print(finalPriceATBNBUSDTF)
            
            # print(finalPriceBinance)
            

            profitOfBigCoinBNBUSDT[pairs] = finalPriceATBNBUSDTF
            
            break
        
        else:
            
            amountOfCoinsBinanceBNBUSDTF += amountCoinBinanceBNBUSDTF
            priceOrderBinanceBNBUSDTF += priceBinanceBNBUSDTF    
            print('PRICEORDER: ', priceOrderBinanceBNBUSDTF)
print('-------------------------')


# maybe do a quick system which then double checks just that coin to make
# sure the value of the coin has stayed the same b/f buying 


#
#
#
#
#
#







printThisBNBUSDT = sorted(profitOfBigCoinBNBUSDT, key=profitOfBigCoinBNBUSDT.__getitem__, reverse=True)
bestCoinBNBUSDT = str(printThisBNBUSDT[0])
smallCoinNameTestBNBUSDT = bestCoinBNBUSDT.replace('BNB', 'USDT')


print('-----------------------=-=-=')
print(smallCoinNameTestBNBUSDT)

amountOfMiddleCoinTestBNBUSDT = {}
amountOfCoinsBinanceTestBNBUSDTVol = 0
    
    

priceOrderBinanceTestBNBUSDTVol = 0
depthBinanceTestBNBUSDTVol = bclient.get_order_book(symbol=str(bestCoinBNBUSDT), limit=10)

bbuyTestBNBUSDTVol = depthBinanceTestBNBUSDTVol['bids']


for orders in bbuyTestBNBUSDTVol:
        
    amountCoinBinanceTestBNBUSDTVol = float(orders[1])
    priceCoinBinanceTestBNBUSDTVol = float(orders[0])
    priceBinanceTestBNBUSDTVol = priceCoinBinanceTestBNBUSDTVol * amountCoinBinanceTestBNBUSDTVol
        
    priceBeforeTestBNBUSDTVol = priceOrderBinanceTestBNBUSDTVol + priceBinanceTestBNBUSDTVol
            
    if priceBeforeTestBNBUSDTVol >= amountOfMinorCoin['BNBUSDT']:
        
            
        minorCoinLeftTestBNBUSDTVol = amountOfMinorCoin['BNBUSDT'] - priceOrderBinanceTestBNBUSDTVol
            
        amountOfCoinToStillBuyTestBNBUSDTVol = minorCoinLeftTestBNBUSDTVol / priceCoinBinanceTestBNBUSDTVol
            
        priceOfSelectCoinsTestBNBUSDTVol = amountOfCoinToStillBuyTestBNBUSDTVol * priceCoinBinanceTestBNBUSDTVol
            
        finalPriceBinanceTestBNBUSDTVol = priceOrderBinanceTestBNBUSDTVol + priceOfSelectCoinsTestBNBUSDTVol
           
            
            # print(finalPriceBinance)
           

        amountOfMiddleCoinTestBNBUSDT[bestCoinBNBUSDT] = (amountOfCoinToStillBuyTestBNBUSDTVol + amountOfCoinsBinanceTestBNBUSDTVol) * (1 - 0.001) 
            
        break
        
    else:
            
        amountOfCoinsBinanceTestBNBUSDTVol += amountCoinBinanceTestBNBUSDTVol
        priceOrderBinanceTestBNBUSDTVol += priceBinanceTestBNBUSDTVol    





# ---------------------------------------------------Part 2

# next it chekcs the coin again and then places a buy if above a couple percent


amountOfCoinsBinanceTestBNBUSDT = 0
priceOrderBinanceTestBNBUSDT = 0
finalCoinBNBUSDT = {}
depthBinanceTestBNBUSDT = bclient.get_order_book(symbol=str(smallCoinNameTestBNBUSDT), limit=10)
bbuyTestBNBUSDT = depthBinanceTestBNBUSDT['asks']
print('__________________________________________-')

for orders in bbuyTestBNBUSDT:
    amountCoinBinanceTestBNBUSDT = float(orders[1])
    priceCoinBinanceTestBNBUSDT = float(orders[0])
    priceBinanceTestBNBUSDT = priceCoinBinanceTestBNBUSDT * amountCoinBinanceTestBNBUSDT
    amountCoinBeforeTestBNBUSDT = amountOfCoinsBinanceTestBNBUSDT + amountCoinBinanceTestBNBUSDT
    print('AMOUNT ', amountCoinBeforeTestBNBUSDT)
           

    if amountCoinBeforeTestBNBUSDT >= float(amountOfMiddleCoinTestBNBUSDT[bestCoinBNBUSDT]):
        print(bbuyTestBNBUSDT)
        print(amountOfMiddleCoinTestBNBUSDT[bestCoinBNBUSDT])
        print(amountOfMiddleCoinBNBUSDT[bestCoinBNBUSDT])
    
        
        
        
        middleCoinLeftTestBNBUSDT = float(amountOfMiddleCoinTestBNBUSDT[bestCoinBNBUSDT]) - amountOfCoinsBinanceTestBNBUSDT
        print(amountOfCoinsBinanceTestBNBUSDT)
        print(middleCoinLeftTestBNBUSDT)
        
        amountOfCoinToStillBuyTestBNBUSDT = middleCoinLeftTestBNBUSDT * priceCoinBinanceTestBNBUSDT
        print(amountOfCoinToStillBuyTestBNBUSDT)
            
        # priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF
        
        finalPriceBinanceTestBNBUSDT = priceOrderBinanceTestBNBUSDT + amountOfCoinToStillBuyTestBNBUSDT
        print(finalPriceBinanceTestBNBUSDT)
        print(priceOrderBinanceTestBNBUSDT)
        
        finalPriceTestATBNBUSDT = finalPriceBinanceTestBNBUSDT * (1 - 0.001)
        
            
            # print(finalPriceBinance)
            

        finalCoinBNBUSDT[smallCoinNameTestBNBUSDT] = finalPriceTestATBNBUSDT
            

        break
        
    else:
            
        amountOfCoinsBinanceTestBNBUSDT += amountCoinBinanceTestBNBUSDT
        priceOrderBinanceTestBNBUSDT += priceBinanceTestBNBUSDT    
        


finalCoinPercentageBNBUSDT = (finalCoinBNBUSDT[smallCoinNameTestBNBUSDT] - accountBalanceBinanceUSDT) / accountBalanceBinanceUSDT
print('_________________________')
print(finalCoinBNBUSDT)
print(finalCoinPercentageBNBUSDT)
print(profitOfBigCoinBNBUSDT[bestCoinBNBUSDT])
if finalCoinPercentageBNBUSDT > 0.04:
    # buy 3 way around.  Add a part which transfers USDT into the coin first so that my balance will be stable 
    print('good op')


    transactionBNBUSDT = client.bclient.order_market_sell(symbol='BNBUSDT', quantity=BALANCEFIX)
                # orders = client.get_active_orders('{}'.format(bestCoinETH))
            
    if transaction['orderOid']:
        print('next part')
        rdnVarFinal = 3
        print(transaction)  
        orders = client.get_active_orders(str(bestCoinETH))
        print(orders)
        print('d')
        # randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
        print('e')
        time.sleep(1)
        if orders['BUY']:
            print('order not filled')
            client.cancel_all_orders()
        else:
            print('order filled')
            time.sleep(1)
            transaction2BNBUSDT = bclient.order_market_sell(symbol=str(), quantity=BALANCEFIX)


    
    
    

    


# In[ ]:


lol = 1.0
print(len(str(lol)))


# In[25]:


while True:
    
    try:
        watchlol()
        
    except:
        time.sleep(10)
        break


# In[60]:


bestCoinFormer = 'DENTETH'
bestCoinFirstThree = 'DENT'
differenceDictVolActual = {'DENTETH': 4}
balanceBinanceBefore = bclient.get_asset_balance(asset=str(bestCoinFirstThree))['free']   

vol = float(differenceDictVolActual[bestCoinFormer])
buyPrice = {'DENTETH': 0.0000055}
buyPriceFinal = float(buyPrice[bestCoinFormer])
print(buyPriceFinal)
print(vol)
    
bestCoinETH = 'DENT-ETH'

            # client.create_buy_order('{}'.format(bestCoinETH), '{}'.format(float(priceOfCoinBuy)), '{}'.format(float(differenceDictVol[bestCoinFormer])))
transaction = client.create_buy_order(str(bestCoinETH), str(buyPriceFinal), str(vol))

