# !/usr/bin/env python3
import time
import threading
import txtadded
import queue
import os
def worker(i):
    while True:
        item = q.get()
        if item is None:
            break
        txtadded.main(item,"test.png","test")
        print(item + "'s video is made!" ) #show working procedure
        q.task_done()
if __name__ == '__main__':
    num_of_threads = 5 #acclerate the process
    Name_List = ["StephenCurry30", "KyrieIrving", "drose", "DWade", "CP3", "KlayThompson", "KDTrey5", "Dame_Lillard",
                 "KingJames", "AntDavis23"]
    q = queue.Queue()

    threads = []
    start = time.time()

    for item in Name_List:
        q.put(item)
    for i in range(1, num_of_threads + 1):
        t = threading.Thread(target=worker,args=(i,))
        threads.append(t)
        t.start()

    q.join() #when all task finsh , it joins
    

    for i in range(num_of_threads):
        q.put(None)         # to stop workers
    for t in threads:
        t.join()
    f = open("Mylist.txt", 'w')

    for i in Name_List:
        f.write('file ' + "\'" + str(i) + '.mp4' + "\'")
        f.write('\n')
    f.close()
    os.system("ffmpeg -f concat -safe 0 -i Mylist.txt -c copy output.mp4")

    print(threads)
    end = time.time()
    print(end-start) #see how long it takes to finish all assignments
