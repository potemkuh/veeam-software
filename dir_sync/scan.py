import shutil
import os


def copy_file(data1, data2, name_file):
    return shutil.copy2(
        os.path.join(data1, name_file),
        os.path.join(data2, name_file)
                        )


def scan(data1, data2):
    list_file = os.listdir(data1)
    list_file2 = os.listdir(data2)
    full_list = sorted(set(list_file + list_file2))
    for item in full_list:
        path1 = os.path.join(data1, item)
        path2 = os.path.join(data2, item)
        if os.path.isfile(path1):
            if item not in list_file2:
                copy_file(data1, data2, item)
            elif item in list_file2:
                time_1 = os.path.getmtime(path1)
                time_2 = os.path.getmtime(path2)
                if time_1 != time_2:
                    copy_file(data1, data2, item)
        elif os.path.isfile(path2):
            if item not in list_file:
                os.remove(path2)

        elif os.path.isdir(path1):
            if not os.path.exists(path2):
                os.mkdir(path2)
                scan(path1, path2)
            else:
                scan(os.path.join(data1, item), os.path.join(data2, item))
        elif os.path.isdir(path2):
            if item not in list_file:
                shutil.rmtree(path2)
    return os.listdir(data2)
