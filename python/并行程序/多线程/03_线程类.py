
import threading
import time

def fun(name,t):
    print("start:{0}".format(name))
    time.sleep(t)
    print("end:{0}".format(name))

class MyTread(threading.Thread):
    def __init__(self,fun,name,args):
        # threading.Thread.__init__(self,target=fun,name=name,args=args)
        super().__init__()
    
    def fun(self):
        self._target(*self._args)

if __name__ == "__main__":
    print("f_start")
    t=MyTread(fun,"1",(1,10))
    t.start()
    print(t.name)
    print(t.is_alive())
    t.join()
    print(t.is_alive())
    print("f_end")

