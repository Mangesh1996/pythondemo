
import glob
import cv2
from frame_counts import frame_count
img_array=[]

for filename in glob.glob("video_frame/ironmane_fly/*.jpg"):
    img=cv2.imread(filename)
    height,width,layer=img.shape
    size=(width,height)
    img_array.append(img)

gap=frame_count("/home/diycam/Desktop/dump/frame_video/video/ironmane_fly.mp4")
    
out=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'),gap,size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()