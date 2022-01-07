class Determine:
    def __init__(self):
        self.SOLBTC = 1
        self.SOLBNB = 1
        self.BNBBTC = 1
        self.ratio = 0
    def routine(self):#일단 SOL에 대해서만 적어놓자
        self.ratio = (self.SOLBTC - self.SOLBNB*self.BNBBTC)/(self.SOLBNB*self.BNBBTC)*100
        if self.ratio >= 0.1:
            print("SOLBTC 개비쌈지금")
        if self.ratio <= -0.1:
            print("SOLBNB 개비쌈지금")

SOLDET = Determine()