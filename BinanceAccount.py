import config
import ccxt
import binance
import asyncio
class user:
    def __init__(self):
        self.APIKEY = config.get_secret('apiKey')
        self.SECRET = config.get_secret('secret')
        self.binance = ccxt.binance({'apiKey' : self.APIKEY, 'secret' : self.SECRET})
        self.balance = self.binance.fetch_balance()
    def getBalance(self):
        self.balance = self.binance.fetch_balance()
        return {'free': self.balance['free'], 'used' : self.balance['used'], 'total' : self.balance['total']}
    async def buyCrypto(self,coin,quantity,price):
        order = binance.create_limit_buy_order(coin,quantity,price)
        print(order)
        asyncio.sleep(1000)
        if order['info']:
            resp = binance.cancel_order(order['info']['orderId'],coin)
            print(resp)
    async def sellCrypto(self,coin,quantity,price):
        order = binance.create_test_order(coin,quantity,price)
        print(order)
        asyncio.sleep(1000)
        if order['info']:
            resp = binance.cancel_order(order['info']['orderId'],coin)
            print(resp)
User = user()
if __name__ == '__main__':
    tmp = user()
    asyncio.run(tmp.buyCrypto('SOLBNB',0.2,0.001))
    print(tmp.getBalance())
