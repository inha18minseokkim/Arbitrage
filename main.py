from fastapi import FastAPI, BackgroundTasks
from typing import Optional
import time
from fastapi.responses import JSONResponse
import numpy as np
import asyncio
from Ticker.Ticker import recv_ticker
from CoinDataManager import coindata,label
from fastapi.middleware.cors import CORSMiddleware
from Determinant import SOLDET
from BinanceAccount import User
origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_app_start() -> None:
    asyncio.create_task(recv_ticker())
    #asyncio.create_task(SOLDET.routine())

@app.on_event("shutdown")
def on_app_shutdown():
    print("BYESERVER")
    
#BTCUSDT 같이 코인 정보를 넣으면 현재 서버에 있는 데이터를 로드해줌
@app.get("/get/{coin}")
def get_item(coin):
    return JSONResponse({"data": [time.time()*1000,coindata.price_data[label[coin.upper()]][-1]]})
#두개 나눈 상대가격 로드
@app.get("/get_relative_price/{coin1}/{coin2}")
def get_relative_price(coin1,coin2):
    return JSONResponse({"data": [time.time()*1000,coindata.get_relative_price(coin1.upper(),coin2.upper()).tolist()]})

#두개 곱한 가격 로드
@app.get("/get_product_price/{coin1}/{coin2}")
def get_product_price(coin1,coin2):
    return JSONResponse({"data": [time.time()*1000,coindata.get_product_price(coin1.upper(),coin2.upper()).tolist()]})

#BTCUSDT/BTCBNB 같이 넣으면 두값을 나눈 상대가격 리스트를 로드
@app.get("/get_relative_pricelist/{coin1}/{coin2}")
def get_relative_pricelist(coin1,coin2):
    return JSONResponse({"data": coindata.get_relative_price(coin1.upper(),coin2.upper()).tolist()})

@app.get("/getlist/{coin}")
def get_item_list(coin):
    return JSONResponse({"data": coindata.price_data[label[coin.upper()]].tolist()})

@app.get("/accountinfo/getbalance")
def get_balance():
    return JSONResponse({"data" : User.getBalance()})