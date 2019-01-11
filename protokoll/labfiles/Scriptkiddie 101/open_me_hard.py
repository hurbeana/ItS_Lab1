from optparse import OptionParser
from os import path
from os import walk
from threading import Thread
from subprocess import run
from subprocess import PIPE

parser = OptionParser()
parser.add_option("-f", "--file", dest="f")
(options, args) = parser.parse_args()
file = args[0]
dicts = args[1:]

print(dicts)
found = False

def test_seven_zip(pwd):
    """ Run 7z.exe with given password on 7z file given in argument """
    global found
    global file
    if found:
            return
    sevzip = run(
            ['7z.exe', 'e', file],
            input=pwd,
            encoding='ascii',
            stdout=PIPE, stderr=PIPE)
    rc = sevzip.returncode
    if rc is 0:
        print(f"Password for 7z file is {pwd}")
        found = True

def run_dic(dictionary):
    global found
    if path.basename(dictionary).startswith("."):
        print(f"{dictionary} is hidden, skipping")
        return
    print(f"checking dictionary {dictionary}")
    f = open(dictionary, 'r')
    for line in f.readlines():
        if len(line) is not 8:
            continue
        if found:
            f.close()
            return
        else:
            test_seven_zip(line)
            th = Thread(target=test_seven_zip, args=(line,))
            th.start()
    f.close()
    print(f"done with dictionary {dictionary}")

def run_all_in_dir(dir):
    global found
    if path.basename(dir).startswith("."):
        print(f"{dir} is hidden, skipping")
        return
    print(f"running all in dir {dir}")
    for root, dirs, files in walk(dir):
        if found:
            return
        for dir in dirs:
            run_all_in_dir(path.join(root, dir))
        for file in files:
            th = Thread(target=run_dic, args=(path.join(root, file),))
            th.start()
    print(f"done with all in dir {dir}")

for f in dicts:
    for root, dirs, files in walk(f):
        for dir in dirs:
            run_all_in_dir(path.join(root, dir))
        for file in files:
            th = Thread(target=run_dic, args=(path.join(root, file),))
            th.start()