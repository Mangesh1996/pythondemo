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
# creating exception to handle error
try:
    root = tk.Tk()
    root.withdraw()
    #specifice the file type when user chose the file
    filetype=(("Mp4 files","*.mp4"),("Window Media Viewer","*.wvm"),("Audio Video Interleave","*.avi"),("Matroska Multimedia Container","*.mkv"),)
    #make a default path to show user in dialog box
    defalut_path=os.path.join(os.getcwd())
    user_fps=frame_count("source_video/ironmane_fly.mp4")
    #save the path when user chose path using dialog box
    file_path=filedialog.askopenfile(title="Select Video to convert frame",initialdir=defalut_path,filetypes=filetype)
    #select only path name in filedialog box
    sourcepath=file_path.name
    print(sourcepath)
    #save path in save_path 
    save_path=filedialog.askdirectory(title="Select Folder to save frames")
    #run the command using os.system 
    start =time.time()
    fp=frame_count("source_video/ironmane_fly.mp4")
    cmd = [
    "ffmpeg", "-i", "source_video/ironmane_fly.mp4", "-vf", "fps=1", "frame_dire/img-%03d.jpg",]
    cmd[4]="fps="+str(fp)
    cmd[2]=sourcepath
    cmd[5]=save_path+"/img-%03d.jpg"

    ff = FfmpegProgress(cmd)
    with tqdm(total=100, position=0, desc="Converting....") as pbar:
        for progress in ff.run_command_with_progress():
            pbar.update(progress - pbar.n)
    
    end=time.time()
    print("\n")
    print("Video to frame converting done ")
    sec=end-start
    print("task complete duration:- ",str(datetime.timedelta(seconds=sec)))
except Exception:
    print("Your are Not select properly file ")
