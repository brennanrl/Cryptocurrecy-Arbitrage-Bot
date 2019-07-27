
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

bclient = BinanceClient('wZUkR3OrwI953kvURKvRXiwTT41xT0Qsh1G7UfB6rz5kbGM0t9qspLAYaUCpfk7z', 'ybvMtTm4PeOGT0bJ5CrQugI5Wpdi2OcvaIoB0wAD462lekazGP0wRirDXL5kIbJM')


# In[4]:


# KUCOIN
currencies = client.get_currencies()

# orders = client.get_buy_orders('ETH-BTC', limit=50)
# sellorders = client.get_sell_orders('ETH-BTC', limit=50)

# account balance
userFee = 0.002
accountBalanceKucoin =  1 * (1 - userFee)
accountBalanceKucoinBTAX = 1
accountBalanceKucoinBTC = (1 / 9) * (1- userFee)
FixedAccountBalanceKucoin = 1.5 
# accountBalanceKucoin = client.get_coin_balance('ETH') 


# In[5]:


# BINANCE
depth = bclient.get_order_book(symbol='ETHBTC')


# In[6]:


print(orders)
print(sellorders)
print(depth)


# In[ ]:


coins = client.get_trading_symbols() # get all kucoin prices
prices = bclient.get_all_tickers() # get all binance prices


# In[ ]:


kucoinDict = {} # create a dictionary

for coin in coins:
    coinsymbol = coin['symbol']
    coinsymbol = coinsymbol.replace('-', '') # we need to remove dash to ocmpare to binance
    lastDeal = coin['lastDealPrice']
    kucoinDict[coinsymbol] = lastDeal # add to the dict to compare binance and kucoin

        
print(kucoinDict['ENJETH'])


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

print(binancePriceDict['ENJETH'])


# In[ ]:


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
                'SNTETH': 20, 'WTCETH': 0.1, 'NANOETH': 0.5, 'DOCKETH': 20, 'VETETH': 9999999999, 'ETHETH': 999999,
                'POLYETH': 3}
coinFeesBTC =  {'RPXBTC': 1, 'ARNBTC': 1.8, 'OMGBTC': 0.1, 'GASBTC': 0, 'MTHBTC': 10, 'GVTBTC': 0.1,
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
coinFeesUSDT = {'NEOUSDT': 0, 'LTCUSDT': 0.001, 'EOSUSDT': 0.5}


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


# In[14]:


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


# In[9]:


# to withdrawl from kucoin & buy from kucoin
# this is the important cell, all code is compiled into this so that i get up to date info
import time



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




def watch():
    
    
    # this gets the prices
    coins = client.get_trading_symbols() # get all kucoin prices
    prices = bclient.get_all_tickers() # get all binance prices


    # this makes a dict of all kucoin coins
    kucoinDict = {} # create a dictionary

    for coin in coins:
        coinsymbol = coin['symbol']
        coinsymbol = coinsymbol.replace('-', '') # we need to remove dash to ocmpare to binance
        lastDeal = coin['lastDealPrice']
        kucoinDict[coinsymbol] = lastDeal # add to the dict to compare binance and kucoin

    
    # this makes a dict of all binance coins

    binancePriceDict = {}

    for price in prices:
        bsymbol = price['symbol']
        bprice = price['price']
        if bsymbol in kucoinDict:
            binancePriceDict[bsymbol] = bprice


    # makes a dict of all things that are the same

    differenceDictlol = {}

    for price in prices:
        bsymbol = price['symbol']
        bprice = price['price']
        if bsymbol in kucoinDict:
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
    differenceDict = {}

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
        if coins in coinFeesDict:
            coinPriceKucoin = float(kucoinDict[coins])
            amountOfCoinsToBuy = differenceDictVol[coins]
            # nameWithoutBigCoin = coins.replace('ETH', '').replace('BTC', '').replace('USDT', '')
            # print(nameWithoutBigCoin)
            # if '' and 'ETH' and 'USDT' and 'BTC' not in nameWithoutBigCoin:
            withdrawlFee = coinFeesDict[coins]
    
    
            priceToWithdrawl = withdrawlFee * coinPriceKucoin
    
    
            finalProfit = prices - priceToWithdrawl
    
            finalCoinsAfterBaseFee[coins] = finalProfit


    
    # order all difference coins by how much profit they make. best coin is named bestCoin, use that in all further operations for the final part

    coinsAndStuff = sorted(finalCoinsAfterBaseFee, key=finalCoinsAfterBaseFee.__getitem__, reverse=True)
    print(coinsAndStuff)
    bestCoinFormer = coinsAndStuff[0]
    bestCoinFirstThree = bestCoinFormer[:3]
    bestCoin = {}
    bestCoin[bestCoinFormer] = finalCoinsAfterBaseFee[bestCoinFormer] / accountBalanceKucoin
    bestCoinPercentage = bestCoin[bestCoinFormer]
    bestCoinETH = []

    for coins in bestCoin:
    
        if len(coins) == 7:
            newCoinNameETH = coins[:4] + '-' + coins[4:]
    
        if len(coins) == 6:
            newCoinNameETH = coins[:3] + '-' + coins[3:]
    
        bestCoinETH.append(newCoinName)

    # print('____________-----')
    print(bestCoin)




    
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

            
            
    if bestCoinPercentage > 0.01:
        print("BUY KUCOIN SELL BINANCE")
            
        
        try:
            # transaction = client.create_buy_order('{}'.format(bestCoinETH), 'BEST_PRICE', differenceDictVol[bestCoinFormer])
            print(transaction)   
                
                    
           
            orders = client.get_active_orders('{}'.format(bestCoinETH))
            
            time.sleep(1)
                
                
            
        except:
            print("PROBLEM WITH TRADE")
            
            rdnVar = 6
            
            
        if rdnVar != 6:
            for x in range(0, 11):
                    
                    
                    if orders['BUY']:
                        
                        print('order not filled')
                        
                        x += 1
                        
                        time.sleep(1)
                        
                
                        
                        
                        if x == 10:
                            client.cancel_all_orders()
        
                    else:
                
                
                   
                    
                        print("ORDER FILLED")
                    
                        balanceETHBinance = bclient.get_asset_balance(asset='ETH')
                        randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree))) 
                    
                        maketrade(bestCoinFormer, balanceETHBinance, randomCoinBalance)

            
            
# balanceETHBinance = bclient.get_asset_balance(asset='ETH')
def maketrade(x, y, z):
    randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree)))
    if randomCoinBalance > 0:
        address = bclient.get_deposit_address(asset='{}'.format(bestCoinFirstThree))
        client.create_withdrawal('{}'.format(bestCoinFirstThree), float(dashbalance['balance']),
                                 str(address['address']))
        print('WITHDRAWING')
        
        
    while True:
       
    
        
        try:
            orderBinance = bclient.order_market_sell(symbol='{}'.format(bestCoinFormer), quantity=differenceDictVol[bestCoinFormer])
            time.sleep(5)
            balance = print('COIN SOLD ON BINANCE FOR: {}'.format(balanceETHBinance))
            return balance
            break
        except:
            print('COINS NOT SOLD YET')
        
            continue
    
        

# tom, do the safety stuff like checking if buy went through on kucoin and if the coins were sent properly, and if they sold on binance


# In[10]:


# dont run
# input = input('Press q to quit: ')
i = 0
while True:
    
#     if input == 'q':
#         break
    
    # i += 1
    try:
        # print('IT: {}'.format(i))
        watch()
        # watchBTC()
    except:
        time.sleep(10)
        continue


# In[11]:


# to withdrawl from kucoin & buy from kucoin
# this is the important cell, all code is compiled into this so that i get up to date info
#BTC
import time



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




def watchBTC():
    
    
    # this gets the prices
    coinsBTC = client.get_trading_symbols() # get all kucoin prices
    pricesBTC = bclient.get_all_tickers() # get all binance prices

    
    # this makes a dict of all kucoin coins
    kucoinDictBTC = {} # create a dictionary

    for coin in coinsBTC:
        coinsymbolBTC = coin['symbol']
        coinsymbolBTC = coinsymbolBTC.replace('-', '') # we need to remove dash to ocmpare to binance
        lastDealBTC = coin['lastDealPrice']
        kucoinDictBTC[coinsymbolBTC] = lastDealBTC # add to the dict to compare binance and kucoin

    
    # this makes a dict of all binance coins

    

    
    # makes a dict of all things that are the same

    differenceDictlolBTC = {}

    for priceBTC in pricesBTC:
        bsymbolBTC = priceBTC['symbol']
        bpriceBTC = priceBTC['price']

        if bsymbolBTC in kucoinDictBTC:
            diffBTC = float(bpriceBTC) - kucoinDictBTC[bsymbolBTC] # find the biggest diff. 
            if bsymbolBTC[-3:] == 'BTC':
                
                differenceDictlolBTC[bsymbolBTC] = diffBTC

    # print(differenceDictlolBTC)
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
    

    # print(differenceListBTC)
    # print(differenceListDash)

    amountOfCoinsToBuyBTC = {}
    differenceDictFinalBTC = {}
    # sellorders = client.get_sell_orders('ENJ-ETH')
    print('-------------------------')
    # print(sellorders)
    # print('_________________________')
    # print(amountOfCoinsToBuy)
    amountOfCoinsBTC = 0
    priceOfOrderBTC = 0
    differenceDictPreBTC = {}
    differenceDictVolBTC = {}
    #print(differenceListDashBTC)
    
    
    
    # print(differenceListDash)
    for i in differenceListDashBTC:
        sellordersBTC = client.get_sell_orders('{}'.format(i), limit=10)
        amountOfCoinsBTC = 0
        priceOfOrderBTC = 0
    
        for coins in sellordersBTC:
            priceBTC = float(coins[2])
            amountOfTheCoinBTC = float(coins[1])
            priceOfCoinAskBTC = float(coins[0])
        
            priceOfOrderBeforeBidBTC = priceOfOrderBTC + priceBTC
    
            if priceOfOrderBeforeBidBTC >= accountBalanceKucoinBTC:
                BTCLeft = (accountBalanceKucoinBTC - priceOfOrderBTC)
            
            
                amountToBuyBTC = BTCLeft / priceOfCoinAskBTC
            
                finalOrderBTC = (amountToBuyBTC * priceOfCoinAskBTC) + priceOfOrderBTC
            
            
                amountOfCoinsFinalBTC = amountToBuyBTC + amountOfCoinsBTC
                          
                          
        
                symbolNoDashBTC = i.replace('-', '')
                differenceDictPreBTC[symbolNoDashBTC] = finalOrderBTC
                differenceDictVolBTC[symbolNoDashBTC] = amountOfCoinsFinalBTC
            
            
            
            else:
            
                priceOfOrderBTC += priceBTC
            
                amountOfCoinsBTC += amountOfTheCoinBTC
        
            continue
    
    
    # print(differenceDictVolBTC)
    differenceDictBTC = {}

    amountOfCoinsBinanceBTC = 0
    priceOrderBinanceBTC = 0
    # FOR BINANCE 
    for coins, vol in differenceDictVolBTC.items():
        amountOfCoinsBinanceBTC = 0
        priceOrderBinanceBTC = 0
        depthBTC = bclient.get_order_book(symbol='{}'.format(coins), limit=10)
        bbuyBTC = depthBTC['bids']


        for i in bbuyBTC:
        
            amountCoinBinanceBTC = float(i[1])
            priceCoinBinanceBTC = float(i[0])
            priceBTCBinance = priceCoinBinanceBTC * amountCoinBinanceBTC
        
            amountOfCoinsBeforeBTC = amountOfCoinsBinanceBTC + amountCoinBinanceBTC
        
            if amountOfCoinsBeforeBTC >= vol:
            
                amountOfCoinsLeftBTC = vol - amountOfCoinsBinanceBTC
            
                priceOfSelectCoinsBTC = amountOfCoinsLeftBTC * priceCoinBinanceBTC
            
                finalPriceBinanceBTC = priceOrderBinanceBTC + priceOfSelectCoinsBTC
            
                # print(finalPriceBinance)
            
                differenceInPricesBTC = finalPriceBinanceBTC - differenceDictPreBTC[coins]
                differenceDictBTC[coins] = differenceInPricesBTC
            
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
        if coinsBTC in coinFeesBTC:
    #     newProfit = prices * (1 - baseFee)
            
            coinPriceKucoinBTC = float(kucoinDictBTC[coinsBTC])
            amountOfCoinsToBuyBTC = differenceDictVolBTC[coinsBTC]
            # nameWithoutBigCoin = coins.replace('ETH', '').replace('BTC', '').replace('USDT', '')
            # print(nameWithoutBigCoin)
            # if '' and 'ETH' and 'USDT' and 'BTC' not in nameWithoutBigCoin:
            withdrawlFeeBTC = coinFeesBTC[coinsBTC]
    
    
            priceToWithdrawlBTC = withdrawlFeeBTC * coinPriceKucoinBTC
    
    
            finalProfitBTC = pricesBTC - priceToWithdrawlBTC
    
            finalCoinsAfterBaseFeeBTC[coinsBTC] = finalProfitBTC

    
    
    # print(finalCoinsAfterBaseFeeBTC)
# order all difference coins by how much profit they make. best coin is named bestCoin, use that in all further operations for the final part
    
    
    
    coinsAndStuffBTC = sorted(finalCoinsAfterBaseFeeBTC, key=finalCoinsAfterBaseFeeBTC.__getitem__, reverse=True)
    bestCoinFormerBTC = coinsAndStuffBTC[0]
    bestCoinFirstThreeBTC = bestCoinFormerBTC[:3]
    bestCoinBTC = {}
    bestCoinBTC[bestCoinFormerBTC] = finalCoinsAfterBaseFeeBTC[bestCoinFormerBTC] / accountBalanceKucoinBTC
    bestCoinPercentageBTC = bestCoinBTC[bestCoinFormerBTC]
    bestCoinKU = []

    
    print(bestCoinBTC)

    
    
    for coins in bestCoinBTC:
    
        if len(coins) == 7:
            newCoinNameKU = coins[:4] + '-' + coins[4:]
    
        if len(coins) == 6:
            newCoinNameKU = coins[:3] + '-' + coins[3:]
    
        bestCoinKU.append(newCoinNameKU)
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

            
            
    if bestCoinPercentageBTC > 0.03:
        print("BUY KUCOIN SELL BINANCE")
            
        
        try:
            transactionBTC = client.create_buy_order('{}'.format(bestCoinKU), 'BEST_PRICE', differenceDictVolBTC[bestCoinFormerBTC])
            print(transactionBTC)   
                
                    
           
            ordersBTC = client.get_active_orders('{}'.format(bestCoinKU))
            
            time.sleep(1)
                
                
            
        except:
            print("PROBLEM WITH TRADE")
            
            rdnVar = 6
            
            
        if rdnVar != 6:
            for x in range(0, 11):
                    
                    
                    if orders['BUY']:
                        
                        print('order not filled')
                        
                        x += 1
                        
                        time.sleep(1)
                        
                
                        
                        
                        if x == 10:
                            client.cancel_all_orders()
        
                    else:
                
                
                   
                    
                        print("ORDER FILLED")
                    
                        balanceBTCBinance = bclient.get_asset_balance(asset='ETH')
                        randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree))) 
                    
                        maketradeBTC(bestCoinFormerBTC, balanceBTCBinance, randomCoinBalanceBTC)

            
            
# balanceETHBinance = bclient.get_asset_balance(asset='ETH')
def maketradeBTC(x, y, z):
    randomCoinBalanceBTC = float(client.get_coin_balance('{}'.format(bestCoinFirstThreeBTC)))
    if randomCoinBalanceBTC > 0:
        addressBTC = bclient.get_deposit_address(asset='{}'.format(bestCoinFirstThreeBTC))
        client.create_withdrawal('{}'.format(bestCoinFirstThreeBTC), float(randomCoinBalanceBTC['balance']),
                                 str(addressBTC['address']))
        print('WITHDRAWING')
        
        
    while True:
       
    
        
        try:
            orderBinanceBTC = bclient.order_market_sell(symbol='{}'.format(bestCoinFormerBTC), quantity=differenceDictVolBTC[bestCoinFormerBTC])
            time.sleep(5)
            balanceBTC = print('COIN SOLD ON BINANCE FOR: {}'.format(balanceETHBinance))
            return balanceBTC
            break
        except:
            print('COINS NOT SOLD YET')
        
            continue
    
        

# tom, do the safety stuff like checking if buy went through on kucoin and if the coins were sent properly, and if they sold on binance


# In[12]:


while True:
    
    try:
        watch()
        time.sleep(3)
        watchBTC()
    except:
        time.sleep(10)
        continue


# In[ ]:


# this does that wonderful thing called TRI arbi

def triArbiBinance():
    
    pricesBTC = bclient.get_all_tickers() # get all binance prices

    
    # this makes a dict of all kucoin coins
    binanceDictTri = {} # create a dictionary

    for coin in pricesBTC:
        bsymbolTri = price['symbol']
        bpriceTri = price['price']
        binanceDictTri[bsymbolTri] = bpriceTri # add to the dict of all binance coins without extra info
    
    originalPais = ['ETHBTC', 'ETHUSDT', 'ETCETH', 'BTCUSD']
        


# In[ ]:


while True:
    try:
        triArbiBinance()
    except:
        continue


# In[22]:


# input = input('Press q to quit: ')
# just need to find out why it is not printing best coin, then look at both exchanges and do a basic test
i = 0
while True:
    
#     if input == 'q':
#         break
    
    # i += 1
    try:
        # print('IT: {}'.format(i))
        # watch()
        watchBTC()
    except:
        time.sleep(10)
        continue


# In[21]:


# TEST CELL FOR NEOBTC TO TEST BTC BUYING
# bitbuy should be verified in next couple days, then test btc/eth so everything is ready to go
import time



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




def watchBTC():
    
    
    # this gets the prices
    coinsBTC = client.get_trading_symbols() # get all kucoin prices
    pricesBTC = bclient.get_all_tickers() # get all binance prices

    
    # this makes a dict of all kucoin coins
    kucoinDictBTC = {} # create a dictionary

    for coin in coinsBTC:
        coinsymbolBTC = coin['symbol']
        coinsymbolBTC = coinsymbolBTC.replace('-', '') # we need to remove dash to ocmpare to binance
        lastDealBTC = coin['lastDealPrice']
        kucoinDictBTC[coinsymbolBTC] = lastDealBTC # add to the dict to compare binance and kucoin

    
    # this makes a dict of all binance coins

    

    
    # makes a dict of all things that are the same

    differenceDictlolBTC = {}

    for priceBTC in pricesBTC:
        bsymbolBTC = priceBTC['symbol']
        bpriceBTC = priceBTC['price']

        if bsymbolBTC in kucoinDictBTC:
            diffBTC = float(bpriceBTC) - kucoinDictBTC[bsymbolBTC] # find the biggest diff. 
            if bsymbolBTC[-3:] == 'BTC':
                
                differenceDictlolBTC[bsymbolBTC] = diffBTC

    # print(differenceDictlolBTC)
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
    

    # print(differenceListBTC)
    # print(differenceListDash)

    amountOfCoinsToBuyBTC = {}
    differenceDictFinalBTC = {}
    # sellorders = client.get_sell_orders('ENJ-ETH')
    print('-------------------------')
    # print(sellorders)
    # print('_________________________')
    # print(amountOfCoinsToBuy)
    amountOfCoinsBTC = 0
    priceOfOrderBTC = 0
    differenceDictPreBTC = {}
    differenceDictVolBTC = {}
    #print(differenceListDashBTC)
    
    
    
    # print(differenceListDash)
    for i in differenceListDashBTC:
        sellordersBTC = client.get_sell_orders('{}'.format(i), limit=10)
        amountOfCoinsBTC = 0
        priceOfOrderBTC = 0
    
        for coins in sellordersBTC:
            priceBTC = float(coins[2])
            amountOfTheCoinBTC = float(coins[1])
            priceOfCoinAskBTC = float(coins[0])
        
            priceOfOrderBeforeBidBTC = priceOfOrderBTC + priceBTC
    
            if priceOfOrderBeforeBidBTC >= accountBalanceKucoinBTC:
                BTCLeft = (accountBalanceKucoinBTC - priceOfOrderBTC)
            
            
                amountToBuyBTC = BTCLeft / priceOfCoinAskBTC
            
                finalOrderBTC = (amountToBuyBTC * priceOfCoinAskBTC) + priceOfOrderBTC
            
            
                amountOfCoinsFinalBTC = amountToBuyBTC + amountOfCoinsBTC
                          
                          
        
                symbolNoDashBTC = i.replace('-', '')
                differenceDictPreBTC[symbolNoDashBTC] = finalOrderBTC
                differenceDictVolBTC[symbolNoDashBTC] = amountOfCoinsFinalBTC
            
            
            
            else:
            
                priceOfOrderBTC += priceBTC
            
                amountOfCoinsBTC += amountOfTheCoinBTC
        
            continue
    
    
    # print(differenceDictVolBTC)
    differenceDictBTC = {}

    amountOfCoinsBinanceBTC = 0
    priceOrderBinanceBTC = 0
    # FOR BINANCE 
    for coins, vol in differenceDictVolBTC.items():
        amountOfCoinsBinanceBTC = 0
        priceOrderBinanceBTC = 0
        depthBTC = bclient.get_order_book(symbol='{}'.format(coins), limit=10)
        bbuyBTC = depthBTC['bids']


        for i in bbuyBTC:
        
            amountCoinBinanceBTC = float(i[1])
            priceCoinBinanceBTC = float(i[0])
            priceBTCBinance = priceCoinBinanceBTC * amountCoinBinanceBTC
        
            amountOfCoinsBeforeBTC = amountOfCoinsBinanceBTC + amountCoinBinanceBTC
        
            if amountOfCoinsBeforeBTC >= vol:
            
                amountOfCoinsLeftBTC = vol - amountOfCoinsBinanceBTC
            
                priceOfSelectCoinsBTC = amountOfCoinsLeftBTC * priceCoinBinanceBTC
            
                finalPriceBinanceBTC = priceOrderBinanceBTC + priceOfSelectCoinsBTC
            
                # print(finalPriceBinance)
            
                differenceInPricesBTC = finalPriceBinanceBTC - differenceDictPreBTC[coins]
                differenceDictBTC[coins] = differenceInPricesBTC
            
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
        if coinsBTC in coinFeesBTC:
            
    #     newProfit = prices * (1 - baseFee)
        
            coinPriceKucoinBTC = float(kucoinDictBTC[coinsBTC])
            amountOfCoinsToBuyBTC = differenceDictVolBTC[coinsBTC]
            # nameWithoutBigCoin = coins.replace('ETH', '').replace('BTC', '').replace('USDT', '')
            # print(nameWithoutBigCoin)
            # if '' and 'ETH' and 'USDT' and 'BTC' not in nameWithoutBigCoin:
            withdrawlFeeBTC = coinFeesBTC[coinsBTC]
    
    
            priceToWithdrawlBTC = withdrawlFeeBTC * coinPriceKucoinBTC
    
    
            finalProfitBTC = pricesBTC - priceToWithdrawlBTC
    
            finalCoinsAfterBaseFeeBTC[coinsBTC] = finalProfitBTC

    
    
    # print(finalCoinsAfterBaseFeeBTC)
# order all difference coins by how much profit they make. best coin is named bestCoin, use that in all further operations for the final part
    
    
    
    coinsAndStuffBTC = sorted(finalCoinsAfterBaseFeeBTC, key=finalCoinsAfterBaseFeeBTC.__getitem__, reverse=True)
    bestCoinFormerBTC = 'NEOBTC'
    bestCoinFirstThreeBTC = 'NEO'
    bestCoinBTC = {}
    bestCoinBTC['NEOBTC'] = finalCoinsAfterBaseFeeBTC['NEOBTC'] / accountBalanceKucoinBTC
    bestCoinPercentageBTC = bestCoinBTC['NEOBTC']
    bestCoinKU = 'NEO-BTC'


    
    print(bestCoinBTC)

    
    
    for coins in bestCoinBTC:
    
        if len(coins) == 7:
            newCoinNameKU = coins[:4] + '-' + coins[4:]
    
        if len(coins) == 6:
            newCoinNameKU = coins[:3] + '-' + coins[3:]
    
        bestCoinKU.append(newCoinNameKU)
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

            
            
    if bestCoinPercentageBTC > 0.03:
        print("BUY KUCOIN SELL BINANCE")
            
        
        try:
            transactionBTC = client.create_buy_order('{}'.format(bestCoinKU), 'BEST_PRICE', differenceDictVolBTC[bestCoinFormerBTC])
            print(transactionBTC)   
                
                    
           
            ordersBTC = client.get_active_orders('{}'.format(bestCoinKU))
            
            time.sleep(1)
                
                
            
        except:
            print("PROBLEM WITH TRADE")
            
            rdnVar = 6
            
            
        if rdnVar != 6:
            for x in range(0, 11):
                    
                    
                    if orders['BUY']:
                        
                        print('order not filled')
                        
                        x += 1
                        
                        time.sleep(1)
                        
                
                        
                        
                        if x == 10:
                            client.cancel_all_orders()
        
                    else:
                
                
                   
                    
                        print("ORDER FILLED")
                    
                        balanceBTCBinance = bclient.get_asset_balance(asset='ETH')
                        randomCoinBalance = float(client.get_coin_balance('{}'.format(bestCoinFirstThree))) 
                    
                        maketradeBTC(bestCoinFormerBTC, balanceBTCBinance, randomCoinBalanceBTC)

            
            
# balanceETHBinance = bclient.get_asset_balance(asset='ETH')
def maketradeBTC(x, y, z):
    randomCoinBalanceBTC = float(client.get_coin_balance('{}'.format(bestCoinFirstThreeBTC)))
    if randomCoinBalanceBTC > 0:
        addressBTC = bclient.get_deposit_address(asset='{}'.format(bestCoinFirstThreeBTC))
        client.create_withdrawal('{}'.format(bestCoinFirstThreeBTC), float(randomCoinBalanceBTC['balance']),
                                 str(addressBTC['address']))
        print('WITHDRAWING')
        
        
    while True:
       
    
        
        try:
            orderBinanceBTC = bclient.order_market_sell(symbol='{}'.format(bestCoinFormerBTC), quantity=differenceDictVolBTC[bestCoinFormerBTC])
            time.sleep(5)
            balanceBTC = print('COIN SOLD ON BINANCE FOR: {}'.format(balanceETHBinance))
            return balanceBTC
            break
        except:
            print('COINS NOT SOLD YET')
        
            continue
    
        

# tom, do the safety stuff like checking if buy went through on kucoin and if the coins were sent properly, and if they sold on binance


# In[16]:


binance = float(allBinanceCoins['ETCETH'])
print(binance)
kucoin = float(kucoinDict['ETCETH'])
print(kucoin)
print(abs(float(kucoin) - float(binance)))
print(float((kucoin + binance) / 2))
print((abs(float(kucoin - binance)) / (float((kucoin + binance) / 2))))


# In[26]:


# just prints out the list
print(sorted(finalCoinsToTrade.items(), key=lambda x: x[1]))


# In[ ]:


# TEST CELL FOR THE API COMMANDS
# this command gets ticker which contains almost all helpful info
info = bclient.get_ticker(symbol='ETHBTC')
# this then prints out just the volume
print(info['volume'])
moreInfo = bclient.get_ticker()
print(moreInfo)


# In[ ]:


# finds the best coin and prepares to buy it.  In future,
# incorporate the code below which gets stuff like how much coin i can
# buy ect. with the coin with the best price diff
# also look to make sure that the coin isnt scam ect.
bestPriceDiffCoin = max(percentDiffDictBinance.items(), key=lambda x: x[1])


# In[ ]:


# this is the function to sell coins on kucoin.  Eventually, put this into a function as well as get the transfer and withdrawl of coins

# have a 'best' coin.  this will be done later 
bestCoin = 

# sell order goes symbol, price, amount
sellOrder = client.create_sell_order('KCS-BTC', '0.01', '1000')


# In[ ]:


def watch():
    try:
        orders = client.get_buy_orders('DASH-ETH', limit=5)
        sellorders = client.get_sell_orders('DASH-ETH', limit=5)
        depth = bclient.get_order_book(symbol='DASHETH')
        bsell = depth['asks'][0][0]
        bbuy = depth['bids'][0][0]
        ksell = sellorders[0][0]
        kbuy = orders[0][0]
        kbuyAdd = kbuy + 0.01
        print("GOT BOOKS")
        
    except:
        print("Problem grabbing order books")
        kbuyAdd = 2
        bbuy = 1
    # if an ask is larger than a sell order arbitrage
    if kbuyAdd < float(bbuy):
        print("BUY KUCOIN SELL BINANCE")
        print(sellorders[0])
        print(depth['bids'][0])
        dashbalance = client.get_coin_balance('ETH')
        print(dashbalance['balance'])
        kucoinBalance = dashbalance['balance'] # get balance
        buyPrice = kbuy + 0.000001 # so buy order is placed at top
        print(kucoinBalance/buyPrice)
        amount = kucoinBalance/buyPrice # find the amount that you can buy
        print('Buying {0} dash coin on kucoin'.format(amount))
        
        try:
            transaction = client.create_buy_order('DASH-ETH', buyPrice, amount)
            print(transaction)
            maketrade(transaction[orderOid])
        except:
            client.cancel_all_orders()
            print("PROBLEM WITH TRADE")
 

def maketrade(oid):
    for x in range(0,9):
        time.sleep(1)
        orders = client.get_active_orders('DASH-ETH')
        time.sleep(1)
        print(orders)
        if orders['BUY']:
            print("ORDER NOT FILLED")
        else:
            print("ORDER FILLED")
            dashbalance = client.get_coin_balance('DASH')
            address = bclient.get_deposit_address(asset='DASH')
            client.create_withdrawal('DASH', float(dashbalance['balance']),
                                    str(address['address']))
            makeSellTradeBinance()
        print(x)
        if x == 8:
            client.cancel_all_orders()
        time.sleep(1)

        
def makeSellTradeBinance():
    bclient.order_market_sell(symbol='{}'.format(INSERTVAR), quantity=INSERTVAR)


# In[ ]:


# def watch():
#     try:
#         orders = client.get_buy_orders('DASH-ETH', limit=5)
#         sellorders = client.get_sell_orders('DASH-ETH', limit=5)
#         depth = bclient.get_order_book(symbol='DASHETH')
#         bsell = depth['asks'][0][0]
#         bbuy = depth['bids'][0][0]
#         ksell = sellorders[0][0]
#         kbuy = orders[0][0]
#         kbuyAdd = kbuy + 0.01
        
#     except:
#         print("Problem grabbing order books")
#         kbuyAdd = 2
#         bbuy = 1
#     # if an ask is larger than a sell order arbitrage
#     if kbuyAdd < float(bbuy):
#         print("BUY KUCOIN SELL BINANCE")
#         print(sellorders[0])
#         print(depth['bids'][0])
#         dashbalance = client.get_coin_balance('ETH')
#         print(dashbalance['balance'])
#         kucoinBalance = dashbalance['balance'] # get balance
#         buyPrice = kbuy + 0.000001 # so buy order is placed at top
#         print(kucoinBalance/buyPrice)
#         amount = kucoinBalance/buyPrice # find the amount that you can buy
#         print('Buying {0} dash coin on kucoin'.format(amount))
        
#         try:
#             transaction = client.create_buy_order('DASH-ETH', buyPrice, amount)
#             print(transaction)
#             maketrade(transaction[orderOid])
#         except:
#             client.cancel_all_orders()
#             print("PROBLEM WITH TRADE")
            
            
# time.sleep(7)

def maketrade(oid):
    for x in range(0,9):
        time.sleep(1)
        orders = client.get_active_orders('DASH-ETH')
        time.sleep(1)
        print(orders)
        if orders['BUY']:
            print("ORDER NOT FILLED")
        else:
            print("ORDER FILLED")
            dashbalance = client.get_coin_balance('DASH')
            address = bclient.get_deposit_address(asset='DASH')
            client.create_withdrawal('DASH', float(dashbalance['balance']),
                                    str(address['address']))
            makeSellTradeBinance()
        print(x)
        if x == 8:
            client.cancel_all_orders()
        time.sleep(1)
# def makeTradeBinance():
#     print('madeit')
#     # in future, when u want thing to work, you change this to executing sell trade on 
#     # binance or whatever

# while True:
#     watch();


# In[ ]:


def makeSellTradeBinance():
    print('madeit')
    # in future, when u want thing to work, you change this to executing sell trade on 
    # binance or whatever


# In[ ]:


while True:
    watch();
    


# In[ ]:


# to do list:
    # hookup to make trade in binance instead of just saying made it
    # reverse system to go binance to kucoin because prices could be different that way
    # start recording differences in prices and graph them
    # use ai to analyze these prices to find at what time of day prices are usually biggest so my system can be turned on for this time and expect the trade
    # start basic technical analysis next
    # move onto ichimoku cloud technical analysis.  there is a github for this - just look up ichimoku cloud ai for crypto/crypto bot on github
    # add one to two more trading platforms.  Coinbase. CryptoCompare API?
    # factor in trade fees so the percentage difference has to be more than how much i will lose

