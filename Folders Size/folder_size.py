
import os

f_path = ""  # File path
os.chdir(f_path)
li = []


def get_size(start_path="."):
    total_size = 0
    for dirpath, dirname, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size/1024**2


for course in os.listdir(os.getcwd()):
    li.append([course, get_size(os.path.join(os.getcwd(), course))])

li.sort(key=lambda k: k[1], reverse=True)
for l in li:
    print(l)
