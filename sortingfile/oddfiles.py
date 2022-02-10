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


def sortfiles(source,pair,odd):


    print(os.getcwd())   # os.getcwd() to get current working directory

    # we are store the path of source file,missingfiles,jpg and xml
    src=os.path.join(os.getcwd(),source)
    mis=os.path.join(os.getcwd(),odd)
    pairs=os.path.join(os.getcwd(),pair)


    ls=os.listdir(src) # storing the file data name in list

    # we are sorting the jpg and xmls file name in store different list   
    img=[i.replace(".jpg","") for i in ls if i.endswith(".jpg")] 
    xml=[i.replace(".xml","") for i in ls if i.endswith(".xml")]
    png=[i.replace(".png","")for i in ls if i.endswith(".png")]
    odd=[] # create the empty list for stroe odd files

    for z in range(21):
        sleep(1.0)
        sys.stdout.write("\r")
        # we are move  the unpair file name and pair file name 
        for i in img:
            print(f"{i}.jpg")
            for j in png:
                print(f"{j}.png")
            # if i not in xml:
            #     odd.append(i+".jpg")
            # else:
            #     n=i+".xml"
            #     shutil.copy(os.path.join(src,n),pairs)
        # for k in png:
        #     if k not in xml:
        #         odd.append(k+".png")
        #     else:
        #         ns=k+".xml"
        #         shutil.copy(os.path.join(src,ns),pairs)
        # for j in xml:
        #     if j not in img: 
        #         odd.append(j+".xml")
        #     else:
        #         na=j+".jpg"
        #         shutil.copy(os.path.join(src,na),pairs)
        # for z in xml:
        #     if z not in png:
        #         odd.append(z+".png")
        #         print(z)
        #     else:
        #         nz=z+".png"
        #         shutil.copy(os.path.join(src,nz),pairs)
        # for f in odd:
        #     shutil.copy(os.path.join(src,f),mis) 
        # sys.stdout.write("[%-20s]%d%%" %( "="* z,5*z) )
    sys.stdout.flush()
    sleep(0.2)
    print("\n")
    print("All File copy to designation directory ")
    print("\n")

source="source"
pairs="pairs"
odd="odd"
sortfiles(source,pairs,odd)