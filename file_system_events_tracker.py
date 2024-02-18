import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/malli/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    def  on_created(self, event):
        print(f"Hey,{event.src.path}has been created!")
    def  on_created(self, event):
        print(f"oops! someone deleted,{event.src.path}")
    def  on_created(self, event):
        print(f"Hey there!,{event.src.path}has been modified")
    def  on_created(self, event):
        print(f"someone moved,{event.src.path} to {event.dest.path} ")
    

    #2_on_deleted

    #3_on_modified

    #4_on_moved

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
     print("stopped...")
     observer.stop()






