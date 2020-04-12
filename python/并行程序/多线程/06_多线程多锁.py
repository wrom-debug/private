import time
import threading
lock1=threading.Lock()
lock2=threading.Lock()
lock3=threading.Lock()
lock2.acquire()
lock3.acquire()
def fun1():
    while 1:
        lock1.acquire()
        print("1")
        time.sleep(1)
        lock2.release()

def fun2():
    while 1:
        lock2.acquire()
        print("2")
        time.sleep(1)
        lock3.release()

def fun3():
    while 1:
        lock3.acquire()
        print("3")
        time.sleep(1)
        lock1.release()


if __name__ == "__main__":
    t1=threading.Thread(target=fun1)
    t2=threading.Thread(target=fun2)
    t3=threading.Thread(target=fun3)
    t1.start()
    t2.start()
    t3.start()


    # 再一个方法要写多个共享数据时应防止线程a锁线程b的某部，线程b锁线程a的某部
    