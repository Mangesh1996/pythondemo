import numpy as np
import glob
import cv2


img_array=[]

for filename in glob.glob("/home/diycam/Desktop/dump/frames_work/save_frame/ironman/*.jpg"):
    img=cv2.imread(filename)
    height,width,layer=img.shape
    size=(width,height)
    img_array.append(img)
    
out=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'),25.0,size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()