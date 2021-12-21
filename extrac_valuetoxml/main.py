from bs4 import BeautifulSoup

with open("gun_01_163939819008.xml","r")as f:
    data=f.read()

bs_data=BeautifulSoup(data,'xml')

name=bs_data.find_all("name")
print(name[1])
pose=bs_data.find_all("pose")
difficult=bs_data.find_all("difficult")
xmin =bs_data.find_all("xmin")
ymin =bs_data.find_all("ymin")
xmax =bs_data.find_all("xmax")
ymax =bs_data.find_all("ymax")

for i in range(0,len(name)):
    print("name :- "+name[i].get_text(),end="\n")
    print("pose:- "+pose[i].get_text(),end="\n")
    print("difficult:- "+difficult[i].get_text(),end="\n")
    print("X-max:- "+xmin[i].get_text(),end="\n")
    print("Y-min:- "+ymin[i].get_text(),end="\n")
    print("X-max:- "+xmax[i].get_text(),end="\n")
    print("Y-max:- "+ymax[i].get_text(),end=" ")
    print("\n")
    print("---------------------------------")


