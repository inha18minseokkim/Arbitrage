from BinanceAccount import User
import asyncio
import threading
from Declaration import label
class Determine:
    def __init__(self):
        self.curPrice = [1 for i in range(len(label.keys()))]
        # self.SOLBTC = 1
        # self.SOLBNB = 1
        # self.BNBBTC = 1
        # self.ratio = 0
    def routine(self):#일단 SOL에 대해서만 적어놓자
        #SOLBNB부분
        SOLBTC = self.curPrice[label['SOLBTC']]
        SOLBNB = self.curPrice[label['SOLBNB']]
        BNBBTC = self.curPrice[label['BNBBTC']]
        ratio = (SOLBTC - SOLBNB*BNBBTC)/(SOLBNB*BNBBTC)*100
        if SOLBTC == 1 or SOLBNB == 1 or BNBBTC == 1: return
        #이거 일단 리퀘스트 받는 타이밍이 달라서 가격 받아오지도 않았는데 매수타이밍 잡을 수도 있으니 임시로 이렇게 함
        #나중에 좀더 공부해서 좋은방법이 있으면 바꿀것
        if ratio >= 0.08:
            print("SOLBTC 개비쌈지금")
            threading.Thread(target=User.buyCrypto, args=('SOL/BNB',SOLBNB)).start()
        if ratio <= -0.04:
            print("SOLBNB 개비쌈지금")
            threading.Thread(target=User.sellCrypto, args=('SOL/BNB',SOLBNB)).start()
        #SOLBNB부분끝

DET = Determine()