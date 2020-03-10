import os
import time

def convert_to_megabytes(value):
    """to convert to megabytes"""
    mb = 1048576
    return round(value/mb, 2)

def get_size(dir):
    size = 0
    for path, sub_dirs, files in os.walk(dir):
        for f in files:
            file_path = os.path.join(path, f)
            size += os.path.getsize(file_path)
            converted = convert_to_megabytes(size)
    return converted

dir_size = get_size('../../')



print("Total Dir size MB: ", dir_size )