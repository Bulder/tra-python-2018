import subprocess
import glob
import os
import sys
import time

files = sorted(glob.glob(sys.argv[1]))

loop = 0
if len(sys.argv) <= 2:
    loop = 1
else:
    loop = int(sys.argv[2])

number = {}
for file in files:
    key = file.split('_')[-1].split('.')[0]
    print("File", file)
    number[key] = []
    for i in range(loop):
        start = time.clock()
        result = subprocess.run(['python', 'main.py', file], stdout=subprocess.PIPE)
        stop = time.clock()
        number[key].append(stop - start)

string = ""
for key, value in number.items():
    string += key
    for item in value:
        string += ','
        string += str(item)
    string +='\n'
print(string)
