
import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

frm_dir = "C:/Users/Aaditya Paul/Downloads"
to_dir = "C:/Users/Aaditya Paul/Documents/WhiteHat/Classes/c103/images"

class FileMovementHandler(FileSystemEventHandler):
    
    def on_created(self,event):
        name,ext = os.path.splitext(event.src_path)
        print(event.src_path)

        for key,value in dir_tree.items():
            if ext in value:
                fileName = os.path.basename(event.src_path)
                print("downloaded and moving" + fileName)

                path1 = frm_dir + "/" + fileName
                path2 = to_dir + "/" + key
                path3 = to_dir + "/" + key + "/" + fileName

                if os.path.exists(frm_dir + "/" + key):

                    if os.path.exists(path2):
                        print("copying")
                        shutil.move(path1,path3)
                    else:
                        os.mkdir(path2)
                        shutil.move(path1,path3)

        print(event)

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,frm_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running ...",end="\r")
except KeyboardInterrupt:
    print("error")
    observer.stop()



    

    
