"""
Download the youtube video multiple resoluation 

usage :- find_resoluation.py and main.py

"""
#import the libaray
from pytube import YouTube
from time import sleep
from random import randint
from find_resoluation import resoulation_find
import os
#derivate the save path
save_path=os.path.join(os.getcwd(),"save_path")
# get the input link
link=input("Paster the Youtube link:-  ")
#make the try to handle error
try:
    yt=YouTube(link)
    print(yt.title)
#make the excepthe when the connection issue
except:
    print("connection error")
# call the function for check resoluation
pixl=resoulation_find(link)
for j in range(len(pixl)):
    # filter the resolution 
    mp4files=yt.streams.filter(res=pixl[j]).first()
    try:
        # download the video to save path with vide title name
        mp4files.download(save_path,filename=f"{yt.title}_{pixl[j]}.mp4")
    except:
        print("some error")

    print(f"downloading complete {yt.title}.mp4")

sleep(randint(7,20))