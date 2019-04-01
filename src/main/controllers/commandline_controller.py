from src.main.controllers.commandlineparsercontroller import CommandLineParserController
from src.main.controllers.parking_controller import ParkingController

class CommandLineController(object):

    def __init__(self):
        self.commandlineparser = CommandLineParserController()
        self.parkingcontroller = ParkingController()


    def process_command(self, command):

        if self.commandlineparser.validate_command(command):
            command, kwargs = self.commandlineparser.parse(command)
            print self.execute_command(command, kwargs)

    def execute_command(self, command, kwargs):
        return self.parkingcontroller.route_command(command, kwargs)


    def start_interactive(self):

        while True:
            self.process_command(raw_input().strip().rstrip())


    def start_non_interactive(self, filename):
        with open(filename, 'r') as file:
            command = file.readline().strip().rstrip()
            while command:
                self.process_command(command)
                command = file.readline().strip().rstrip()