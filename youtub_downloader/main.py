"""
Download the youtube video multiple resoluation 

usage :- find_resoluation.py and main.py

"""
#import the libaray
from genericpath import exists
from pytube import YouTube
from time import sleep
from random import randint
from find_resoluation import resoulation_find
import os

def save_path(download_path):
    try:
        if os.path.exists(download_path):
            print("download directory are present")
        else:
            os.mkdir(download_path)
    except OSError:
        print(f"File not created {download_path}")
#derivate the save path
save_path("save_path")
path=os.path.join(os.getcwd(),"save_path")
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
print("Select Video resoluation :- ")
for i in range(len(pixl)):
    print(f"{i+1}."+pixl[i])
choice=int(input("Choice the resoulation  :- "))

mp4files=yt.streams.filter(res=pixl[choice-1]).first()
try:
    # download the video to save path with vide title name
    mp4files.download(path,filename=f"{yt.title}_{pixl[choice-1]}.mp4")
except:
    print("some error")

print(f"downloading complete {yt.title}.mp4")

sleep(randint(7,20))