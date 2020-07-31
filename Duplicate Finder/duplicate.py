import os
from hashlib import md5
start_path = r"E:\VIT\Virtual Semester"
duplicates = dict()
for dirpath, dirname, filenames in os.walk(start_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if os.path.isfile(fp):
            try:
                fi = open(fp, 'rb')
                hexa_code = md5(fi.read()).hexdigest()
                duplicates[hexa_code] = duplicates.get(
                    hexa_code, [])+[os.path.abspath(fp)]
            except:
                pass
for value in duplicates.values():
    if len(value) > 1:
        print(value)
