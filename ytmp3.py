#!/usr/bin/python

import os
import sys
import click
from pytube import YouTube
from pprint import pprint


try:
        url = sys.argv[1]
except:
        url = raw_input('Insert a YouTube URL: ')

vd = YouTube(url)
title = vd.filename
dst = "$HOME/YTmusic/"

print('Title:' + title)
print('Available codecs and resolutions: ')
pprint(vd.get_videos())

codec = raw_input('Choose an available codec: ')
quality = raw_input('Choose an available resolution: ')

with click.progressbar(label="Extracting audio..", length=100) as bar:
        video = vd.get(codec, quality)
        bar.update(25)
        video.download('/tmp/')
        bar.update(25)
        os.system("mkdir -p " + dst)
        bar.update(10)
        return_code = os.system('ffmpeg -i /tmp/"' + title  + '"' + '.' + codec + ' -qscale:a 0 "' + dst + title + '.mp3" > /dev/null 2>&1')
        bar.update(40)


print('ffmpeg exit with code: '+str(return_code))

os.system("rm /tmp/'" + title + "." + codec+ "'")

if(return_code):
        print("Ops! We've got an error while extracting audio..You should check parameters..")
        exit(1)

print("Audio saved in " + dst)
