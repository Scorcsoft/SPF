import threading
import scorcsoft.main
from time import sleep
import scorcsoft.initialize
import scorcsoft.globalAssets as sga


class load(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        scorcsoft.initialize.main()
        sga.initFinsh = True




if __name__ == "__main__":
    t1 = load()
    t1.start()

    while not sga.initFinsh:
        l = ['|','/','-','\\']
        for i in l:
            string = "\r[%s] scorcsoft proof of concept framework is initializeing..."%(i)
            print(string,end="")
            sleep(0.2)

    print("\r" + " " * len(string),end="")
    print("\n")
    print(sga.spfLogo,end="")
    scorcsoft.main.main()