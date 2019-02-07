import time
import readline
import threading
import scorcsoft.command
import scorcsoft.globalAssets as sga

global word
word = sga.commandWord
global exit
exit = False

class getLinbeBuffer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global word
        global exit
        while not exit:
            buffer = readline.get_line_buffer()
            if buffer[0:4] == 'load':
                word = sga.allPocPath

            elif buffer[0:3] == "set":
                word = sga.moduleOptionsWord

            else:
                word = sga.commandWord
            time.sleep(0.5)

def autoComplete():
    def custom_complete(text, state):
        results = [x for x in word if x.startswith(text)] + [None]
        return results[state]

    return custom_complete


def main():
    t = getLinbeBuffer()
    t.start()
    global exit

    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")
    readline.set_completer(autoComplete())


    cmd = ""
    while cmd != "exit":
        try:

            cmd = input(sga.commandPrompt)
            scorcsoft.command.main(cmd)

        except (EOFError, KeyboardInterrupt) as e: #intercept Ctrl + c
            print("")
            if input(sga.infoEcho("Are you sure you want to quit SPF? [y/n] ")) == 'y':
                cmd = "exit"
    exit = True



