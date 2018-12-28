# -*- ubuild -*-

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import time
import webbrowser

from qprompt import warn
from auxly.shell import call, iterout
from auxly.filesys import Cwd
from ubuild import menu, main

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

SRVWINTITLE = "FlaskVue Demo App Server"

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def is_running():
    for line in iterout("netstat -a -n"):
        if "127.0.0.1:5000" in line and "TCP" in line and "LISTENING" in line:
            return True
    return False

@menu
def run():
    if not is_running():
        with Cwd("app"):
            call(f'start "{SRVWINTITLE}" python app.py')
    else:
        warn("App server already running!")
    time.sleep(3)
    open_browser()

@menu
def open_browser():
    if not is_running():
        warn("App not yet running!")
        return
    webbrowser.open("http://127.0.0.1:5000/")

@menu
def kill_server():
    if is_running():
        call(f'taskkill /fi "WINDOWTITLE eq {SRVWINTITLE}"')
    else:
        warn("Could not find running server!")

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    main(default="r")
