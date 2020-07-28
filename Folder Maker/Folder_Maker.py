import os
import shutil
import time
from datetime import datetime


'''
Put this python file in another directorty or result may cause problem
'''


def folder_maker(folder_path):
    """
    Moves the files in the directory of the modified time
    """
    if os.getcwd() == folder_path:
        print("folder path invalid")
    else:
        os.chdir(folder_path)
        for i in os.listdir():
            path = os.path.join(folder_path, i)
            ti = (datetime.fromtimestamp(os.path.getmtime(path)))
            c_ti = str(ti.strftime('%Y-%m-%d'))
            f_path = os.path.join(folder_path, c_ti)
            if not os.path.exists(f_path):
                os.makedirs(f_path)
            source = os.path.join(folder_path, i)
            destination = os.path.join(folder_path, f_path)
            test = shutil.move(source, destination)


folder_maker()
