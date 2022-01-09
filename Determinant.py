class Determine:
    def __init__(self):
        self.SOLBTC = 1
        self.SOLBNB = 1
        self.BNBBTC = 1
        self.ratio = 0
    def routine(self):#일단 SOL에 대해서만 적어놓자
        self.ratio = (self.SOLBTC - self.SOLBNB*self.BNBBTC)/(self.SOLBNB*self.BNBBTC)*100
        if self.SOLBTC == 1 or self.SOLBNB == 1 or self.BNBBTC == 1: return
        #이거 일단 리퀘스트 받는 타이밍이 달라서 가격 받아오지도 않았는데 매수타이밍 잡을 수도 있으니 임시로 이렇게 함
        #나중에 좀더 공부해서 좋은방법이 있으면 바꿀것
        if self.ratio >= 0.1:
            print("SOLBTC 개비쌈지금")
        if self.ratio <= -0.1:
            print("SOLBNB 개비쌈지금")

SOLDET = Determine()