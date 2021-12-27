"""
Converting Video to image 

usage:- add souce file and define destation directory

"""


#making the function if save path not present 
import os
from tqdm import tqdm
import time
from frame_count import frame_count
import datetime
from tqdm import tqdm
from ffmpeg_progress_yield import FfmpegProgress
from glob import glob

def make_dri(path):
    try:
        if os.path.exists(path):
            print("path already present")
        else:
            os.makedirs(path)
    except OSError:
        print(f"directory not crater {path}")

def convert_img(source_path,save_path):
    source=glob(source_path+"/*")
    for i,path in enumerate(source):
        name=path.split("/")[-1].split(".mp4")[0]
        print(name)
        
        save=os.path.join(save_path,name)
        # make_dri(save)
        
        # # # os.system(f"ffmpeg -i {path} -vf fps=1 {save}/img-%03d.jpg")
        # os.system(f"ffmpeg -i {path} -vf fps=1 {save_path}/img{i}-%05d.jpg")
        start = time.time()
        cmd = [
        "ffmpeg", "-i", "source_video/ironmane_fly.mp4", "-vf", "fps=1", "frame_dire/img-%03d.jpg", ]
        
        cmd[2] = path
        cmd[5] = save_path+f"/img{i}-%03d.jpg"
        uni = [0,]
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


if __name__=="__main__":
    source_path="source_path/iron"
    save="save/"
    convert_img(source_path,save)
        
    
