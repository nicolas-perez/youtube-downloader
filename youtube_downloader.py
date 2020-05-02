import os
import youtube_dl

DESTINATION_FOLDER_ABSOLUTE_PATH = "C:\\Users\\nperez\\Desktop\\videos"

os.makedirs(DESTINATION_FOLDER_ABSOLUTE_PATH, exist_ok=True)
os.chdir(DESTINATION_FOLDER_ABSOLUTE_PATH)
print("Destination Folder: ", DESTINATION_FOLDER_ABSOLUTE_PATH)

links = []

input_text = input("Copy-Paste the links below (1 per line), then enter 'd' to start downloading all videos:\n")
while input_text != "d":
    links.append(input_text)
    input_text = input("")


ydl_opts = {"ignoreerrors": True}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)
