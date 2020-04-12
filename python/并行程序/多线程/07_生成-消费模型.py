""" 线程中也有queue队列，使用队列大小判断线程是否执行相关
操作
 """
import time
import threading
from queue import Queue

def scz():
    cp=0
    global q
    while True:
        if q.qsize()<1000:
            for i in range(100):
                cp+=1
                sp="商品 id："+str(cp)
                print("正在生产："+sp)
                time.sleep(1)
                q.put(sp)
        time.sleep(2)

def xfz():
    global q
    while True:
        if q.qsize()>20:
            for i in range(10):
                hw=q.get()
                print("正在消费："+hw)
                time.sleep(1)
        time.sleep(2)

if __name__ == "__main__":
    q=Queue()
    sc=threading.Thread(target=scz)
    xf=threading.Thread(target=xfz)
    sc.start()
    time.sleep(0.5)
    xf.start()