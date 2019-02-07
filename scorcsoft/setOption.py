import scorcsoft.globalAssets as sga

def main(cmd):
    cmdList = cmd.split(" ")
    if len(cmdList) < 3:
        sga.errorPrint("set command: set [option name] [option value]")
        return

    if not sga.module:
        sga.errorPrint("no module has been load")
        return

    name = str(cmdList[1])
    value = str(cmdList[2])
    try:
        sga.moduleOptions[name]['value'] = value
    except:
        pass

    sga.infoPrint("set %s => %s"%(name,value))
