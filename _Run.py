# -*- ubuild -*-

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import time
import webbrowser

from qprompt import warn
from auxly.shell import start
from auxly.filesys import Cwd
from ubuild import menu, main

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

APPADDRPORT = "127.0.0.1:5000"
TESTSERVER = None

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def is_running():
    global TESTSERVER
    return TESTSERVER != None

@menu
def run():
    global TESTSERVER
    if not is_running():
        with Cwd("app"):
            TESTSERVER = start("python app.py")
            time.sleep(3)
            open_browser()
    else:
        warn("App server already running!")

@menu
def open_browser():
    if not is_running():
        warn("App not yet running!")
        return
    webbrowser.open(f"http://{APPADDRPORT}")

@menu
def kill_server():
    global TESTSERVER
    if is_running():
        TESTSERVER.kill()
        TESTSERVER = None
    else:
        warn("Could not find running server!")

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    main(default="r")
