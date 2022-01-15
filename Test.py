import asyncio
import time
import threading
def a():
    print("A")
    time.sleep(2)
    print("B")
    time.sleep(1)
    print("X")

if __name__ == "__main__":
    t = threading.Thread(target=a).start()
    print("C")