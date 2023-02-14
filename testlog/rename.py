import os

now_dir = os.getcwd()
files = os.listdir(now_dir)
# print(files)
for i in files:
    if os.path.splitext(i)[-1] == '.log':
        os.rename(i, os.path.splitext(i)[0]+'.txt')

