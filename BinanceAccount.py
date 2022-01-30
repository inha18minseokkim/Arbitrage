import ssl

import config
import ccxt
import asyncio
import time
from binance import AsyncClient,BinanceSocketManager
class balance:
    def __init__(self,binance):
        self.base = binance.fetch_balance()
    def getBalance(self,coin):
        return self.base['free'][coin]
    def getBalanceList(self):
        return self.base
    async def update_websocket(self):
        client = await AsyncClient.create(config.get_secret('apiKey'),config.get_secret('secret'))
        bm = BinanceSocketManager(client)
        us = bm.user_socket()
        async with us as tmp:
            while True:
                res = await us.recv()
                print("async update by websocket",res)
                if res['e'] == 'outboundAccountPosition':
                    for i in res['B']:
                        self.base['free'][i['a']] = float(i['f'])

class user:
    def __init__(self):
        self.APIKEY = config.get_secret('apiKey')
        self.SECRET = config.get_secret('secret')
        self.binance = ccxt.binance({'apiKey' : self.APIKEY, 'secret' : self.SECRET})
        self.balance = balance(self.binance)
    def getBalanceList(self):
        return self.balance.getBalanceList()
    def getBalance(self,coin):
        return self.balance.getBalance(coin)
    def buyCrypto(self,coin,price,quantity=0): # threading.Thread(tmp.buyCrypto,args=('SOL/BNB',0,0.295))).start() 이렇게 호출하면됨
        tobuy, tosell = coin.split('/') #SOL/BNB인 경우 tobuy는 SOL tosell은 BNB tobuy:살거, tosell: 팔거
        #수량지정을 하지않은경우 최저 한도 수량으로 정함
        limitquantity = self.binance.markets[coin]['limits']['cost']['min']*1.05/price
        if quantity == 0: quantity = limitquantity
        #주문 넣기전에 잔고에 그만큼 있는지 확인 그만큼 없으면 종료
        print('BUY: ', coin, 'quantity: ',quantity, 'price: ',price,'total: ', quantity * price)
        if self.getBalance(tosell) < quantity:
            print("잔고없엉")
            return
        #주문 넣음
        order = self.binance.create_limit_buy_order(coin,quantity,price)
        #3초 기다렸다가 체결안되면 바로 취소
        time.sleep(3)
        if order['status'] == 'open': # 주문하고 3초지났는데 체결안되면 자동취소
            resp = self.binance.cancel_order(order['info']['orderId'],coin)
            print('BUY',coin,'Canceled')

    def sellCrypto(self,coin,price,quantity=0):
        tosell, tobuy = coin.split('/') #SOL/BNB일 경우 tobuy : BNB, tosell : SOL
        #수량지정을 하지않은 경우 최저 한도 수량으로 정함
        limitquantity = self.binance.markets[coin]['limits']['cost']['min'] * 1.05 / price
        if quantity == 0: quantity = limitquantity
        # 주문 넣기전에 잔고에 그만큼 있는지 확인 그만큼 없으면 종료
        print('SELL: ', coin, 'quantity: ',quantity, 'price: ',price,'total: ', quantity * price)
        if self.getBalance(tosell) < quantity:
            print("잔고없엉")
            return
        #주문 ㄱㄱ
        order = self.binance.create_limit_sell_order(coin,quantity,price)
        print(order)
        #3초 기다렸다가 주문 체결안되면 취소
        time.sleep(3)
        if order['status'] == 'open':
            resp = self.binance.cancel_order(order['info']['orderId'],coin)
            print('SELL',coin,'Canceled')
User = user()
# async def f():
#     uri = 'wss://stream.binance.com:9443/stream?streams=tGNh7JVPg7jdvBOgNUdQiVKmW35hGNzoozYMODbZOhiBlDXA0hyY4mUSLaMT'
#     print(uri)
#     ws = create_connection(uri)
#     print(ws)
#     print("A")
#     while True:
#         print("C")
#         result = await ws.recv()
#         print("B")
#         ws.close()
#         print(result)
if __name__ == '__main__':
    #asyncio.get_event_loop().run_until_complete(f())
    tmp = user()
    print(tmp.getBalance('SOL'))
