"""
    Generate the frame using open-cv libarary 
    and alse generate the specifier number of frame
    
"""

# Import to libarary
import cv2
import os
from glob import glob
from time import sleep
import sys
from frame_count import frame_count

#making the function for creating direactory
def createdire(path):
    try:# apply the try method for exception handling 
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"File already exist {path}")
        
#making a function for generate the frame through video
def genarate_frame(path,save_path,gap):
            name=path.split("/")[-1].split(".")[0] # extract the name of video for video
            save_path=os.path.join(save_path,name) # define the path of saving 
          
            createdire(save_path)# call the function for create the save direactory
            for z in range(21):
                  sleep(1.0)
                  sys.stdout.write("\r")
                  cap=cv2.VideoCapture(path)
                  idx=0
                  while True:
                        res,frame=cap.read()
                        if res == False:
                              cap.release()
                              break
                        if idx ==0:
                              cv2.imwrite(f"{save_path}/{idx}.jpg",frame)
                        else:
                              if idx % gap == 0:
                                    cv2.imwrite(f"{save_path}/{idx}.jpg",frame)
                        idx+=1
                  sys.stdout.write("[%-20s]%d%%" %( "="* z,5*z) )
            sys.stdout.flush()
            sleep(0.2)
            print("\n")
            print(f"Video to Frame converting done frame rate is {gap}")
            print("\n")


if __name__=="__main__":
    video_path=glob("source_video/*")#assing the video path
    save_dir="save_frame"# assing the save direactory 
    #gap=int(input("enter the video frame speed:- "))
    
    for path in video_path:
        gap=frame_count(path)
        genarate_frame(path,save_dir,gap)
        
        
    