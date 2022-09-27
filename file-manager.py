# file manager automation script

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import fnmatch
import re


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):

        # if new file is created, move to destination folder
        for filename in os.listdir(watch_folder):
            i = 1
                # we match file type to a pattern.
            newname = filename

            for k,v in extension_dest.items():
                if fnmatch.fnmatch(filename, k):
                    newDir = v
                if not os.path.exists(newDir):
                    os.mkdir(newDir)
                    shutil.move(watch_folder+'\\'+newname, newDir)


#build a dictionary for every extention and its respective 
extension_dest ={
    '*.txt' : 'C:\\Users\\Raymond\\Desktop\\test\\text',
    '*.pdf': 'C:\\Users\\Raymond\\Desktop\\test\\pdfs',
    '*.png': 'C:\\Users\\Raymond\\Desktop\\test\\pictures',
    '*.mp3': 'C:\\Users\\Raymond\\Desktop\\test\\Media'
    }


watch_folder = 'C:\\Users\\Raymond\\Desktop\\here'
destination_folder = 'C:\\Users\\Raymond\\Desktop\\test'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, watch_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
