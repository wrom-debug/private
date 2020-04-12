""""""
from multiprocessing import Process
import time

class ClockProcess(Process):
    def __init__(self,data):
        super().__init__() 
        
        # Process.__init__(self) 
        self.data=data
        
    def run(self):
        print("statr:{0}".format(time.ctime()))
        time.sleep(self.data)
        print("end:{0}".format(time.ctime()))
        
if __name__ == "__main__":
    print("f_statr")
    p=ClockProcess(10)
    p.start()
    p.join()
    print("f_end")
