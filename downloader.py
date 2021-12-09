from abc import *

class Downloader(metaclass=ABCMeta):
    def __init__(self, url, save_dir="./"):
        import os
        self.url = url
        self.save_dir = save_dir
        os.makedirs(self.save_dir, exist_ok=True)
    
    def download(self):
        pass
    
class Youtube(Downloader):
    def __init__(self, url, save_dir="./"):
        import pytube
        super().__init__(url, save_dir)
        self.youtuber = pytube.YouTube(self.url)
        print(f"title : {self.youtuber.title}")
    
    def download(self, resolution="1440p"):
        if self.youtuber.streams.filter(res=resolution) == []:
            print(f"Not Found {self.youtuber.title}, res : {resolution}")
        self.youtuber.streams.filter(res=resolution, only_video=True).first().download(self.save_dir)

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=zsY5tDA7zE0&t=80s"
    yt = Youtube(url)
    yt.download()