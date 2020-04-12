"""therading创建线程"""
import threading
import time

def fun(name,t):
    print("start:{0}".format(name))
    time.sleep(t)
    print("end:{0}".format(name))
    
if __name__ == "__main__":
    print("f_start")
    t=threading.Thread(target=fun,args=(1,10))
    t.start()
    print(t.name)
    print(t.is_alive())
    time.sleep(10)
    print("f_end")
#在程序执行到最后如果线程还没有跑完进程会等待，可以在线程daemon设置true进行设置和旧版一样