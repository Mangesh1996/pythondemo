import os
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
        make_dri(save)
        
        # # os.system(f"ffmpeg -i {path} -vf fps=1 {save}/img-%03d.jpg")
        os.system(f"ffmpeg -i {path} -vf fps=1 {save_path}/img{i}-%05d.jpg")


if __name__=="__main__":
    source_path="source_path/4video"
    save="save"
    convert_img(source_path,save)