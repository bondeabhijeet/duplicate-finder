from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor
import time

def func1():
    print("waiting 3 seconds")
    time.sleep(3)
    print("Done waiting 3 seconds")
    # do something
    pass

def func2():
    print("waiting 5 seconds")
    time.sleep(5)
    print("Done waiting 5 seconds")
    # do something else
    pass

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=2) as executor:
        future1 = executor.submit(func1)
        future2 = executor.submit(func2)
        # wait for the futures to complete
        future1.result()
        future2.result()