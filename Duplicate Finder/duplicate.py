import os
from hashlib import md5
from threading import Thread
import threading
import time
c1 = time.time()
in_t = threading.active_count()
def checker(duplicates, file_name):
    if os.path.isfile(file_name):
        try:
            fi = open(fp, 'rb')
            hexa_code = md5(fi.read()).hexdigest()
            duplicates[hexa_code] = duplicates.get(
                hexa_code, [])+[os.path.abspath(fp)]
        except:
            pass


start_path = r"E:\VIT"
duplicates = dict()

for dirpath, dirname, filenames in os.walk(start_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        t = Thread(target=checker, args=(duplicates, fp))
        t.start()
        time.sleep(.01)

while(True):
    if threading.active_count() <= in_t:
        stats = False
        for value in list(duplicates):
            if len(duplicates[value]) > 1:
                stats = True
                print(duplicates[value])
        if not stats:
            print("No duplicates found")
        print(time.time()-c1)
        break
