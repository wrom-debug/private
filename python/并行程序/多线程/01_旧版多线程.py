import _thread
import time

def fun_th(a):
    print("start:{0}".format(a))
    time.sleep(1)
    print("end:{0}".format(a))

if __name__ == "__main__":
    print("start")
    th1=_thread.start_new_thread(fun_th,("a",))
    th2=_thread.start_new_thread(fun_th,("b",))
    time.sleep(3)
    print("end")
    # 主线程时间要比子线程时间长