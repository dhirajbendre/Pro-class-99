import os 
path = "C:/Users/User/file.txt"
root_ext = os.path.splitext(path)
print("root part ", root_ext[0])
print(os.listdir(path))