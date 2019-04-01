from src.main.controllers.commandlineparsercontroller import CommandLineParserController
from src.main.exceptions.commandlineexception import UnsupportedCommandException

import unittest

class CommandLineParserControllerTest(unittest.TestCase):

    def test_parse_command_with_correct_values(self):

        commandlinecontroller = CommandLineParserController()

        self.assertTrue(commandlinecontroller.validate_command("create_parking_lot 6"))
        self.assertTrue(commandlinecontroller.validate_command("park KA-01-HH-1234 White"))
        self.assertTrue(commandlinecontroller.validate_command("leave 4"))
        self.assertTrue(commandlinecontroller.validate_command("status"))
        self.assertTrue(commandlinecontroller.validate_command("registration_numbers_for_cars_with_colour White"))
        self.assertTrue(commandlinecontroller.validate_command("slot_numbers_for_cars_with_colour White"))
        self.assertTrue(commandlinecontroller.validate_command("slot_number_for_registration_number KA-01-HH-3141"))

    def test_parse_command_with_invalid_commands(self):

        commandlinecontroller = CommandLineParserController()

        with self.assertRaises(UnsupportedCommandException):
            commandlinecontroller.validate_command("gojek is awesome")

        with self.assertRaises(UnsupportedCommandException):
            commandlinecontroller.validate_command(None)

    def test_parser_with_valid_commmands(self):

        commandlinecontroller = CommandLineParserController()

        self.assertEqual(("create_parking_lot",['6']), commandlinecontroller.parse("create_parking_lot 6"))
        self.assertEqual(("park", ['KA-01-HH-1234','White']), commandlinecontroller.parse("park KA-01-HH-1234 White"))
        self.assertEqual(("leave", ['4']), commandlinecontroller.parse("leave 4"))
        self.assertEqual(("status", []), commandlinecontroller.parse("status"))
        self.assertEqual(("registration_numbers_for_cars_with_colour", ['White']), commandlinecontroller.parse("registration_numbers_for_cars_with_colour White"))
        self.assertEqual(("slot_numbers_for_cars_with_colour", ['White']), commandlinecontroller.parse("slot_numbers_for_cars_with_colour White"))



if __name__ == "__main__":
    unittest.main()