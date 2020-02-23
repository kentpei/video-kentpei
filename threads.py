# !/usr/bin/env python3
import time
import threading
import txtadded
import queue
def worker():
    while True:
        item = q.get()
        if item is None:
            break
        txtadded.main(item,"test.png","test")
        print(item + "'s video is made!" ) #show working procedure
        q.task_done()
if __name__ == '__main__':
    num_of_threads = 10 #acclerate the process
    Name_List = ["StephenCurry30", "KyrieIrving", "drose", "DWade", "CP3", "KlayThompson", "KDTrey5", "Dame_Lillard",
                 "KingJames", "AntDavis23"]

    q = queue.Queue()

    threads = []
    start = time.time()

    for i in range(1, num_of_threads + 1):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for item in Name_List:
        q.put(item)

    q.join() #when all task finsh , it joins

    for i in range(num_of_threads):
        q.put(None)         # to stop workers
    for t in threads:
        t.join()
    print(threads)
    end = time.time()
    print(end-start) #see how long it takes to finish all assignments
