import os
import time;
import scorcsoft.globalAssets as sga

def main():
    for dir in os.walk("scorcsoftPOC"):
        d = dir[0]
        if d[-11:] == "__pycache__":
            continue
        for file in dir[2]:
            if file == "__init__.py":
                continue
            if file[-3:] == "pyc":
                continue
            string = "%s/%s"%(d,file[:-3])
            sga.allPocPath.append(string)

    #time.sleep(1)
    sga.initDone = True

