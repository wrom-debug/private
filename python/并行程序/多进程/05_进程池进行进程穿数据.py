import time
from multiprocessing import Manager,Pool
""" 
def run_proc(q,name):
    print("start:{0}".format(name))
    a=int(q.get())
    print(str(name)+":"+str(a))
    q.put(str(a+1))
    print("end:{0}".format(name))

if __name__ == "__main__":
    p=Pool(3)
    q=Manager().Queue(1)
    q.put("0")
    for i in range(5):
        p.apply_async(run_proc,(q,i))
    p.close()
    p.join()
    print("end")
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
    q=Manager().Queue()
    p=Pool(3)
    p.apply_async(writeq,(q,))
    p.apply_async(readq,(q,))
    p.close()
    p.join()
    print("end")