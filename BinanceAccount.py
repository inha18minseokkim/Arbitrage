import config
import ccxt
import asyncio
import time
import logging
class user:
    def __init__(self):
        self.APIKEY = config.get_secret('apiKey')
        self.SECRET = config.get_secret('secret')
        self.binance = ccxt.binance({'apiKey' : self.APIKEY, 'secret' : self.SECRET})
        self.balance = self.binance.fetch_balance()
    def getBalance(self):
        self.balance = self.binance.fetch_balance()
        return {'free': self.balance['free'], 'used' : self.balance['used'], 'total' : self.balance['total']}
    def buyCrypto(self,coin,price,quantity=0): # threading.Thread(tmp.buyCrypto,args=('SOL/BNB',0,0.295))).start() 이렇게 호출하면됨
        tobuy, tosell = coin.split('/') #SOL/BNB인 경우 tobuy는 SOL tosell은 BNB tobuy:살거, tosell: 팔거
        #수량지정을 하지않은경우 최저 한도 수량으로 정함
        limitquantity = self.binance.markets[coin]['limits']['cost']['min']*1.1/price
        if quantity == 0: quantity = limitquantity
        #주문 넣기전에 잔고에 그만큼 있는지 확인 그만큼 없으면 종료
        if self.getBalance()['free'][tosell] < quantity:
            print("잔고없엉")
            return
        #주문 넣음
        print('BUY',coin,quantity,price,quantity*price)
        order = self.binance.create_limit_buy_order(coin,quantity,price)
        #3초 기다렸다가 체결안되면 바로 취소
        time.sleep(5)
        if order['status'] == 'open': # 주문하고 3초지났는데 체결안되면 자동취소
            resp = self.binance.cancel_order(order['info']['orderId'],coin)
            print('BUY',coin,'Canceled')

    def sellCrypto(self,coin,price,quantity=0):
        tosell, tobuy = coin.split('/') #SOL/BNB일 경우 tobuy : BNB, tosell : SOL
        #수량지정을 하지않은 경우 최저 한도 수량으로 정함
        limitquantity = self.binance.markets[coin]['limits']['cost']['min'] * 1.1 / price
        if quantity == 0: quantity = limitquantity
        # 주문 넣기전에 잔고에 그만큼 있는지 확인 그만큼 없으면 종료
        if self.getBalance()['free'][tosell] < quantity:
            print("잔고없엉")
            return
        #주문 ㄱㄱ
        print('SELL', coin, quantity, price, quantity * price)
        order = self.binance.create_limit_sell_order(coin,quantity,price)
        print(order)
        #3초 기다렸다가 주문 체결안되면 취소
        time.sleep(5)
        if order['status'] == 'open':
            resp = self.binance.cancel_order(order['info']['orderId'],coin)
            print('SELL',coin,'Canceled')
User = user()
if __name__ == '__main__':
    tmp = user()
    print(tmp.balance)
    asyncio.run(tmp.buyCrypto('SOL/BNB',0,0.295))
    #print(tmp.binance.markets['SOL/BNB']['limits']['cost']['min']*1.01/0.296)
    print(tmp.getBalance())
