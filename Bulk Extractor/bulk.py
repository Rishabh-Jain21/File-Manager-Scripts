
import os
import shutil
import argparse


def bulk_extractor(folder_path, f_name):
    """
    Move all files in all subfolders to a single folder
    """
    if os.getcwd() == folder_path:
        print("folder path invalid")
    else:
        os.chdir(folder_path)
        f_path = os.path.join(folder_path, f_name)
        if not os.path.exists(f_path):
            os.makedirs(f_path)

        for dirpath, dirname, filenames in os.walk(folder_path):
            if dirname != 'Extracted':
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if os.path.isfile(fp):
                        try:
                            source = os.path.join(folder_path, fp)
                            destination = f_path
                            test = shutil.move(source, destination)
                        except:
                            pass


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, metavar='',
                    required=True, help="Folder Path")
parser.add_argument('-n', '--name', type=str, metavar='',
                    required=True, help="Folder Name for extracted files")
args = parser.parse_args()
bulk_extractor(args.file, args.name)
