from subprocess import run
from subprocess import PIPE
from sys import argv
from os import path
from os import makedirs
from os import remove
from os import listdir
from random import getrandbits
from shutil import copyfile
from shutil import rmtree

try:
    target = argv[1]
except:
    target = r".\zips\matryoshka_166.zip"

if not path.exists(target):
    print(f"Could not find target {target}")
    sys.exit(1)

basename, ext = path.splitext(target)
dirname = path.dirname(target)

new_target = path.join(dirname, str(getrandbits(64)) + ext)
copyfile(target, new_target)
target = new_target

while True:
    if not path.exists(target):
        print("Done!")
        break

    tmpdir = path.join(dirname, str(getrandbits(64)))
    makedirs(tmpdir)

    sevzip = run(
            ['7z.exe', 'e', f'-o{tmpdir}', target],
            encoding='ascii',
            stdout=PIPE, stderr=PIPE)

    remove(target)

    for file in listdir(tmpdir):
        unzipped_full = path.join(tmpdir, file)
        #print(file)
        if (path.isfile(unzipped_full)):
            with open(unzipped_full, "r") as f:
                try:
                    first_line = f.readline()
                    if first_line.startswith("Esse"):
                        print(f"Flag is {first_line}")
                        break
                except:
                    pass
            copyfile(unzipped_full, path.join(dirname,file))
            target = path.join(dirname, file)
    rmtree(tmpdir)
