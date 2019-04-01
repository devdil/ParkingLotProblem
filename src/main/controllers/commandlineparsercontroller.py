from src.main.constants.commands import SUPPORTED_COMMANDS
from src.main.exceptions.commandlineexception import UnsupportedCommandException

import re

class CommandLineParserController(object):

    VALID_SUPPORTED_COMMANDS_REGULAR_EXPRESSIONS = [value['validate_regex'] for value in SUPPORTED_COMMANDS.values()]
    SUPPORTED_COMMANDS = [ command for command in SUPPORTED_COMMANDS.keys()]

    def parse(self, command):
        if not command:
            raise UnsupportedCommandException("Command should be supported")
        else:
            if self.validate_command(command):
                command_split = command.split(' ')
                return (command_split[0], command_split[1:])


    def validate_command(self, command):
        if command:
            for supported_regular_expression in CommandLineParserController.VALID_SUPPORTED_COMMANDS_REGULAR_EXPRESSIONS:
                matched_command = re.findall(supported_regular_expression, command)
                if matched_command:
                    return True
            raise UnsupportedCommandException("Command {} not supported! Available commands are {}".format(command, CommandLineParserController.SUPPORTED_COMMANDS))
        else:
            raise UnsupportedCommandException("Command {} not supported! Available commands are {}".format(command,
                                                                                                           CommandLineParserController.SUPPORTED_COMMANDS))


