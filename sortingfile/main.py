
"""
To separate the .jpg and .xml pair and finding missing pairs

USAGE: python3 offfiles.py <numberof classes> <>
ex ython3 offfiles.py 5
"""
# Import library os and shutil use to file operation 
import os
import shutil
import sys
from time import sleep

print(os.getcwd())   # os.getcwd() to get current working directory

# we are store the path of source file,missingfiles,jpg and xml
src=os.path.join(os.getcwd(),"source")
mis=os.path.join(os.getcwd(),"missingfiles")
jpgs=os.path.join(os.getcwd(),"jpg")
xmls=os.path.join(os.getcwd(),"xml")

ls=os.listdir(src) # storing the file data name in list

# we are sorting the jpg and xmls file name in store different list   
img=[i.replace(".jpg","") for i in ls if i.endswith(".jpg")] 
xml=[i.replace(".xml","") for i in ls if i.endswith(".xml")]
odd=[] # create the empty list for stroe odd files

for z in range(21):
    sleep(1.0)
    sys.stdout.write("\r")
    # we are move  the unpair file name and pair file name 
    for i in img:
        if i not in xml:
            odd.append(i+".jpg")
        else:
            n=i+".xml"
            shutil.copy(os.path.join(src,n),xmls)
    for j in xml:
        if j not in img: 
            odd.append(j+".xml")
        else:
            na=j+".jpg"
            shutil.copy(os.path.join(src,na),jpgs)
    for f in odd:
        shutil.copy(os.path.join(src,f),mis) 
    sys.stdout.write("[%-20s]%d%%" %( "="* z,5*z) )
sys.stdout.flush()
sleep(0.2)
print("\n")
print("All File copy to designation directory ")
print("\n")


        
        
        
