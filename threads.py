# !/usr/bin/env python3


import time
import queue
import threading
import imagetovideo
import os
Name_List = ['BU_ece', 'BU_CCD', 'BU_CAS', 'BU_Tweets','kobebryant','DCBatman',
            'DCSuperman', "DWade", "CP3", 'LinkedIn']


num_threads = 3# Build threads
threads = []
q = queue.Queue()   # build queue


def worker():
    while True:
        item = q.get()
        qSize = q.qsize()
        if item is None:
            print("No item!")
            break
        print("Currently process on " + item)
        imagetovideo.imgToVideo("test.png", item, "test")
        print("Current worker is finished.")
        q.task_done()
start = time.time()
for item in Name_List:
    q.put(item)
# how to wait for enqueued tasks to be completed
# reference: https://docs.python.org/2/library/queue.html
for i in range(num_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()     #when all task finsh , it joins


# put threads in queue
for i in range(num_threads):
    q.put(None)
# join thread in threads list
for j in threads:
    t.join()
path = "./pictures/videos/"
os.chdir(path)
f = open("Mylist.txt", 'w')
for i in Name_List:
    f.write('file ' + "\'" + str(i) + '.mp4' + "\'")
    f.write('\n')
f.close()
os.system("ffmpeg -f concat -safe 0 -i Mylist.txt -c copy output.mp4")
print(threads)
end = time.time()
print(end - start)  # see how long it takes to finish all assignments
