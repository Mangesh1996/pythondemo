


from video_imge import save_frame
from tqdm import tqdm
from ffmpeg_progress_yield import FfmpegProgress
import tkinter as tk
from tkinter import filedialog
import os


if __name__=="__main__":
    root = tk.Tk()
    root.withdraw()
    # specifice the file type when user chose the file
    filetype = (("Mp4 files", "*.mp4"), ("Window Media Viewer", "*.wvm"),
                ("Audio Video Interleave", "*.avi"), ("Matroska Multimedia Container", "*.mkv"),)
    defalut_path = os.path.join(os.getcwd())
    file_path = filedialog.askdirectory(title="Select Folder ")
    
    print(file_path)
    # save path in save_path
    save_path = filedialog.askdirectory(title="Select Folder to save frames")
    print(save_path)
    save_frame(file_path,save_path)
    print("\n")
    print("Video to frame converting done ")


