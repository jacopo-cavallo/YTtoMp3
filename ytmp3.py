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

click.secho('Title:',nl=False, fg='green')
click.secho(' '+title, bold=True, fg='blue')

click.secho('Available codecs and resolutions:',fg='green')
pprint(vd.get_videos())

click.secho('Choose an available codec (e.g. \'mp4\'): ', nl=False, fg='green')
codec = raw_input()
click.secho('Choose an available resolution (e.g. \'720p\'): ', nl=False, fg='green')
quality = raw_input()


with click.progressbar(label="Extracting audio..", length=100) as bar:
        video = vd.get(codec, quality)
        bar.update(25)
        
        video.download('/tmp/')
        bar.update(25)
        
        os.system("mkdir -p " + dst)
        bar.update(10)
        
        return_code = os.system('ffmpeg -i /tmp/"' + title  + '"' + '.' + codec + ' -qscale:a 0 "' + dst + title + '.mp3" > /dev/null 2>&1')
        bar.update(40)
        

click.secho('ffmpeg exit with code: '+str(return_code), fg='green')

os.system("rm /tmp/'" + title + "." + codec+ "'")

if(return_code):
        click.secho("Ops! We've got an error while extracting audio..You should check parameters..", bg='red', fg='white', bold=True)
        exit(1)

click.secho("Audio saved in " + dst, bold=True, fg='blue')
                                                                                                                                                                              53,58         Fon
