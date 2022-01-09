import config
import ccxt
import binance
class user:
    def __init__(self):
        self.APIKEY = config.get_secret('apiKey')
        self.SECRET = config.get_secret('secret')
        self.binance = ccxt.binance({'apiKey' : self.APIKEY, 'secret' : self.SECRET})
        self.balance = self.binance.fetch_balance()
    def getBalance(self):
        self.balance = self.binance.fetch_balance()
        return self.balance
if __name__ == '__main__':
    tmp = user()
    balance = tmp.getBalance()
    for k,v in balance.items():
        print(k,v)