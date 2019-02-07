#-----------------------------------required-----------------------------------
#import othermodule

import scorcsoft.globalAssets as sga
#import scscscs
keyword = "test" #search keyword
author = "scorcsoft.com" #your name
type = 2 #int 1: poc,2: scanner,3: exploit
date = "2019-01-15"
info = "the SFW test module" #this module information

options = {
    "rhost": {"info": "the target ip address","value": ""},
    "rport": {"info": "the target port","value": "80"}
}










def exploit(): #poc main function


    sga.infoPrint("test module, target host: %s, target port: %s"%(sga.get("rhost"),sga.get("rport")))

    sga.successPrint("this is a successfully message for test")

    sga.errorPrint("this is an error message for test")

    sga.weakPrint("the target is vulnerable")

    sga.infoPrint("哈哈骗你的,想什么呢")

    sga.nweakPrint("the target is not vulnerable!")
    #sga.commandPrompt = "hahaah > "

#-----------------------------------required-----------------------------------
