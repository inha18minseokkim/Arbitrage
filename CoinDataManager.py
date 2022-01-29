import numpy as np
from typing import List,Dict
from Determinant import DET
from Declaration import marketlabel,max_arr_size,truncate_size


class CoinData:
    def __init__(self):
        self.price_data: List = [np.array([]) for i in range(len(marketlabel.keys()))]

    def data_order(self):#Ticker에서 recv_ticker로 가격데이터 받아온다음에 데이터로 응애 하는 작업 여기다 적어줘
        for k,v in marketlabel.items():#차익거래 관련된 정보(최신 가격)을 Determinant 객체에 넘겨줌
            if (len(self.price_data[v] != 0)):
                DET.curPrice[v] = self.price_data[v][-1]
        for i in range(len(marketlabel.keys())):#max_arr_size 보다 많이 데이터가 쌓이면 truncate_size만큼 남기고 가장 오래된 데이터는 다 잘라버려
            if len(self.price_data[i]) > max_arr_size:
                self.price_data[i] = self.price_data[i][-truncate_size:]
        DET.routine()#Determinant 깨워서 가격 변했으니 비교해보고 사거나 팔만한거 있으면 주문넣으라고 함

    def get_relative_pricelist(self,c1,c2):
        if c1 not in marketlabel or c2 not in marketlabel: return
        print("get_relative_price: c1 c2 까지는 잘 입력함")
        if len(self.price_data[marketlabel[c1]]) < truncate_size or len(self.price_data[marketlabel[c2]]) < truncate_size: return
        print("사이즈 다참")
        return self.price_data[marketlabel[c1]][-truncate_size:] / self.price_data[marketlabel[c2]][-truncate_size:]
    def get_relative_price(self,c1,c2):
        if c1 not in marketlabel or c2 not in marketlabel: return
        return self.price_data[marketlabel[c1]][-1] / self.price_data[marketlabel[c2]][-1]
    def get_product_price(self,c1,c2):
        if c1 not in marketlabel or c2 not in marketlabel: return
        return self.price_data[marketlabel[c1]][-1] * self.price_data[marketlabel[c2]][-1]

#싱글톤패턴을 사용하며 인스턴스는 무조건 하나만 만들도록
coindata = CoinData()
