import os
# from pathlib import Path
import subprocess
import random

# repoPath = "C:\\Users\\Matta\\Repos\\random_1.py"
myFolder = "C:\\Users\\Matta\\Desktop\\NewFolder"
vlcPlayer = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
fileList = os.listdir(myFolder)
theLength = fileList.__len__()
rando = random.randint(0, theLength-1)
for file in fileList:
    if fileList.index(file) == rando:
        playFile = os.path.join(myFolder, file)
        p = subprocess.Popen([vlcPlayer, playFile])