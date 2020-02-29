# Video-kentpei
video-kentpei created by GitHub Classroom
# technology 
1.Python3.7  
2.Tweppy(Twitter API)  
3.ffmpeg  
# Design
 ![image](https://github.com/kentpei/miniproject3/blob/master/arch.JPG)
# Description
1.Set 10 twitter_user in a list,put them in the queue.  
2.get the twitter_user one by one and use tweepy API to get each text from the user.
![image](https://github.com/kentpei/miniproject3/blob/master/screenshot.png)
3.add the text into pictures and use ffmpeg to form videos.After transforming,delete the pics we used before.  
![image](https://github.com/kentpei/miniproject3/blob/master/screenshot1.png)
4.intergrate all the videos we get
![image](https://github.com/kentpei/miniproject3/blob/master/screenshot2.png)
# main function explain
1.tweetinfo python file is to produce text we needed to add into pictures.  
2.txtadded python file is to add text into pictures and delete emoji or other illegal words in 'UTF-8'.  
3.imagetovideo python file is to transfer pictures to videos using ffmpeg.  
4.threads python file is to using queue and threads to process the imagetovideo part and produce all videos.  
# Homework part
1. How many API calls you can handle simultaneously and why?  
I call one API Tweepy.  
2. For example, run different API calls at the same time?  
I think I can run defferent API calls at the same time.
3. Split the processing of an API into multiple threads?
I split the process to 3 threads.
