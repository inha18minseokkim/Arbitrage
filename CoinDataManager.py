import numpy as np
from typing import List,Dict
from Determinant import SOLDET
label: Dict = {'BTCUSDT': 0, 'ETHUSDT': 1, 'BNBBTC': 2, 'SOLBTC' : 3, 'SOLBNB' : 4}

max_arr_size = 20 #데이터로 저장할 코인 가격 리스트 최대 수. 넘어가면 버린다
truncate_size = 7 #가장 최근 데이터 이만큼 살리고 나머지 버린다.
class CoinData:
    def __init__(self):
        self.price_data: List = [np.array([]) for i in range(len(label.keys()))]
        #self.price_volume: List = [np.array([]) for i in range(2)]
    def data_order(self):
        for i in range(len(label.keys())):
            if len(self.price_data[i]) >= max_arr_size:
                self.price_data[i] = self.price_data[i][-truncate_size:]
    def get_relative_pricelist(self,c1,c2):
        if c1 not in label or c2 not in label: return
        print("get_relative_price: c1 c2 까지는 잘 입력함")
        if len(self.price_data[label[c1]]) < truncate_size or len(self.price_data[label[c2]]) < truncate_size: return
        print("사이즈 다참")
        return self.price_data[label[c1]][-truncate_size:]/self.price_data[label[c2]][-truncate_size:]
    def get_relative_price(self,c1,c2):
        if c1 not in label or c2 not in label: return
        return self.price_data[label[c1]][-1]/self.price_data[label[c2]][-1]
    def get_product_price(self,c1,c2):
        if c1 not in label or c2 not in label: return
        return self.price_data[label[c1]][-1]*self.price_data[label[c2]][-1]

#싱글톤패턴을 사용하며 인스턴스는 무조건 하나만 만들도록
coindata = CoinData()
