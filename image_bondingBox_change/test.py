import ffmpeg


process=(
    ffmpeg
    .input("images/hard_hat_workers0.png")
    .filter("scale",width=1280,height=720)
    .output("save/imge.jpg",)
    .overwrite_output()
    .run()
)
