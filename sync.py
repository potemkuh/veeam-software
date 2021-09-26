import os
from dirsync import sync

path = 'dir_test1'
path2 = 'dir_test2'


def sync(p1, p2): 
    for i in os.listdir(p1):
        full_path = os.path.join(os.path.join(p1, i))
        if os.path.isdir(full_path):
            if os.path.exists(os.path.join(path2+i)):
                os.mkdir(os.path.join(path2+i))
            




sync(path, path2)
