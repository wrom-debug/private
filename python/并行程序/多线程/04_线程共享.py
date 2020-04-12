""""""
import time
import threading

NUM=0

def fun(name,t):
    global NUM
    print("start:{0}".format(name))
    for i in range(t):
        NUM+=1
    print(NUM)
    print("end:{0}".format(name))

if __name__ == "__main__":
    t1=threading.Thread(target=fun,args=(1,100000))
    t2=threading.Thread(target=fun,args=(2,100000)) 
    t1.start()
    t2.start()
    t1.join()
   
    t2.join()
#组数据过大时会导致数据复习的发生