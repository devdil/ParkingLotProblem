from src.main.controllers.commandline_controller import CommandLineController
from os import path
import sys

def start(filename, interactive=False):
    commandcontroller = CommandLineController()
    if filename and path.exists(filename) and not interactive:
        commandcontroller.start_non_interactive(filename)
    if interactive
        commandcontroller.start_interactive()

if  __name__ == '__main__':
    if len(sys.argv) > 1:
        start(sys.argv[1], interactive=False)
    else:
        start(interactive=True)
