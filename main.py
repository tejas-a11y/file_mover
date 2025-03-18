from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os

pictures = ['.png','.jpg','.jpeg','.gif','.svg']
videos = ['.mp4','.mov','.avi','.wmv','.flv']

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