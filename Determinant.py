from BinanceAccount import User
import asyncio
import threading
from Declaration import marketlabel, label,truncate_size,max_arr_size
from typing import List
import numpy as np
class Determine:
    def __init__(self):
        self.curPrice = [1 for i in range(len(marketlabel.keys()))]
        self.price_data_ratio: List = [np.array([]) for i in range(len(label.keys()))]
        self.price_data_std: List = [0 for i in range(len(label.keys()))]
    def routine(self):#일단 SOL에 대해서만 적어놓자
        #SOLBNB부분 SOLBNB vs BNBBTC * BTCBNB
        self.routineForThreeCoin('SOL','BNB','BTC')
        #SOLBNB부분끝
        #ETHUSDT부분, ETHUSDT vs ETHBTC * BTCUSDT
        self.routineForThreeCoin('ETH','BTC','USDT')
        #ETHUSDT부분 끝
    def routineForThreeCoin(self,coin1,coin2,coin3): #SOL BNB BTC
        FISRST = self.curPrice[marketlabel[coin1+coin3]]
        SECOND = self.curPrice[marketlabel[coin1+coin2]]
        THIRD = self.curPrice[marketlabel[coin2+coin3]]
        ratio = (FISRST - SECOND * THIRD) / (SECOND * THIRD) * 100
        np.append(self.price_data_ratio[label[coin1]], ratio)
        if len(self.price_data_ratio[label[coin1]]) >= max_arr_size:
            self.price_data_std[label[coin1]] = np.std(self.price_data_ratio[label[coin1]])
            self.price_data_ratio[label[coin1]] = self.price_data_ratio[label[coin1]][-truncate_size:]
        if FISRST == 1 or SECOND == 1 or THIRD == 1: return
        # 이거 일단 리퀘스트 받는 타이밍이 달라서 가격 받아오지도 않았는데 매수타이밍 잡을 수도 있으니 임시로 이렇게 함
        # 나중에 좀더 공부해서 좋은방법이 있으면 바꿀것
        if ratio >= 0.075 + self.price_data_std[label['SOL']]:
            print(f'{coin1+coin3} 개비쌈지금')
            threading.Thread(target=User.sellCrypto, args=(f'{coin1}/{coin3}', FISRST)).start()
            threading.Thread(target=User.buyCrypto, args=(f'{coin1}/{coin2}', FISRST)).start()
        if ratio <= -0.075 - self.price_data_std[label['SOL']]:
            print(f"{coin1+coin2} 개비쌈지금")
            threading.Thread(target=User.buyCrypto, args=(f'{coin1}/{coin3}', SECOND)).start()
            threading.Thread(target=User.sellCrypto, args=(f'{coin1}/{coin2}', SECOND)).start()
DET = Determine()