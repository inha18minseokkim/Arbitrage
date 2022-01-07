class Determine:
    def __init__(self):
        self.SOLBTC = 1
        self.SOLBNB = 1
        self.BNBBTC = 1
        self.ratio = 0
    async def routine(self):
        self.ratio = (self.SOLBTC - self.SOLBNB*self.BNBBTC)/(self.SOLBNB*self.BNBBTC)*100
        if self.ratio >= 0.1:
            print("SOLBTC 개비쌈지금")
        if self.ratio <= -0.1:
            print("SOLBNB 개비쌈지금")
SOLDET = Determine()