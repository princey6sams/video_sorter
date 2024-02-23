import os

sorted_files=[]
files = os.listdir()
for i in files:
    if i.endswith('.mp4'):
        sorted_files.append(i)
print(sorted_files) 
for i in sorted_files:
    new_name = i[4:]
    os.rename(i, new_name)
