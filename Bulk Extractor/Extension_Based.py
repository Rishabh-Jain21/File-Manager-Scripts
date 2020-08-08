import os
import shutil
import time
from datetime import datetime


'''
Put this python file in another directorty or result may cause problem
'''
extensions = {
    'Document': ['.doc', '.dot', '.odt', '.sxw', '.rtf', '.pdf', '.txt'],
    'Images': ['.jpg', '.jpeg', '.jpe', '.gif', '.bmp', '.tif', '.tiff', '.png'],
    'Audio': ['.mp3', '.wma', '.ogg', '.au', '.aif', '.aiff', '.wav'],
    'Video': ['.avi', '.mpg', '.mpeg', '.wmv', '.mov', '.divx', '.mp4', '.m4v', '.asf']
}


def bulk_extractor(folder_path):
    """
    Move all files in all subfolders to a single folder
    """
    if os.getcwd() == folder_path:
        print("folder path invalid")
    else:
        os.chdir(folder_path)
        f_path = os.path.join(folder_path, "Extracted")
        if not os.path.exists(f_path):
            os.makedirs(f_path)

        for dirpath, dirname, filenames in os.walk(folder_path):
            if dirname != 'Extracted':
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if os.path.isfile(fp) and (os.path.splitext(fp)[1] in extensions['Document']):
                        try:
                            source = os.path.join(folder_path, fp)
                            destination = f_path
                            test = shutil.move(source, destination)
                        except:
                            pass


bulk_extractor(r"#Enter Path")
