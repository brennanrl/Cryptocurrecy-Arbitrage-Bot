
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
print(prices)


# In[8]:


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


# In[9]:


# this is the balances for all starting pairs which are listed below

accountBalanceBinanceEthereum = 0.01 # (float(bclient.get_asset_balance(asset='ETH')['free']) / 2) 

accountBalanceBinanceBitcoin = 0.1# (float(bclient.get_asset_balance(asset='BTC')['free']) / 2) 
accountBalanceBinanceUSDT = 1000# (float(bclient.get_asset_balance(asset='USDT')['free']) / 2)  

accountBalanceBinanceDict = {'BTC': accountBalanceBinanceBitcoin, 'ETH': accountBalanceBinanceEthereum, 'USDT': accountBalanceBinanceUSDT}


print(accountBalanceBinanceDict)


# In[10]:


from binance.enums import *
order = bclient.create_test_order(
    symbol='TRIGBNB',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=0.51,
    price='0.014482')


# In[31]:


# this cell just does everything faster :))):()(:


def makeMoneyPlz():
    prices = bclient.get_all_tickers() # get all binance prices
    allBCoins = {}
    for coins in prices:
        symbol = coins['symbol']
        price = coins['price']
        allBCoins[symbol] = price


    startingPairs = {'ETHBTC', 'BNBBTC', 'BNBETH', 'BTCUSDT', 'ETHUSDT', 'BNBUSDT'}

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
            firstLetters = pairs[:3]

        if len(pairs) == 7:
            lastLetters = pairs[-4:]
            firstLetters = pairs[:3]

        majorCoinBalance = float(accountBalanceBinanceDict[lastLetters])
            # taxSymbol = firstLetters 

        amountOfCoinsBinanceTri = 0



        priceOrderBinanceTri = 0
        depthBinanceTri = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

        bbuyTri = depthBinanceTri['asks']


        for ordersTri in bbuyTri:

            amountCoinBinanceTri = float(ordersTri[1])
            priceCoinBinanceTri = float(ordersTri[0])

            priceBinanceTri = priceCoinBinanceTri * amountCoinBinanceTri

            priceBeforeTri = priceOrderBinanceTri + priceBinanceTri

            if priceBeforeTri >= majorCoinBalance:

                majorCoinLeft = majorCoinBalance - priceOrderBinanceTri

                amountOfCoinToStillBuy = majorCoinLeft / priceCoinBinanceTri

                priceOfSelectCoinsTri = amountOfCoinToStillBuy * priceCoinBinanceTri

                finalPriceBinanceTri = priceOrderBinanceTri + priceOfSelectCoinsTri

                amountOfCoins = (amountOfCoinToStillBuy + amountOfCoinsBinanceTri)
                    # print(finalPriceBinance)
                minAmountDigits = minimumAmountDict[pairs]
                differenceInDigits = float(len(str(amountOfCoins))) - float(minAmountDigits)

                if differenceInDigits > 0:
                    differenceInDigits = int(differenceInDigits * (-1))
                    amountOfCoins = float(str(amountOfCoins)[:differenceInDigits])

                amountOfMinorCoin[pairs] = amountOfCoins


                if pairs == 'BNBETH':
                    taxMinorBNBETH1 = (amountOfCoins * (0.00075))
                taxMinorBTCUSDT1 = 1

                break

            else:

                amountOfCoinsBinanceTri += amountCoinBinanceTri
                priceOrderBinanceTri += priceBinanceTri

        # a dict of all coins
        # print(amountOfMinorCoin)

    allCoinList = []


    for coin in prices:
        symbolTri = coin['symbol']
        priceTri = coin['price']
        allCoinList.append(symbolTri)





    ETHFirstThree = set()
        # BTCFirstThree = set()
    BNBFirstThree = set()
        # USDTFirstThree = set()

    for coins in allCoinList:




        if coins[-3:] == 'ETH':
            # coinListETH.add(coins)
            if len(coins) == 8:
                coinNameTri = coins[:5]
            if len(coins) == 7:
                coinNameTri = coins[:4]

            if len(coins) == 6:
                coinNameTri = coins[:3]
            ETHFirstThree.add(coinNameTri)
        
#         elif coins[-3:] == 'BTC':
#             coinListBTC.add(coins)
#             if len(coins) == 8:
#                 coinNameTri = coins[:5]
#             if len(coins) == 7:
#                 coinNameTri = coins[:4]
        
#             if len(coins) == 6:
#                 coinNameTri = coins[:3]
#             BTCFirstThree.add(coinNameTri)
        elif coins[-3:] == 'BNB':
            # coinListBNB.add(coins)
            if len(coins) == 8:
                coinNameTri = coins[:5]
            if len(coins) == 7:
                coinNameTri = coins[:4]

            if len(coins) == 6:
                coinNameTri = coins[:3]
            BNBFirstThree.add(coinNameTri)
#         elif coins[-4:] == 'USDT':
#             coinListUSDT.add(coins)
#             if len(coins) == 8:
#                 coinNameTri = coins[:4]
#             if len(coins) == 7:
#                 coinNameTri = coins[:3]
        
#             if len(coins) == 9:
#                 coinNameTri = coins[:5]
#             USDTFirstThree.add(coinNameTri)

        

      
    BNBETHSimilar = set()

    for coins in ETHFirstThree:
        # create a dict of sim coins
        if coins in BNBFirstThree:
            coinsExtraBNBETH = coins + 'BNB'
            BNBETHSimilar.add(coinsExtraBNBETH)         


#     ETHBTCSimilar = set()        
#     for coins in BTCFirstThree:
#         if coins in ETHFirstThree:
#             coinsExtraETHBTC = coins + 'ETH'
#             ETHBTCSimilar.add(coinsExtraETHBTC)

#     BNBBTCSimilar = set()
#     for coins in BTCFirstThree:
#         if coins in BNBFirstThree:
#             coinsExtraBNBBTC = coins + 'BNB'
#             BNBBTCSimilar.add(coinsExtraBNBBTC)
        
#     BTCUSDTSimilar = set()
#     for coins in USDTFirstThree:
#         if coins in BTCFirstThree:
#             coinsExtraBTCUSDT = coins + 'BTC'
#             BTCUSDTSimilar.add(coinsExtraBTCUSDT)

#     ETHUSDTSimilar = set()
#     for coins in USDTFirstThree:
#         if coins in ETHFirstThree:
#             coinsExtraETHUSDT = coins + 'ETH'
#             ETHUSDTSimilar.add(coinsExtraETHUSDT)
    
#     BNBUSDTSimilar = set()
#     for coins in USDTFirstThree:
#         if coins in BNBFirstThree:
#             coinsExtraBNBUSDT = coins + 'BNB'
#             BNBUSDTSimilar.add(coinsExtraBNBUSDT)

       
    # appends second coin name onto everything for looking at orders (above)
    # this section goes through and calculates how much of a small coin i can buy then calculates how much of the big coin
    # and calcs the profit 
    # this one does eth bnb 
    smallCoinNameBNBETHDict = {}
    for pairs in BNBETHSimilar:
        if len(pairs) == 7:
            smallCoinNameBNBETH = '{0}{1}'.format(pairs[:4], 'ETH')
        if len(pairs) == 6:
            smallCoinNameBNBETH = '{0}{1}'.format(pairs[:3], 'ETH')
        if len(pairs) == 8:
            smallCoinNameBNBETH = '{0}{1}'.format(pairs[:5], 'ETH')
        smallCoinNameBNBETHDict[pairs] = smallCoinNameBNBETH

    for pairs in BNBETHSimilar:
        amountOfMiddleCoinBNBETH = 0
        amountOfCoinsBinanceBNBETH = 0
        newCoinNameBNBETH = pairs


        priceOrderBinanceBNBETH = 0
        depthBinanceBNBETH = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

        bbuyBNBETH = depthBinanceBNBETH['asks']




        for orders in bbuyBNBETH:

            amountCoinBinanceBNBETH = float(orders[1])
            priceCoinBinanceBNBETH = float(orders[0])
            priceBinanceBNBETH = priceCoinBinanceBNBETH * amountCoinBinanceBNBETH

            priceBeforeBNBETH = priceOrderBinanceBNBETH + priceBinanceBNBETH

            if priceBeforeBNBETH >= amountOfMinorCoin['BNBETH']:


                minorCoinLeftBNBETH = amountOfMinorCoin['BNBETH'] - priceOrderBinanceBNBETH

                amountOfCoinToStillBuyBNBETH = minorCoinLeftBNBETH / priceCoinBinanceBNBETH

                priceOfSelectCoinsBNBETH = amountOfCoinToStillBuyBNBETH * priceCoinBinanceBNBETH

                # finalPriceBinanceBNBETH = priceOrderBinanceBNBETH + priceOfSelectCoinsBNBETH

                amountOfCoinsMidBNBETH = (amountOfCoinToStillBuyBNBETH + amountOfCoinsBinanceBNBETH)

                firstThreeMidBNBETH = pairs.replace('BNB', 'BTC')
                taxMidBNBETH = (amountOfCoinsMidBNBETH * 0.00075) * (float(allBCoins[firstThreeMidBNBETH]) / float(allBCoins['BNBETH']))
                amountOfMiddleCoinBNBETH = amountOfCoinsMidBNBETH

                break

            else:

                amountOfCoinsBinanceBNBETH += amountCoinBinanceBNBETH
                priceOrderBinanceBNBETH += priceBinanceBNBETH 








        amountOfCoinsBinanceBNBETHF = 0



        priceOrderBinanceBNBETHF = 0
        depthBinanceBNBETHF = bclient.get_order_book(symbol='{}'.format(smallCoinNameBNBETHDict[pairs]), limit=10)

        bbuyBNBETHF = depthBinanceBNBETHF['bids']


        for orders in bbuyBNBETHF:

            amountCoinBinanceBNBETHF = float(orders[1])
            priceCoinBinanceBNBETHF = float(orders[0])
            priceBinanceBNBETHF = priceCoinBinanceBNBETHF * amountCoinBinanceBNBETHF

            amountCoinBeforeBNBETHF = amountOfCoinsBinanceBNBETHF + amountCoinBinanceBNBETHF

            if amountCoinBeforeBNBETHF >= float(amountOfMiddleCoinBNBETH):


                middleCoinLeftBNBETHF = float(amountOfMiddleCoinBNBETH) - amountOfCoinsBinanceBNBETHF



                priceOfSelectCoinsBNBETHF = middleCoinLeftBNBETHF * priceCoinBinanceBNBETHF

                finalPriceBinanceBNBETHF = priceOrderBinanceBNBETHF + priceOfSelectCoinsBNBETHF


                finalPriceATBNBETHF = finalPriceBinanceBNBETHF 



                tax3BNBETH = (finalPriceATBNBETHF * 0.00075) * (float(allBCoins['ETHBTC']) / float(allBCoins['BNBBTC']))
                profitOfBigCoinBNBETH = finalPriceATBNBETHF


                taxBNBETH = (taxMinorBNBETH1 + taxMidBNBETH + tax3BNBETH) * float(allBCoins['BNBETH'])
                totalBNBETH = ((profitOfBigCoinBNBETH - taxBNBETH) - accountBalanceBinanceEthereum) / accountBalanceBinanceEthereum 
                nameTEMPORARYBNBETH = smallCoinNameBNBETHDict[pairs]
                firstThreeBNBETH = nameTEMPORARYBNBETH.replace('ETH', '')

                print(totalBNBETH)

                break

            else:

                amountOfCoinsBinanceBNBETHF += amountCoinBinanceBNBETHF
                priceOrderBinanceBNBETHF += priceBinanceBNBETHF    





        x = 0
        if totalBNBETH > 0:


            while True:

                try:




                    transactionBNBETH = bclient.order_market_buy(symbol='BNBETH', quantity=float(amountOfMinorCoin['BNBETH']))


                    rdnVarBNBETH = 3




                    if transactionBNBETH['status'] != 'FILLED':
                        print('order not filled')
                        break                    

                    else:


                        lotsOfSmallCoinBNBETH = float(amountOfMiddleCoinBNBETH)     
                        while True:

                            try:

                                transaction2BNBETH = bclient.order_market_buy(symbol=str(newCoinNameBNBETH), quantity=float(lotsOfSmallCoinBNBETH))   # float(lotsOfSmallCoin))





                                rdnVar2BNBETH = 2




                                if transaction2BNBETH['status'] != 'FILLED':

                                    print('order not filled yet')
                                else:

                                    accountBalanceFinalStepBNBETH = float(bclient.get_asset_balance(asset=str(firstThreeBNBETH))['free'])
                                    while True:

                                        try:


                                            transaction3BNBETH = bclient.order_market_sell(symbol=str(nameTEMPORARYBNBETH), quantity=float(accountBalanceFinalStepBNBETH))

                                            finalCommandBNBETH = 7
                                            # print(float(transaction3['origQty']) * (0.999))
                                            print('DUN FINALY BOSS')
                                            break
                                        except:
                                            accountBalanceFinalStepBNBETH = float(str(accountBalanceFinalStepBNBETH)[:-1])



                                    if finalCommandBNBETH == 7:
                                        print('getting there')
                                        break
                                if rdnVar2BNBETH == 2:
                                    print('almost done')
                                    break
                            except:
                                x += 1
                                lotsOfSmallCoinBNBETH = float(str(lotsOfSmallCoinBNBETH)[:-1])

                                if x == 20:
                                    lotsOfSmallCoinBNBETH = lotsOfSmallCoinBNBETH - (float(lotsOfSmallCoinBNBETH) * 0.01)




                    if rdnVarBNBETH == 3:
                        print('dunzoooo')
                        break
                except:
                    print('error BOSS REPORT STATION 12')
                    break





            


# In[32]:


makeMoneyPlz()


# In[23]:


def makeMoneyPlzETHBTC():
    prices = bclient.get_all_tickers() # get all binance prices
    allBCoins = {}
    for coins in prices:
        symbol = coins['symbol']
        price = coins['price']
        allBCoins[symbol] = price

    taxMinorETHBTC1 = 0    
    startingPairs = {'ETHBTC', 'BNBBTC', 'BNBETH', 'BTCUSDT', 'ETHUSDT', 'BNBUSDT'}

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
            firstLetters = pairs[:3]

        if len(pairs) == 7:
            lastLetters = pairs[-4:]
            firstLetters = pairs[:3]

        majorCoinBalance = float(accountBalanceBinanceDict[lastLetters])
            # taxSymbol = firstLetters 

        amountOfCoinsBinanceTri = 0



        priceOrderBinanceTri = 0
        depthBinanceTri = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

        bbuyTri = depthBinanceTri['asks']


        for ordersTri in bbuyTri:

            amountCoinBinanceTri = float(ordersTri[1])
            priceCoinBinanceTri = float(ordersTri[0])

            priceBinanceTri = priceCoinBinanceTri * amountCoinBinanceTri

            priceBeforeTri = priceOrderBinanceTri + priceBinanceTri

            if priceBeforeTri >= majorCoinBalance:

                majorCoinLeft = majorCoinBalance - priceOrderBinanceTri

                amountOfCoinToStillBuy = majorCoinLeft / priceCoinBinanceTri

                priceOfSelectCoinsTri = amountOfCoinToStillBuy * priceCoinBinanceTri

                finalPriceBinanceTri = priceOrderBinanceTri + priceOfSelectCoinsTri

                amountOfCoins = (amountOfCoinToStillBuy + amountOfCoinsBinanceTri)
                    # print(finalPriceBinance)
                minAmountDigits = minimumAmountDict[pairs]
                differenceInDigits = float(len(str(amountOfCoins))) - float(minAmountDigits)

                if differenceInDigits > 0:
                    differenceInDigits = int(differenceInDigits * (-1))
                    amountOfCoins = float(str(amountOfCoins)[:differenceInDigits])

                amountOfMinorCoin[pairs] = float(amountOfCoins)


                if pairs == 'ETHBTC':
                    print('-------', amountOfMinorCoin['ETHBTC'])
                    taxMinorETHBTC1 = (amountOfMinorCoin['ETHBTC'] * 0.00075) 
                    print(taxMinorETHBTC1)
                    taxMinorETHBTC1 = taxMinorETHBTC1 * (float(allBCoins['ETHBTC']) / float(allBCoins['BNBBTC']))
                    print(taxMinorETHBTC1)
                
                break
                    

            else:

                amountOfCoinsBinanceTri += amountCoinBinanceTri
                priceOrderBinanceTri += priceBinanceTri

        # a dict of all coins
        # print(amountOfMinorCoin)

    allCoinList = []


    for coin in prices:
        symbolTri = coin['symbol']
        priceTri = coin['price']
        allCoinList.append(symbolTri)





    ETHFirstThree = set()
    BTCFirstThree = set()
    BNBFirstThree = set()
    USDTFirstThree = set()

    for coins in allCoinList:




        if coins[-3:] == 'ETH':
            # coinListETH.add(coins)
            if len(coins) == 8:
                coinNameTri = coins[:5]
            if len(coins) == 7:
                coinNameTri = coins[:4]

            if len(coins) == 6:
                coinNameTri = coins[:3]
            ETHFirstThree.add(coinNameTri)
        
        elif coins[-3:] == 'BTC':
            # coinListBTC.add(coins)
            if len(coins) == 8:
                coinNameTri = coins[:5]
            if len(coins) == 7:
                coinNameTri = coins[:4]
        
            if len(coins) == 6:
                coinNameTri = coins[:3]
            BTCFirstThree.add(coinNameTri)
        elif coins[-3:] == 'BNB':
            # coinListBNB.add(coins)
            if len(coins) == 8:
                coinNameTri = coins[:5]
            if len(coins) == 7:
                coinNameTri = coins[:4]

            if len(coins) == 6:
                coinNameTri = coins[:3]
            BNBFirstThree.add(coinNameTri)
        elif coins[-4:] == 'USDT':
            # coinListUSDT.add(coins)
            if len(coins) == 8:
                coinNameTri = coins[:4]
            if len(coins) == 7:
                coinNameTri = coins[:3]
        
            if len(coins) == 9:
                coinNameTri = coins[:5]
            USDTFirstThree.add(coinNameTri)

        

      
    BNBETHSimilar = set()

    for coins in ETHFirstThree:
        # create a dict of sim coins
        if coins in BNBFirstThree:
            coinsExtraBNBETH = coins + 'BNB'
            BNBETHSimilar.add(coinsExtraBNBETH)         


    ETHBTCSimilar = set()        
    for coins in BTCFirstThree:
        if coins in ETHFirstThree:
            coinsExtraETHBTC = coins + 'ETH'
            ETHBTCSimilar.add(coinsExtraETHBTC)

    BNBBTCSimilar = set()
    for coins in BTCFirstThree:
        if coins in BNBFirstThree:
            coinsExtraBNBBTC = coins + 'BNB'
            BNBBTCSimilar.add(coinsExtraBNBBTC)
        
    BTCUSDTSimilar = set()
    for coins in USDTFirstThree:
        if coins in BTCFirstThree:
            coinsExtraBTCUSDT = coins + 'BTC'
            BTCUSDTSimilar.add(coinsExtraBTCUSDT)

    ETHUSDTSimilar = set()
    for coins in USDTFirstThree:
        if coins in ETHFirstThree:
            coinsExtraETHUSDT = coins + 'ETH'
            ETHUSDTSimilar.add(coinsExtraETHUSDT)
    
    BNBUSDTSimilar = set()
    for coins in USDTFirstThree:
        if coins in BNBFirstThree:
            coinsExtraBNBUSDT = coins + 'BNB'
            BNBUSDTSimilar.add(coinsExtraBNBUSDT)

    

       
    # appends second coin name onto everything for looking at orders (above)
    # this section goes through and calculates how much of a small coin i can buy then calculates how much of the big coin
    # and calcs the profit 
    # this one does eth bnb 
    smallCoinNameETHBTCDict = {}
    for pairs in ETHBTCSimilar:
        if len(pairs) == 7:
            smallCoinNameETHBTC = '{0}{1}'.format(pairs[:4], 'BTC')
        if len(pairs) == 6:
            smallCoinNameETHBTC = '{0}{1}'.format(pairs[:3], 'BTC')
        if len(pairs) == 8:
            smallCoinNameETHBTC = '{0}{1}'.format(pairs[:5], 'BTC')
        smallCoinNameETHBTCDict[pairs] = smallCoinNameETHBTC
    
    taxMidETHBTC = 0
    totalETHBTC = 0
    tax3ETHBTC = 0
    for pairs in ETHBTCSimilar:
        
        amountOfMiddleCoinETHBTC = 0
        amountOfCoinsBinanceETHBTC = 0
        newCoinNameETHBTC = pairs
        
        print('A', pairs)

        priceOrderBinanceETHBTC = 0
        depthBinanceETHBTC = bclient.get_order_book(symbol='{}'.format(pairs), limit=10)

        bbuyETHBTC = depthBinanceETHBTC['asks']




        for orders in bbuyETHBTC:
            print('lol')

            amountCoinBinanceETHBTC = float(orders[1])
            priceCoinBinanceETHBTC = float(orders[0])
            priceBinanceETHBTC = priceCoinBinanceETHBTC * amountCoinBinanceETHBTC

            priceBeforeETHBTC = priceOrderBinanceETHBTC + priceBinanceETHBTC

            if priceBeforeETHBTC >= amountOfMinorCoin['ETHBTC']:


                minorCoinLeftETHBTC = amountOfMinorCoin['ETHBTC'] - priceOrderBinanceETHBTC

                amountOfCoinToStillBuyETHBTC = minorCoinLeftETHBTC / priceCoinBinanceETHBTC

                priceOfSelectCoinsETHBTC = amountOfCoinToStillBuyETHBTC * priceCoinBinanceETHBTC

                # finalPriceBinanceETHBTC = priceOrderBinanceETHBTC + priceOfSelectCoinsETHBTC

                amountOfCoinsMidETHBTC = (amountOfCoinToStillBuyETHBTC + amountOfCoinsBinanceETHBTC)
                print(amountOfCoinsMidETHBTC)

                midCoinNameETHBTC = pairs.replace('ETH', 'BTC') 
                taxMidETHBTC = (amountOfCoinsMidETHBTC * 0.00075) * (float(allBCoins[midCoinNameETHBTC]) / float(allBCoins['BNBBTC']))
                amountOfMiddleCoinETHBTC = amountOfCoinsMidETHBTC

                break

            else:

                amountOfCoinsBinanceETHBTC += amountCoinBinanceETHBTC
                priceOrderBinanceETHBTC += priceBinanceETHBTC 








        amountOfCoinsBinanceETHBTCF = 0



        priceOrderBinanceETHBTCF = 0
        depthBinanceETHBTCF = bclient.get_order_book(symbol='{}'.format(smallCoinNameETHBTCDict[pairs]), limit=20)

        bbuyETHBTCF = depthBinanceETHBTCF['bids']


        for orders in bbuyETHBTCF:
            print('made it to second part')

            amountCoinBinanceETHBTCF = float(orders[1])
            priceCoinBinanceETHBTCF = float(orders[0])
            priceBinanceETHBTCF = priceCoinBinanceETHBTCF * amountCoinBinanceETHBTCF

            amountCoinBeforeETHBTCF = amountOfCoinsBinanceETHBTCF + amountCoinBinanceETHBTCF
            print(amountCoinBeforeETHBTCF)
            if amountCoinBeforeETHBTCF >= float(amountOfMiddleCoinETHBTC):
                
                print('a')
                middleCoinLeftETHBTCF = float(amountOfMiddleCoinETHBTC) - amountOfCoinsBinanceETHBTCF
                print('b')


                priceOfSelectCoinsETHBTCF = middleCoinLeftETHBTCF * priceCoinBinanceETHBTCF
                print('there')
                finalPriceBinanceETHBTCF = priceOrderBinanceETHBTCF + priceOfSelectCoinsETHBTCF


                finalPriceATETHBTCF = finalPriceBinanceETHBTCF 
                print('right before final stuff')


                tax3ETHBTC = (finalPriceATETHBTCF * 0.00075) / float(allBCoins['BNBBTC'])
                profitOfBigCoinETHBTC = finalPriceATETHBTCF

                print('right before tax')
                taxETHBTC = (taxMinorETHBTC1 + taxMidETHBTC + tax3ETHBTC) * float(allBCoins['BNBBTC'])
                totalETHBTC = ((profitOfBigCoinETHBTC - taxETHBTC) - accountBalanceBinanceBitcoin) / accountBalanceBinanceBitcoin 
                nameTEMPORARYETHBTC = smallCoinNameETHBTCDict[pairs]
                firstThreeETHBTC = nameTEMPORARYETHBTC.replace('BTC', '')

                print(totalETHBTC)
                print(taxMinorETHBTC1)
                print(taxMidETHBTC)
                print(tax3ETHBTC)
                time.sleep(20)

                break

            else:

                amountOfCoinsBinanceETHBTCF += amountCoinBinanceETHBTCF
                priceOrderBinanceETHBTCF += priceBinanceETHBTCF    





        x = 0
        if totalETHBTC > 10000:


            while True:

                try:




                    transactionETHBTC = bclient.order_market_buy(symbol='ETHBTC', quantity=float(amountOfMinorCoin['ETHBTC']))


                    rdnVarETHBTC = 3




                    if transactionETHBTC['status'] != 'FILLED':
                        print('order not filled')
                        break                    

                    else:


                        lotsOfSmallCoinETHBTC = float(amountOfMiddleCoinETHBTC)     
                        while True:

                            try:

                                transaction2ETHBTC = bclient.order_market_buy(symbol=str(newCoinNameETHBTC), quantity=float(lotsOfSmallCoinETHBTC))   # float(lotsOfSmallCoin))





                                rdnVar2ETHBTC = 2




                                if transaction2ETHBTC['status'] != 'FILLED':

                                    print('order not filled yet')
                                else:

                                    accountBalanceFinalStepETHBTC = float(bclient.get_asset_balance(asset=str(firstThreeETHBTC))['free'])
                                    while True:

                                        try:


                                            transaction3ETHBTC = bclient.order_market_sell(symbol=str(nameTEMPORARYETHBTC), quantity=float(accountBalanceFinalStepETHBTC))

                                            finalCommandETHBTC = 7
                                            # print(float(transaction3['origQty']) * (0.999))
                                            print('DUN FINALY BOSS')
                                            break
                                        except:
                                            accountBalanceFinalStepETHBTC = float(str(accountBalanceFinalStepETHBTC)[:-1])



                                    if finalCommandETHBTC == 7:
                                        print('getting there')
                                        break
                                if rdnVar2ETHBTC == 2:
                                    print('almost done')
                                    break
                            except:
                                x += 1
                                lotsOfSmallCoinETHBTC = float(str(lotsOfSmallCoinETHBTC)[:-1])

                                if x == 20:
                                    lotsOfSmallCoinETHBTC = lotsOfSmallCoinETHBTC - (float(lotsOfSmallCoinETHBTC) * 0.01)




                    if rdnVarETHBTC == 3:
                        print('dunzoooo')
                        break
                except:
                    print('error BOSS REPORT STATION 12')
                    break





            


# In[24]:




        
makeMoneyPlzETHBTC()
       


# In[25]:


def cool():
    hi = ['why', 'what', 'where']

def do(arg):
    print(hi)
do(cool)


# In[14]:


lol = set()
hi = ['what', 'lol']

for items in hi:
    lol.add(items)

for items in lol:
    yep = '{0}{1}'.format(items[:2], 'ETHBNB')
    print(yep)


# In[16]:


while True:
    try:
        MoneyPrinter6000()
        time.sleep(1)
    except:
        continue


# In[11]:



accountBalanceMajorCoinBNBETH = 0.001
transcation = bclient.order_market_buy(symbol='BNBETH', quantity=accountBalanceMajorCoinBNBETH)
print(transaction)


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

