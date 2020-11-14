# -*- ubuild -*-

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import time
import webbrowser

from qprompt import alert, warn
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
    if is_running():
        warn("App server already running!")
        return
    with Cwd("app"):
        TESTSERVER = start("python app.py", "__temp-flask.log")
        alert("Application starting...")
        time.sleep(3)
        if TESTSERVER.isrunning():
            alert("Application started.")
            browse()
        else:
            warn("Issue starting application!")
            stop()

@menu
def browse():
    if not is_running():
        warn("Application not running!")
        return
    webbrowser.open(f"http://{APPADDRPORT}")

@menu
def stop():
    global TESTSERVER
    if not is_running():
        warn("Application not running!")
        return
    TESTSERVER.stop()
    TESTSERVER = None
    alert("Application stopped.")

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    main(default="r")
