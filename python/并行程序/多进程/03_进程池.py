import multiprocessing
import time

def func(abc):
    print("statr:{0}".format(abc))
    time.sleep(abc)
    print("end:{0}".format(abc))

if __name__ == "__main__":
    pool=multiprocessing.Pool(processes=2)
    for i in range(10):
        pool.apply_async(func,(i,))
    pool.close()
    pool.join()
    print("end")
