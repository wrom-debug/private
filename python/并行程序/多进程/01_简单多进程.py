"""创建多个进程,并传参数，调用属性"""
from multiprocessing import Process
from time import sleep
def run_proc(name,**a):
    print("start:{0}".format(name))
    print(a)
    sleep(10)
    print("end:{0}".format(name))
    return 

if __name__ == "__main__":
    print("f_start")
    p1=Process(target=run_proc,args=("p1",),name="p1",kwargs={"1":"ccc"})
    p1.start()
    """
    p2=Process(target=run_proc)
    p2.start()
    p3=Process(target=run_proc)
    p3.start()
    """
    
    print(p1.name)
    print(p1.pid)
    print(p1.is_alive())
    p1.join()
    
    print("f_end")