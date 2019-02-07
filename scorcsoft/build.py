import os
import json
import importlib
import scorcsoft.globalAssets as sga

def main():
    if os.path.isfile(".com/cacheDB"):
        os.remove(".com/cacheDB")

    filePointer = open(".com/cacheDB","a+")

    for dir in os.walk("scorcsoftPOC"):
        d = dir[0]
        if d[-11:] == "__pycache__":
            continue
        for file in dir[2]:
            if file == "__init__.py":
                continue
            if file[-3:] == "pyc":
                continue
            if file[0:1] == ".":
                continue
            string = "%s/%s"%(d,file[:-3])
            pathString = string.replace("/",".")

            #print(string,pathString)
            module = importlib.import_module(pathString)

            subTmp = {"author": module.author,"date": module.date,"info": module.info}

            tmp = {string: subTmp}

            string = json.dumps(tmp)
            filePointer.write("%s\n"%(string))

    filePointer.close()
    sga.infoPrint("build the local cache database")
