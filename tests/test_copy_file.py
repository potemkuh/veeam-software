import os
from dir_sync.scan import copy_file


def test_copy():
    path1 = 'tests/fixture/test_file_copy/dir_file1'
    path2 = 'tests/fixture/test_file_copy/dir_file_copy'
    file_name = 'file.txt'
    copy_file(path1, path2, file_name)
    with open(os.path.join(path1, file_name), 'r') as f1:
        file1 = f1.read()
        with open(os.path.join(path1, file_name), 'r') as f2:
            file2 = f2.read()
            assert file1 == file2
            os.remove(os.path.join(path2, file_name))
