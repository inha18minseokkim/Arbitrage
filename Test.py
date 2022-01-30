import asyncio
from binance import AsyncClient, BinanceSocketManager
import config
async def binance_ws_client():
    client = await AsyncClient.create(config.get_secret('apiKey'),config.get_secret('secret'))
    bm = BinanceSocketManager(client)
    us = bm.user_socket()
    async with us as tmp:
        while True:
            res = await us.recv()
            print(res)
asyncio.run(binance_ws_client())

# token = "GTu1KdBDcKuuWJfT3CrC3BRWgJLMn5YECiblvewRtyw3fgX2NpZovSrDHtiy"
# uri = "wss://stream.binance.com:9443/ws/"+token
# async def wsexample():
#     async with websockets.connect(uri) as ws:
#         data = await ws.recv()
#         print(data)
# async def main():
#     await wsexample()
# asyncio.run(main())