
print("****** YOUTUBE AUDIO VIDEO DOWNLOADER ******")
from pytube import YouTube
import os

def ytvid():
  link = str(input("\nenter the youtube video link: \n>>"))
  yt = YouTube(link)
  print(yt.title)
  res = str(input("\n144p\t360p\t720p\t1080p : "))
  if res == '144p':
    yt.streams.filter(file_extension='mp4')
    video = yt.streams.get_by_itag(17)
    location = str(input("enter the destination where the files should be stored(eg:/Users/name/Downloads and leave it blank for current directory)>>"))
    video.download(output_path=location)
  if res == '360p':
    yt.streams.filter(file_extension='mp4')
    video = yt.streams.get_by_itag(18)
    location = str(input("enter the destination where the files should be stored(eg:/Users/name/Downloads and leave it blank for current directory)>>"))
    video.download(output_path=location)
  if res == '720p':
    yt.streams.filter(file_extension='mp4')
    video = yt.streams.get_by_itag(22)
    location = str(input("enter the destination where the files should be stored(eg:/Users/name/Downloads and leave it blank for current directory)>>"))
    video.download(output_path=location)
  if res == '1080p':
    yt.streams.filter(file_extension='mp4')
    video = yt.streams.get_highest_resolution()
    location = str(input("enter the destination where the files should be stored(eg:/Users/name/Downloads and leave it blank for current directory)>>"))
    video.download(output_path=location)
    print("Sucessfully downloaded")



def ytaud():
  link = str(input("\nenter the youtube video link: \n>>"))
  yt = YouTube(link)
  print(yt.title)
  location = str(input("enter the destination where the files should be stored(eg:/Users/name/Downloads and leave it blank for current directory)>>"))
  video = yt.streams.filter(only_audio=True, file_extension='mp4').first()
  vid_file = video.download(output_path=location)

  base, ext = os.path.splitext(vid_file)
  aud_file = base + '.mp3'
  os.rename(vid_file, aud_file)
  print("successfully downloaded")

  
print("\n***************************")
print("\n1.youtube video to video")
print("\n2.youtube video to audio")
print("\n***************************")
user_input = int(input("Enter your choice (1 or 2) : "))
if user_input == 1:
  ytvid()
else:
  ytaud()
