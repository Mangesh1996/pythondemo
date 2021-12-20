"""
Converting the video to  frame by handling user
user can chosse the source path and save path

"""
# import the libary to necessary
import os
import tkinter as tk
# import cv2
# import sys
from time import sleep
from tkinter import filedialog
from tqdm import tqdm
import time
from frame_count import frame_count
import datetime

# creating exception to handle error
try:
    root = tk.Tk()
    root.withdraw()
    #specifice the file type when user chose the file
    filetype=(("Mp4 files","*.mp4"),("Window Media Viewer","*.wvm"),("Audio Video Interleave","*.avi"),)
    #make a default path to show user in dialog box
    defalut_path=os.path.join(os.getcwd())
    user_fps=frame_count("source_video/ironmane_fly.mp4")
    #save the path when user chose path using dialog box
    file_path=filedialog.askopenfile(title="Select Video to convert frame",initialdir=defalut_path,filetypes=filetype)
    #select only path name in filedialog box
    sourcepath=file_path.name
    #save path in save_path 
    save_path=filedialog.askdirectory(title="Select Folder to save frames")
    #run the command using os.system 
    start =time.time()
    
    os.system(f"ffmpeg-bar -i {sourcepath} -vf fps={user_fps} {save_path}/img-%03d.jpg ")#ffmped are convert video to frame
    
    end=time.time()
    print("\n")
    print("Video to frame converting done ")
    sec=end-start
    print("task complete duration:- ",str(datetime.timedelta(seconds=sec)))
except Exception:
    print("Your are Not select properly file ")
