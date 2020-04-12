""""""
import time
import threading

NUM=0
lock=threading.Lock()
def fun(name,t):
    global NUM
    print("start:{0}".format(name))
    # lock.acquire()
    for i in range(t):
        lock.acquire()
        NUM+=1
        lock.release()
        # print(name)
    print(NUM)
    # lock.release()
    print("end:{0}".format(name))

if __name__ == "__main__":
    t1=threading.Thread(target=fun,args=(1,100000))
    t2=threading.Thread(target=fun,args=(2,100000)) 
    print(lock.release())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
#将锁放在循环外相当t1先运行，t2再运行，将锁放在写入部分外才正常保证每次写入成功