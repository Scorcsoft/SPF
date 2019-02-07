import scorcsoft.globalAssets as sga

def main():

    if sga.module == None:
        sga.infoPrint("unload: no module has been loaded")
        return

    string = sga.modulePath
    sga.module = None
    sga.modulePath = None
    sga.moduleType = None
    sga.commandWord.remove("exploit") # remove the exploit command auto complete
    sga.moduleOptionsWord = [] # remove the module option name auto complete
    sga.commandPrompt = '\033[4;30mspf\033[0m > '
    sga.infoPrint("unload: %s"%(string))