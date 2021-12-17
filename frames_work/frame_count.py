
"""
Showing frame rate of video
making the funtion to show video frame rate
"""
# import cv and glob 
import cv2
from glob import glob

#making the funtion to count frames      
def frame_count(name):
    # capture the frame in the video file
    video=cv2.VideoCapture(name)
    #showing details of video frame
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
          
    if int(major_ver)<3:
        #store the frame rate the fps variable 
        fps=video.get(cv2.cv.CV_CAP_PROP_FPS)
        #print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(int(fps)))
        return int(fps)
    else:
        fps=video.get(cv2.CAP_PROP_FPS)
        #print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(int(fps))) 
        return int(fps) 
    #all condition true than close the video
       
    video.release()

if __name__=="__main__":
      source_path=glob("source_video/*")
      for path in source_path:
        frame_count(path)