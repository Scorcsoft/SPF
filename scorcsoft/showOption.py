import scorcsoft.globalAssets as sga

def main(cmd):
    if sga.module == None:
        sga.infoPrint("unload: no module has been loaded")
        return


    maxLength1 = 0
    maxLength2 = 0

    for k in sga.moduleOptions:
        if maxLength1 < len(k):
            maxLength1 = len(k)
        if maxLength2 < len(sga.moduleOptions[k]['value']):
            maxLength2 = len(sga.moduleOptions[k]['value'])

    if maxLength2 < 5:
        maxLength2 = 5
    if maxLength1 < 4:
        maxLength1 = 4

    spaceString1 = "    " + " " * (maxLength1 - 4)
    spaceString2 = "    " + " " * (maxLength2 - 5)
    print("module options")
    print("--------------")
    print("    name%svalue%snote"%(spaceString1,spaceString2))
    print("    ----%s-----%s----"%(spaceString1,spaceString2))

    for k in sga.moduleOptions:
        tmp = sga.moduleOptions[k]
        spaceString1 = "    " + " " * (maxLength1 - len(k))
        spaceString2 = "    " + " " * (maxLength2 - len(tmp["value"]))
        print("    %s%s%s%s%s"%(k,spaceString1,tmp["value"],spaceString2,tmp["info"]))



