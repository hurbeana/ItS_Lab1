import subprocess as sp
from threading import Thread
import os
import sys

found = False
start = 0
end = 10000
file = sys.argv[1]

def run_sev_zip(pwd):
    global found
    if found is True:
            return
    to_send = pwd
    sevzip = sp.run(['7z.exe', 'e', file], input=to_send, encoding='ascii', stdout=sp.PIPE, stderr=sp.PIPE)
    rc = sevzip.returncode
    if rc is not 2:
        print(f"Password for 7z file is {pwd}")
        found = True

for i in range(start, end, 1):
    if found is True:
        break
    pwd = f'{i:04}'
    print(f"At trying {pwd}")
    th = Thread(target=run_sev_zip, args=(pwd,))
    th.start()
