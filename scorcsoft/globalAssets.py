global spfLogo
spfLogo = '''
.----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |    _______   | || |   ______     | || |  _________   | |
| |   /  ___  |  | || |  |_   __ \   | || | |_   ___  |  | |
| |  |  (__ \_|  | || |    | |__) |  | || |   | |_  \_|  | |
| |   '.___`-.   | || |    |  ___/   | || |   |  _|      | |
| |  |`\____) |  | || |   _| |_      | || |  _| |_       | |
| |  |_______.'  | || |  |_____|     | || | |_____|      | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'      
                                              __  _   
                                             / _|| |  
   ___   ___   ___   _ __   ___  ___   ___  | |_ | |_ 
  / __| / __| / _ \ | '__| / __|/ __| / _ \ |  _|| __|
  \__ \| (__ | (_) || |   | (__ \__ \| (_) || |  | |_ 
  |___/ \___| \___/ |_|    \___||___/ \___/ |_|   \__|

      [ Scorcsoft POC Framework By scorcsoft.com ]


'''


global module #poc module object
module = None

global modulePath #poc file path
modulePath = None

global moduleType #poc type
moduleType = None

global moduleOptions #poc options
moduleOptions = None

global initFinsh
initFinsh = False

global allPocPath #poc file path
allPocPath = []

global moduleOptionsWord
moduleOptionsWord = []

global commandPrompt
commandPrompt = '\033[4;30mspf\033[0m > '

commandWord = ["build","exit","load ","search ","set ","show","unload"]
moduleTypeList = {1: "poc",2: "scanner",3: "exploit"}

def get(key):
    try:
        return moduleOptions[key]['value']
    except:
        return ''

def infoPrint(string):
    print('\033[1;34m[*]\033[0m %s'%(string))

def infoEcho(string):
    return '\033[1;34m[*]\033[0m %s'%(string)

def successPrint(string):
    print('\033[1;32m[*]\033[0m %s'%(string))

def successEcho(string):
    return '\033[1;32m[*]\033[0m %s'%(string)

def errorPrint(string):
    print('\033[1;31m[*]\033[0m %s'%(string))

def errorEcho(string):
    return '\033[1;31m[*]\033[0m %s'%(string)

def weakPrint(string):
    print('\033[1;32m[+]\033[0m %s'%(string))

def weakEcho(string):
    return '\033[1;32m[+]\033[0m %s'%(string)

def nweakPrint(string):
    print('\033[1;31m[-]\033[0m %s'%(string))

def nweakEcho(string):
    return '\033[1;31m[-]\033[0m %s'%(string)