import os

for root, dirs, files in os.walk('../../2020'):
    print(root)
    print(dirs)
    print(files)