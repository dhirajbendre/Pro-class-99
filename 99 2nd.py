import os
import shutil
path = 'c:/Users/User/'
print("before copying files:")
print(os.listdir(path))
source = "c:/Users/User/file1.txt"
destination = "c:/Users/User/file1(copy).txt"
dest = shutil.copy(source, destination)
print("after copying files:")
print(os.listdir(path))
