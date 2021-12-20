import cv2



cap=cv2.VideoCapture("video/ironmane_fly.mp4")
cap.set(cv2.CAP_PROP_FPS,10)
fps=int(cap.get(5))
print(fps)