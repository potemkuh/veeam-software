import os
from dir_sync.scan import scan
import random
import shutil


create_dir1 = ['test1', 'dir1', 'dir3']
create_dir2 = ['test2', 'dir2', 'dir3']
path = '/home/grins/veeam-software/tests/fixture/test_directory'


def create_tree(data, list_dir):
    for root in list_dir:
        path = data
        os.mkdir(os.path.join(data, root))
        data = os.path.join(data, root)
        os.chdir(data)
        for file in range(3):
            file = f'{file}{random.randint(1,5)}.txt'
            my_file = open(file, 'w')
            my_file.close()
    os.chdir(path)


def delete_dir(data1, data2):
    shutil.rmtree(data1)
    shutil.rmtree(data2)


def test_scan():
    create_tree(path, create_dir1)
    create_tree(path, create_dir2)
    path1 = '/home/grins/veeam-software/tests/fixture/test_directory/test1'
    path2 = '/home/grins/veeam-software/tests/fixture/test_directory/test2'
    assert scan(path1, path2) == os.listdir(path1)
    delete_dir(path1, path2)
