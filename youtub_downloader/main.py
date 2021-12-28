from pytube import YouTube
from time import sleep
from random import randint
from find_resoluation import resoulation_find
import os

save_path=os.path.join(os.getcwd(),"save_path")

link=input("Paster the Youtube link:-  ")

try:
    yt=YouTube(link)
    print(yt.title)

except:
    print("connection error")
pixl=resoulation_find(link)
for j in range(len(pixl)):
    mp4files=yt.streams.filter(res=pixl[j]).first()
    try:
        mp4files.download(save_path,filename=f"{yt.title}_{pixl[j]}.mp4")
    except:
        print("some error")
    print(f"downloading complete {yt.title}.mp4")
sleep(randint(7,20))