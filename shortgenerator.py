import os
import re
import random
from moviepy.editor import *

def get_shortest_clip(videolist: list, path):
    min_clip = VideoFileClip(path + videolist[0],target_resolution=(1920,1080))
    min_index = 0
    for i, video in enumerate(videolist):
        clip = VideoFileClip(path + video,target_resolution=(1920,1080))
        if clip.duration < min_clip.duration:
            min_clip = clip
            min_index = i
    return min_clip, min_index

def shortgenerator():
    path = "G:/videos/"
    pathused = "G:/videos/used/"
    output_path = "G:/shorts/"
    clips = []
    usedVideos = []
    duration = 0
    shortlength = 60
    shortname = "finshort"
    filename = "finshort0.mp4"

    #get all videos in folder
    videolist = os.listdir(path)
    for i in videolist:
        if not re.search(".*.mp4", i):
            videolist.remove(i)

    if len(videolist) == 0:
        exit("no videos found")

    #append clips until video length reached
    while duration <= shortlength:
        if len(videolist) == 0:
            break
        clip, min_index = get_shortest_clip(videolist, path)
        clips.append(clip)
        usedVideos.append(videolist.pop(min_index))
        duration = 0
        for clip in clips:
            duration += clip.duration

    #name file
    counter = 0
    while filename in os.listdir(output_path):
        counter += 1
        filename = f"{shortname}{counter}.mp4"

    #concat clips add text and write file
    concat_clip = concatenate_videoclips(clips=clips, method="compose" )
    txt_clip = TextClip("gagreflexlol", fontsize=75, color="white").set_position(("center",0.7), relative=True).set_duration(concat_clip.duration)
    clip = CompositeVideoClip(bg_color=(0,0,0), clips=[concat_clip,txt_clip])
    clip.write_videofile(output_path + filename,threads=8, fps=30)

    #delete usedVideos  // not working anymore because clip open in different Process :(
    #for usedVideo in usedVideos:
    #    os.remove(path + usedVideo)