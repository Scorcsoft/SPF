import os
import importlib
import scorcsoft.globalAssets as sga

def main(cmd):
    cmdList = cmd.split(" ")
    if len(cmdList) < 2:
        sga.errorPrint("load command: load scorcsoftPOC/other/test")
        return

    modulePath = cmdList[1]
    badModule = False
    sga.moduleOptions = None
    if not os.path.isfile("%s.py"%(modulePath)):
        sga.errorPrint("failed: %s is not exist"%(modulePath))
        return

    try:
        importString = modulePath.replace("/",".")
        sga.module = importlib.import_module(importString)
    except Exception as e:
        sga.errorPrint("failed: %s has an error: %s"%(modulePath,e))
        sga.module = None
        return

    try:
        sga.moduleType = sga.moduleTypeList[sga.module.type]
        sga.moduleOptions = sga.module.options # copy the module options to global module
    except:
        sga.errorPrint("failed: %s is not a SPF module" % (modulePath))
        sga.module = None
        return

    for k in sga.module.options: # check the options
        sga.moduleOptionsWord.append("%s " % (k)) # add current module option name auto complete
        tmp = list(sga.module.options[k])
        if "value" not in tmp or "info" not in tmp:
            badModule = True
            break

    if "exploit" not in dir(sga.module): # check the main function
        badModule = True

    if badModule:
        sga.errorPrint("failed: %s is not a SPF module" % (modulePath))
        sga.module = None
        return




    sga.modulePath = modulePath
    sga.commandWord.append("exploit") # add the exploit command auto complete
    sga.commandPrompt = '\033[4;30mspf\033[0m \033[1;31m%s\033[0m(%s) > ' % (sga.moduleType, sga.modulePath)
    sga.successPrint("load: %s"%(modulePath))


