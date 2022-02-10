from glob import glob
import os
import shutil

files="source"

ls=os.listdir("source")
xml=[i.replace(".xml","") for i in ls if i.endswith(".xml")]
png=[i.replace(".png","") for i in ls if i.endswith(".png")]
jpgs=[i.replace(".jpg","") for i in ls if i.endswith(".jpg")]
pairs="pairs"
odd="odd"

for i in jpgs:
    if i in xml:
        shutil.copy(os.path.join(files,f"{i}.jpg"),pairs)
    else:
        shutil.copy(os.path.join(files,f"{i}.jpg"),odd)

for i in png:
    if i in xml:
        shutil.copy(os.path.join(files,f"{i}.png"),pairs)
    else:
        shutil.copy(os.path.join(files,f"{i}.png"),odd)

# for i in xml:
#     if i in jpgs:
#         shutil.copy(os.path.join(files,f"{i}.xml"),pairs)
#     elif i in png:
#          shutil.copy(os.path.join(files,f"{i}.xml"),pairs)

#     else:
#         shutil.copy(os.path.join(files,f"{i}.xml"),odd)


