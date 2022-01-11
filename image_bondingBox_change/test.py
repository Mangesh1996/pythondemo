import os
from glob import glob


path=os.getcwd()
file="images"
filename=os.path.join(path,file)
name=glob(filename+"/*.xml")
print(name)