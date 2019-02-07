import subprocess
import scorcsoft.globalAssets as sga


def main(cmd):
    badCommand = ["vi","vim","ex","python","python3","cd"]
    if cmd in badCommand:
        sga.infoPrint("command \"%s\" is not supported in SFW :)"%(cmd))
        return
    result = subprocess.getstatusoutput(cmd)
    if result[0] == 0:
        string = "execute system command: %s"%(cmd)
        sga.successPrint(string)
        print("-" * (4 + len(string)))

        output = result[1].split("\n")
        for i in output:
            print("    %s"%(i))

        print("-" * (4 + len(string)))

    else:
        sga.errorPrint("unknow command: %s"%(cmd))

