from glob import glob
import os
import shutil
from time import sleep
from tqdm import tqdm




def copy_method(source_path,save_path):
    sourcepath_ls=os.listdir(source_path)
    for i in tqdm(range(len(sourcepath_ls))):
        
        for filename in glob(os.path.join(source_path,"*.*")):
            shutil.copy(filename,save_path)
            sleep(0.2)
        print(round(i/len(sourcepath_ls)*100))


if __name__ == '__main__':
    source_path=os.path.join(os.getcwd(),"source_file/4k")
    print(source_path)
    save_path=os.path.join(os.getcwd(),"save_files")
    print(save_path)  
    copy_method(source_path,save_path)