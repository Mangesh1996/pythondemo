from pytube import YouTube



def resoulation_find(url):
    yt=YouTube(url)
    filters=yt.streams.filter(only_video=True,file_extension="mp4",adaptive=True).order_by("resolution")
    st=set()
    for i in filters:
        st.add(i.resolution)
    lst=list(st)
    st=" ".join(lst).split("p")[:-1]
    lsts=[int(i) for i in st ]
    lsts.sort()
    resoul=[ f"{i}p" for i in lsts]
    return resoul
        
    
    

    
if __name__=="__main__":
    url="https://www.youtube.com/watch?v=1GIx-JYdLZs"
    resoulation_find(url)
