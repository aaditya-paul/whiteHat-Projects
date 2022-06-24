import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import cv2
from win10toast import ToastNotifier

frm_dir = "C:/Users/Aaditya Paul/Downloads"

toast = ToastNotifier()
observer = Observer()


class Notify( FileSystemEventHandler ):

    def on_created(self, event):
        print(f"Yoo !!, {event.src_path} has been created ")
        toast.show_toast("Created",f"File created at {event.src_path} ",duration=5,threaded=True)
        # read = cv2.imread(event.src_path)
        # cv2.imshow("Neew",read)
        # cv2.waitKey(0)

    def on_deleted(self, event):
        print(f"Yoo !!, {event.src_path} has been deleted ")
        toast.show_toast("Deleted",f"File deleted at {event.src_path} ",duration=5,threaded=True)


    def on_modified(self, event):
        print(f"Yoo !!, {event.src_path} has been modified ")
        toast.show_toast("Modified",f"File modified at {event.src_path} ",duration=5,threaded=True)


    def on_moved(self, event):
        print(f"Yoo !!, {event.src_path} has been moved ")
        toast.show_toast("Moved",f"File moved at {event.src_path} ",duration=5,threaded=True)


notify = Notify()

observer.schedule(notify,frm_dir,recursive=True)

observer.start()

try:

    while True:
        print("running...",end=" \r ")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping...X")
    observer.stop()
