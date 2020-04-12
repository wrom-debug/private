
import threading
local=threading.local()
def fun(name):
    print(name+":1")
    local.name=name
    fun_1di()

def fun_1di():
    name=local.name
    print("2:"+name)


if __name__ == "__main__":
    t1=threading.Thread(target=fun,args=("a",))
    t2=threading.Thread(target=fun,args=("b",))
    t1.start()
    t1.join
    t2.start()