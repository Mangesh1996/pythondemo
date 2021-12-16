

import cv2
import time
import os
from glob import glob

source=os.path.join(os.getcwd(),"source_video")
ls=os.listdir(source)
for i in ls:
    pass
if __name__=="__main__":
    video=cv2.VideoCapture(i)
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    
    if int(major_ver)<3:
        fps=video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps=video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
        
    num_frames=900
    print("Capturing {0} frames".format(num_frames))
    
    start=time.time()
    for i in range(0,num_frames):
        ret,frame=video.read()
        
    end=time.time()
    seconds=end - start
    print ("Time taken : {0} seconds".format(seconds))
    
    fps=num_frames/seconds
    print("Estimated frames per second : {0}".format(fps))
    
    video.release()
