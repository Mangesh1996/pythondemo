"""
Converting Video to image 

usage:- add souce file and define destation directory

"""

#import os and glob
import os
from glob import glob

#making the function if save path not present 
def create_dir(save_path):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
    except OSError:
        print(f"Error : creating directory with name {save_path}")

#this function are convert video to frame 
def save_frame(video_path,save_dir):
    video_paths=glob(video_path+"/*")

    for path in video_paths:
        video_path="".join(path)
        print(video_path)
        name=path.split("/")[-1].split(".mp4")[0]
        #save_path=os.path.join(save_dir,name)
        create_dir(save_dir)
        fp="fps=1,scale=1280:720"
        os.system(f"ffmpeg -i {video_path} -vf fps={fp} {save_dir}/img-%03d.jpg -loglevel quiet")
    return "done"

if __name__=="__main__":
    video_paths="/home/diycam/Desktop/video/4video"
    save_dir="save/4_video"
    save_frame(video_paths,save_dir)

        
    
