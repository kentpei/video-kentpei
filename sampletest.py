from time import ctime
import threading
import txtadded
import tweetinfo
import glob
import subprocess
import os


def threads():
    thread_list = []
    txt1 = tweetinfo.get_all_tweets("StephenCurry30", 3)
    txt2 = tweetinfo.get_all_tweets("KyrieIrving", 3)
    txt3 = tweetinfo.get_all_tweets("drose", 3)
    t1 = threading.Thread(target=txtadded.video, args=('curry.png', txt1, "curry"))
    t2 = threading.Thread(target=txtadded.video, args=('kyrie.png', txt2, "kyrie"))
    t3 = threading.Thread(target=txtadded.video, args=('Rose.png', txt3, "Rose"))
    thread_list.append(t1)
    thread_list.append(t2)
    thread_list.append(t3)

    # os.remove(directory+"/" + filename)

    for t in thread_list:
        t.setDaemon(True)  # 设置为守护线程
        t.start()
        t.join()  # 在这个子线程完成运行之前，主线程将一直被阻塞

if __name__ == '__main__':
    '''
    threads()
    os.system(
            "ffmpeg -r 1 -f image2 -s 1920x1080 -start_number 1 -i curry%02d.png -vframes 1000 -vcodec libx264 -crf 25  -pix_fmt yuv420p curry.mp4")
    os.system(
            "ffmpeg -r 1 -f image2 -s 1920x1080 -start_number 1 -i Kyrie%02d.png -vframes 1000 -vcodec libx264 -crf 25  -pix_fmt yuv420p Kyrie.mp4")
    os.system(
            "ffmpeg -r 1 -f image2 -s 1920x1080 -start_number 1 -i Rose%02d.png -vframes 1000 -vcodec libx264 -crf 25  -pix_fmt yuv420p Rose.mp4")
    '''
    #os.system("ffmpeg -i " + "concat:curry.mp4|Kyrie.mp4" + " -codec copy output.mp4")
    os.system("ffmpeg -f concat -safe 0 -i list.txt -c copy final.mp4")
    #os.system("ffmpeg -i " + "concat:curry.mp4|Kyrie.mp4" +"-codec copy final.mp4")