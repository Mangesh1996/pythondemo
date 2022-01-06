
from ffmpeg_progress_yield import FfmpegProgress
import os
from glob import glob
from tqdm import tqdm
import shutil
from images_shape import resize
from bs4 import BeautifulSoup

def copy_xml(path,save):
    xmls=sorted(glob(path+"/*.xml"),key=os.path.basename)
    for xml in xmls:
        shutil.copy(xml,save)
def image_convertion(path,res,save):
    images=sorted(glob(path+"/*.png"),key=os.path.basename)
    copy_xml(path,save)
    for path in images:
        name=path.split("/")[-1]
        cmd=[
            "ffmpeg","-i",f"{path}","-vf",f"scale={res[0]}:{res[1]}",f"{save}/{name}"
        ]
        ff=FfmpegProgress(cmd)
        
        with tqdm(total=100,position=0,desc="Converting.....")as pbar:
                for progress in ff.run_command_with_progress():
                    pbar.update(progress-pbar.n)

def modify_xml(save,path,res):
    paths=sorted(glob(save+"/*.xml"),key=os.path.basename)
    ls=resize("images",resolution)
    for i in range(len(ls)):
        for path in paths:
            with open(path,"r")as re:
                data=re.read()
                xml=BeautifulSoup(data,"xml")
            print(ls[i])

        

        
if __name__=="__main__":
    path="images"
    save="save"
    resolution=[1280,720]
    #image_convertion(path,resolution,save)
    modify_xml(save,path,resolution)
    
    