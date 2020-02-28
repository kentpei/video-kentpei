#!/usr/bin/env python
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import tweetinfo
import re
import os
import subprocess
'''
img = Image.new('RGB', (100, 30), color=(0, 0, 0))
img = 
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello World", fill=(0, 0, 0))
'''
def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)
    return lines
def video(png,text,key):
    folder = os.path.exists('pictures')
    if not folder:
        os.makedirs('pictures')
    for i in range(len(text)):

        image = Image.open(png)
        image_size = image.size
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', size=50,encoding='utf-8')
        emoji_pattern = re.compile("["
                                    u"\U0001F600-\U0001F64F"  # emoticons
                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                    "]+", flags=re.UNICODE)
        text[i] = emoji_pattern.sub(r'', text[i])
        lines = text_wrap(text[i], font, image_size[0])
        color = 'rgb(0, 0, 0)'  # black color
        line_height = font.getsize('hg')[1]
        (x, y) = (0, int(image_size[0])//2)
        for line in lines:
            # draw the line on the image
            draw.text((x, y), line, fill=color, font=font)

            # update the y position so that we can use it for next line
            y = y + line_height
        # save the image
        path = "./pictures/"
        #files = path + "*.png"
        #ffmpeg.input(files, pattern_type='glob', framerate=0.3 * self.num_threads).output('dailyfeed.mov').run()
        image.save(path+str(key)+'0'+ str(i+1) +'.png', optimize=True)
