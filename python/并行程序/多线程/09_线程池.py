from concurrent.futures import ThreadPoolExecutor
import time

def fun(a):
    print(a)
    time.sleep(a)

if __name__ == "__main__":
    a=[1,2,3,4,5,6,7,8,9,10]
    with ThreadPoolExecutor(5) as thpool:
        for i in a:
            c=thpool.submit(fun,i)
           

        
