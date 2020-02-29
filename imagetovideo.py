import os
import subprocess
import txtadded
import tweetinfo
import glob

def delete_pictures(path):
    paths = glob.glob(os.path.join(path, '*.png'))
    for file in paths:
        os.remove(file)
def imgToVideo(png,name,key):
    text = tweetinfo.get_all_tweets(name, 3)
    txtadded.video(png, text, key)
    path = "./pictures/"
    #files = path + "*.png"
    #ffmpeg.input(files, pattern_type='glob', framerate=1).output(str(name)+".mp4").run()
    #os.remove("pictures")
    os.chdir(path)
    folder = os.path.exists('videos')
    if not folder:
        os.makedirs('videos')
    path1 = "./videos/"
    paths = glob.glob(os.path.join(path1, str(name) + '.mp4'))
    for file in paths:
        os.remove(file)
    os.system("ffmpeg -r 1 -f image2 -s 1920x1080 -start_number 1 -i " + str(key) +"%02d.png -vframes 1000 -vcodec libx264 -crf 25  -pix_fmt yuv420p "+ './videos/' + str(name) +".mp4 &" )
    delete_pictures(path)
    os.chdir("..")
    return
#main("StephenCurry30","test.png","test")
#imgToVideo("test.png","KingJames","test")
def main():
    return 0
