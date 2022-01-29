#공통적으로 사용되는 전역변수 가급적 여기다가 다 꼬라박고 import 시키자

marketlabel = {'BTCUSDT': 0, 'ETHUSDT': 1, 'BNBBTC': 2, 'SOLBTC' : 3, 'SOLBNB' : 4, 'ETHBTC': 5}
label = {'BTC':0 , 'ETH':1, 'BNB': 2, 'SOL' : 3 ,'USDT': 4}
max_arr_size = 10 #데이터로 저장할 코인 가격 리스트 최대 수. 넘어가면 버린다
truncate_size = 7 #가장 최근 데이터 이만큼 살리고 나머지 버린다.