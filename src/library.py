import os
import shutil


def cleanpath(dirpath):
        if os.path.isdir(dirpath):
            shutil.rmtree(dirpath)
        os.mkdir(dirpath)


def filepath(path, dirpath):
    if os.path.isfile(path):
        shutil.copy(path, dirpath)
    if os.path.isdir(path):
        for file in os.listdir(path):
            joined = os.path.join(path, file)
            dest = os.path.join(dirpath, file)
            if os.path.isfile(joined):
                shutil.copy(joined, dest)
            if os.path.isdir(joined):
                os.mkdir(dest)
                filepath(joined, dest)
                    
        