"""创建多个进程间传数据"""
from multiprocessing import Process
from multiprocessing import Queue
import time
def run_proc(q,name):
    print(name)
    print("start:{0}".format(time.ctime()))
    a=int(q.get())
    print(a)
    q.put(str(a+1))
    time.sleep(10)
    print("end:{0}".format(time.ctime()))
    return 

if __name__ == "__main__":
    print("f_start")
    q=Queue(1)
    q.put("1")
    p1=Process(target=run_proc,args=(q,"p1"))
    p1.start()
    p1.join()
    p2=Process(target=run_proc,args=(q,"p2"))
    p2.start()
    p2.join()
    print(q.get())
    print("f_end") 
"""     
def writeq(q):
    for i in ["a","b","c"]:
        print("写入：{0}".format(i))
        q.put(i)
        time.sleep(1)

def readq(q):
    while not q.empty():
        print("读取："+q.get())
        time.sleep(1)

if __name__ == "__main__":
    q=Queue()
    p1=Process(target=writeq,args=(q,))
    p2=Process(target=readq,args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print("end")
 """