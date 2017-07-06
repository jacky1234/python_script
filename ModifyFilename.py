import os
dir = os.getcwd()
subdir = os.listdir(dir)
for i in subdir:
    path = os.path.join(dir, i)
    if os.path.isdir(path):
        end_dir = os.listdir(path)
        for j in range(len(end_dir)):
            newname = end_dir[j][0:50]
            os.rename(os.path.join(path, end_dir[
                      j]), os.path.join(path, newname))
