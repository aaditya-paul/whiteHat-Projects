import os
import shutil

frm = "C:/Users/Aaditya Paul/Downloads"
to = "C:/Users/Aaditya Paul/Documents/WhiteHat/Projects/c102/"

li = os.listdir(frm)



for files in li:
    name,ext = os.path.splitext(files)
    print(name + ext)

    if ext == "":
        continue
    if ext in [".pdf","docx"]:
        path1 = frm + "/" + files
        path2 = to + "/" + "docs"

        if os.path.exists(path2):
            shutil.copy(path1,path2)
        else:
            os.mkdir(path2)
            shutil.copy(path1,path2)
