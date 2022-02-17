"""
This python program just convert image resoulation give by user 
using ffmpeg libarry

usage : image.py  

"""
#import the libary
import ffmpeg
import os
import cv2
from glob import glob
#making the method to convert image resoulation using ffmpeg
def image_convertion(paths,save,width,height):
    images=sorted(glob(paths+"/*"),key=os.path.basename)
    exts=('.jpeg', '.JPEG', '.png', '.PNG', '.jpg', '.JPG')
    for path in images:
        if path.endswith(exts):
            
            name=path.split("/")[-1]
            try:
                process=(
                    ffmpeg
                    .input(path)
                    .filter("scale",width=width,height=height)
                    .output(f"{save}/{name}")
                    .overwrite_output()
                    .run(quiet=True)
                    )
            except Exception as e:
                print(e,path)
                image=cv2.imread(path)
                size=(1280,720)
                resize=cv2.resize(image,size)
                cv2.imwrite(f"{save}/cv_{name}",resize)  
           
if __name__=="__main__":
    path="/home/diycam/Downloads/fire_template/dataset/annotation_images"
    save="save1"
    resolution=[2020,920]
    image_convertion(path,save,resolution[0],resolution[1])
    
    
    