from src.main.controllers.commandline_controller import CommandLineController
from os import path
import sys

def start(filename):
    commandcontroller = CommandLineController()
    if filename and path.exists(filename):
        commandcontroller.start_non_interactive(filename)
    else:
        commandcontroller.start_interactive()

if  __name__ == '__main__':
    if len(sys.argv) > 1:
        start(sys.argv[1])
    else:
        start(None)