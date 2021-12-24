"""
Converting the video to  frame by handling user
user can chosse the source path and save path

Usage : convert video file to image using ffmpeg also add progess bar for user interaction 

github link for ffmpeg_progress_yield :- https://github.com/Tatsh/ffmpeg-progress

"""
# import the libary to necessary
import os
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm
import time
from frame_count import frame_count
import datetime
from tqdm import tqdm
from ffmpeg_progress_yield import FfmpegProgress
from frame_count import frame_count
from glob import glob

def covert_video_frame(path,save_path,frame):
    # creating exception to handle error
    try:
        name=path.split("/")[-1].split(".")[0]     
        save_path=os.path.join(save_path,name)
        start = time.time()
        
        cmd = [
            "ffmpeg", "-i", "source_path/ironmane_fly.mp4", "-vf", "fps=1", "frame_dire/img-%03d.jpg", ]
        cmd[4]="fps="+frame
        
        cmd[5] = save_path+"/img-%03d.jpg"
        uni = [0, ]
        ff = FfmpegProgress(cmd)
        with tqdm(total=100, position=0, desc="Converting....") as pbar:
            for progress in ff.run_command_with_progress():
                pbar.update(progress - pbar.n)
                uni.insert(1, progress)
                uni.pop(0)
                print(uni)

        end = time.time()
        print("\n")
        print("Video to frame converting done ")
        sec = end-start
        print("task complete duration:- ", str(datetime.timedelta(seconds=sec)))
    except Exception:
        print("Your are Not select properly file ")


if __name__=="__main__":
    
    sourcepath=glob("source_path/*")
    save_path="save"
    for path in sourcepath:
        covert_video_frame(path,save_path,1)
