import os
from glob import glob

def create_dir(save_path):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
    except OSError:
        print(f"Error : creating directory with name {save_path}")


def save_frame(video_path,save_dir):
    video_paths=glob(video_path+"/*")

    for path in video_paths:
        video_path="".join(path)
        print(video_path)
        name=path.split("/")[-1].split(".mp4")[0]
        save_path=os.path.join(save_dir,name)
        create_dir(save_path)
        fp="fps=1,scale=1280:720"
        os.system(f"ffmpeg -i {video_path} -vf fps={fp} {save_path}/img-%03d.jpg -loglevel quiet")

if __name__=="__main__":
    video_paths="source_path"
    save_dir="save"
    save_frame(video_paths,save_dir)

        
    
