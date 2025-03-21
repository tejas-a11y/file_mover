#Importing watchdog and os module for handling file system events and accessing list of folder directory.

from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os

#Specifying file extentions under each category of files.
pictures = ['.png','.jpg','.jpeg','.gif','.svg']
videos = ['.mp4','.mov','.avi','.wmv','.flv']

'''Creating a MyHandler class as per watchdog docs page and under on_modified method (as to be written under docs to be used), specifying a for loop for each event to get 
extention on file by os.path.splitext() method and then adding conditional logic changing the destination as per file extention'''

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            ext = os.path.splitext(filename)[1]
            if ext in pictures:
                new_destination = folder_destination + '/photos/' + filename
            elif ext in videos:
                new_destination = folder_destination + '/videos/' + filename
            else:
                new_destination = folder_destination + '/documents/' + filename
            os.rename(src, new_destination)

#Specifying folder to track and destination in which subfolders are there for file types.

folder_to_track = "C:/Users/Tejas/Desktop/myFolder"
folder_destination = "C:/Users/Tejas/Desktop/newFolder"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
