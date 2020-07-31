import os
from hashlib import md5
start_path = r"#Enter the starting directory"
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
stats = False
for value in duplicates.values():
    if len(value) > 1:
        stats = True
        print(value)
if not stats:
    print("No duplicates found")
