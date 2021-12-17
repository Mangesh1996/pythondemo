""" Play the video using Open Cv libaray
"""
    
# import cv2 libarary 
import cv2
import os
from glob import glob


#create function to play video
def play_video(path):
    # Create a VideoCapture object and read from input file
    cap=cv2.VideoCapture(path)
    # Check if camera opened successfully
    if cap.isOpened()==False:
        print("Error opeing video file")
    #Read untile video is completed 
    while cap.isOpened():
        #capture frame-by-frame 
        ret,frame=cap.read()
        if ret==True:
            #Display the resulting frame
            cv2.imshow("frame",frame)
            # press 'q' buttion to exit video 
            if cv2.waitKey(25)&0xFF == ord("q"):
                cap.release()
                break
        # Break the loop
        else:
            cap.release()
            break
# When everything done, release 
# the video capture object
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    # source_path=os.path.join(os.getcwd(),"source_video")
    # call the function 
    source_path=glob("source_video/*")
    for path in source_path:
        play_video(path)
