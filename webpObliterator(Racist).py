# hi yes code made by Rinko__ and ChatGpt lol
# 1/31/24 - last updated
# its totally racist 

import os
import time 

import tkinter as tk
from tkinter import filedialog

# checking for watchdog
try: 
    import watchdog

except ImportError:
    print("watchdog not found. Installing watchdog lib")
    os.system("pip install watchdog")
    import watchdog

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    
except ImportError: 
    print("Watchdog aint here dawg, install it yourself.")
    exit()

# checking for Pillow
try:
    import PIL

except ImportError:
    print("wtf pillow not found? Installing PIL lib...")
    os.system("pip install Pillow")
    import PIL

try:
    from PIL import Image

except ImportError:
    print("Pillow aint here dawg, install it yourself")
    exit()

class imageHandlerThing(FileSystemEventHandler):

    def __init__ (self,targetDirectory):
        super().__init__()
        self.targetDirectory = targetDirectory

    def on_created(self, event):
        if event.is_directory:
            return

        # checks if the stupid file is a webp (its racist)
        if event.src_path.lower().endswith(".webp"):
            print(f"Detected new webp file: {event.src_path}")
            self.fuckWebp(event.src_path)

    def fuckWebp(self, webpToObliteratePath):

        # open the horrible image
        webpImg = Image.open(webpToObliteratePath)

        # make it cool
        pngFilePath = os.path.splitext(webpToObliteratePath)[0] + ".png"
        webpImg.save(pngFilePath, "PNG")


        webpImg.close()

        #obliterate the webp file lol
        
        os.remove(webpToObliteratePath)
        print(f"Reformatted file as a .png (obliterated the webp)")

def browseDirectory():
    # checks for target directory was previously saved
    if os.path.exists(targetDirectoryFile):
        with open(targetDirectoryFile, "r") as file:
                                    # wtf strip???
            targetDirectory = file.read().strip()
    else:
        targetDirectory = filedialog.askdirectory()
    
    if targetDirectory:
        print(f"Select target directory: {targetDirectory}")

        #save selected to a file
        with open(targetDirectoryFile, "w") as file:
            file.write(targetDirectory)
        
        startmonitoring(targetDirectory)

def startmonitoring(targetDirectory):

    obeserve = Observer()
    eventHandle = imageHandlerThing(targetDirectory)
    obeserve.schedule(eventHandle, path=targetDirectory, recursive= False)
    obeserve.start()

    try:
        print(f"Watching the directory {targetDirectory}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        obeserve.stop
    

    obeserve.join()

if __name__ == "__main__":

    targetDirectoryFile = "targetDirectory.txt"

    browseDirectory()