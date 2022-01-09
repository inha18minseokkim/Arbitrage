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
        return {'free': self.balance['free'], 'used' : self.balance['used'], 'total' : self.balance['total']}
User = user()
if __name__ == '__main__':
    tmp = user()
    print(tmp.getBalance())
