#!pip install douyin

import douyin

# HotVideo
search_video = douyin.hot.video()
# video objects
videos = search_video.data
# print every video
for video in videos:
    print(video)
    print(video.author)
    print(video.music)
    print(video.address)

# define handler and specify folder
handler = douyin.handlers.FileHandler(folder='./downloads')
# define downloader
downloader = douyin.downloaders.VideoDownloader([handler])
# download videos
downloader.download(videos)
