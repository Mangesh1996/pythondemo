
import ffmpeg
import os
from glob import glob
from tqdm import tqdm



def image_convertion(path,res,save):
    images=sorted(glob(path+"/*.png"),key=os.path.basename)
    for path in images:
        name=path.split("/")[-1]
        process=(
                ffmpeg
                .input(path)
                .filter("scale",width=res[0],height=res[1])
                .output(f"{save}/{name}")
                .overwrite_output()
                .run(quiet=True)
                )


    return "done"       
if __name__=="__main__":
    path="images"
    save="save"
    resolution=[1280,720]
    image_convertion(path,resolution,save)
    
    
    