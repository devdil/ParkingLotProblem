from src.main.constants.command_enums import Commands


import unittest

class CommandEnumTest(unittest.TestCase):


    def test_valid_enums(self):

        valid_operations = ["leave", "park", "create_parking_lot", "registration_numbers_for_cars_with_colour",
                            "slot_numbers_for_cars_with_colour",
                            "slot_number_for_registration_number", "status", "exit"]

        for enum in Commands:
            if enum.value not in valid_operations:
                raise Exception("Not a valid enum. Please add your enum to src/main/constants/commands_enum.py")