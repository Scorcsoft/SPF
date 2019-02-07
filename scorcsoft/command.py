import scorcsoft.load
import scorcsoft.help
import scorcsoft.build
import scorcsoft.search
import scorcsoft.unload
import scorcsoft.exploit
import scorcsoft.setOption
import scorcsoft.showOption
import scorcsoft.systemCommand
import scorcsoft.globalAssets as sga

def main(cmd):
    cmdList = cmd.split(" ")

    command = cmdList[0]

    if command == "build":
        scorcsoft.build.main()

    elif command == "exit":
        pass

    elif command == "exploit":
        scorcsoft.exploit.main()

    elif command == "load":
        scorcsoft.load.main(cmd)

    elif command == "search":
        scorcsoft.search.main(cmd)

    elif command == "set":
        scorcsoft.setOption.main(cmd)

    elif command == "show":
        scorcsoft.showOption.main(cmd)

    elif command == "unload":
        scorcsoft.unload.main()

    elif command == "?":
        scorcsoft.help.main()

    elif command == "":
        pass

    else:
        scorcsoft.systemCommand.main(cmd)
        #sga.errorPrint("unknow command: %s"%(command))