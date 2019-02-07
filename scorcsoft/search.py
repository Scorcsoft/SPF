import os
import json
import importlib
import scorcsoft.globalAssets as sga


def search(kw):
    try:
        for i in open(".com/cacheDB"):
            if kw in i:
                i = i.strip("\n")
                i = i.strip("\r\n")  # for stupit bugdows
                info = json.loads(i)
        return info

    except:
        sga.errorPrint("Can not use the local cache database, use \"build\" command to rebuild local cache database")
        sga.infoPrint("use slow search")
        slowSearch(kw)

def slowSearch(kw):
    info = {}
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
            string = "%s.%s" % (d, file[:-3])
            string = string.replace("/",".")
            #print(string,file[:-3])

            module = importlib.import_module(string)

            if kw in module.keyword:
                tmp = {"author": module.author,"date": module.date,"info": module.info}

                info["%s/%s"%(d,file[:-3])] = tmp
    return info


def main(cmd):
    cmdList = cmd.split(" ")
    if len(cmdList) < 2:
        sga.errorPrint("search command: search [cveID/keyword]")
        return

    if not os.path.isfile(".com/cacheDB"):
        sga.errorPrint("No local cache, use \"build\" command to build the local cache database file")
        sga.infoPrint("use slow search")
        result = slowSearch(cmdList[1])

    else:
        result = search(cmdList[1])


    if len(result) <= 0:
        return

    maxLengthPath = 0
    maxLengthAuthor = 0
    maxLengthDate = 0


    for k in result:
        if maxLengthPath < len(k):
            maxLengthPath = len(k)
        if maxLengthAuthor < len(result[k]['author']):
            maxLengthAuthor = len(result[k]['author'])
        if maxLengthDate < len(result[k]['date']):
            maxLengthDate = len(result[k]['date'])



    string = "search keyword: %s" % (cmdList[1])
    print(string)
    print("-" * len(string))

    spaceString1 = "    " + " " * (maxLengthPath - 4)
    spaceString2 = "    " + " " * (maxLengthAuthor - 6)
    spaceString3 = "    " + " " * (maxLengthDate - 4)

    print("    path%sauthor%sdate%sinfo" % (spaceString1, spaceString2,spaceString3))
    print("    ----%s------%s----%s----" % (spaceString1, spaceString2,spaceString3))

    for k in result:
        spaceString1 = "    " + " " * (maxLengthPath - len(k))
        spaceString2 = "    " + " " * (maxLengthAuthor - len(result[k]['author']))
        spaceString3 = "    " + " " * (maxLengthDate - len(result[k]['date']))

        print("    %s%s%s%s%s%s%s"%(k,spaceString1,result[k]['author'],spaceString2,result[k]['date'],spaceString3,result[k]['info']))






