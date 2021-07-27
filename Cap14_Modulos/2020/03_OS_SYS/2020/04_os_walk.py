import os
import time

for path, sub_dirs, files in os.walk('../..'):
    for file in files:
        if not file.endswith(".py") and not file.startswith('.') and not file.endswith('.pyc'):
            file_path = os.path.join(path, file)
            file_size = os.path.getsize(file_path)
            info = os.stat(file_path)
            print("File Path: {0:<65} FIle size:{1:<10} Last Modified:{2}".format(file_path,file_size,time.ctime(info.st_mtime)))