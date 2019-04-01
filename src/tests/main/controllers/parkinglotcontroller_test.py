from src.main.controllers.parking_controller import ParkingController
from src.main.constants.command_enums import Commands

import unittest


class TestParkingController(unittest.TestCase):


    def test_happy_path(self):

        parkinglotcntlr = ParkingController()
        parkinglotcntlr.create_parking_lot(Commands.CREATE_PARKING_LOT.value, 4)
        self.assertEqual("Allocated slot number: 1",parkinglotcntlr.park_car(Commands.PARK.value, 'A', "Blue"))
        self.assertEqual("Allocated slot number: 2", parkinglotcntlr.park_car(Commands.PARK.value, 'B', "White"))
        self.assertEqual("Allocated slot number: 3",parkinglotcntlr.park_car(Commands.PARK.value, 'C', "White"))
        self.assertEqual("Allocated slot number: 4",parkinglotcntlr.park_car(Commands.PARK.value, 'D', "Blue"))

        self.assertEqual("Sorry, parking lot is full", parkinglotcntlr.park_car(Commands.PARK.value, "E","Yellow"))


        self.assertEqual("Slot number 4 is free", parkinglotcntlr.leave_parking_slot(Commands.LEAVE.value, 4))

    def test_happy_path2(self):
        parkinglotcntlr = ParkingController()
        parkinglotcntlr.create_parking_lot(Commands.CREATE_PARKING_LOT.value, 6)
        self.assertEqual("Allocated slot number: 1", parkinglotcntlr.park_car(Commands.PARK.value, 'A', "White"))
        self.assertEqual("Allocated slot number: 2", parkinglotcntlr.park_car(Commands.PARK.value, 'B', "White"))
        self.assertEqual("Allocated slot number: 3", parkinglotcntlr.park_car(Commands.PARK.value, 'C', "Black"))
        self.assertEqual("Allocated slot number: 4", parkinglotcntlr.park_car(Commands.PARK.value, 'D', "Red"))
        self.assertEqual("Allocated slot number: 5", parkinglotcntlr.park_car(Commands.PARK.value, 'E', "Blue"))
        self.assertEqual("Allocated slot number: 6", parkinglotcntlr.park_car(Commands.PARK.value, 'F', "Black"))
        self.assertEqual("Slot number 4 is free", parkinglotcntlr.leave_parking_slot(Commands.LEAVE.value, 4))
        self.assertEqual("Allocated slot number: 4", parkinglotcntlr.park_car(Commands.PARK.value, 'D', "White"))
        self.assertEqual("Sorry, parking lot is full", parkinglotcntlr.park_car(Commands.PARK.value, 'G', "White"))


        self.assertEqual(", ".join(sorted(['A', 'B', 'D'])),
                         ", ".join(sorted(parkinglotcntlr.get_registration_numbers_by_color(
                             Commands.REGISTRATION_NUMBER_BY_COLOR.value, 'White'))))

        self.assertEqual(sorted([1,2,4])    ,
                         sorted(parkinglotcntlr.get_slot_numbers_by_color(Commands.SLOT_NUMBERS_BV_COLOR.value,
                                                                          'White')))

        self.assertEqual(1, parkinglotcntlr.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'A'))
        self.assertEqual(2, parkinglotcntlr.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'B'))
        self.assertEqual(3, parkinglotcntlr.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'C'))
        self.assertEqual(4, parkinglotcntlr.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'D'))
        self.assertEqual(5, parkinglotcntlr.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'E'))
        self.assertEqual(6, parkinglotcntlr.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'F'))

        self.assertEqual("Not found", parkinglotcntlr.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'Z'))


    def test_happy_path_using_route(self):

        parkinglotcntlr = ParkingController()
        parkinglotcntlr.route_command(Commands.CREATE_PARKING_LOT.value, ['4'])
        self.assertEqual("Allocated slot number: 1", parkinglotcntlr.route_command(Commands.PARK.value, ['A', "Blue"]))
        self.assertEqual("Allocated slot number: 2", parkinglotcntlr.route_command(Commands.PARK.value, ['B', "White"]))
        self.assertEqual("Allocated slot number: 3", parkinglotcntlr.route_command(Commands.PARK.value, ['C', "White"]))
        self.assertEqual("Allocated slot number: 4", parkinglotcntlr.route_command(Commands.PARK.value, ['D', "Blue"]))

        self.assertEqual("Sorry, parking lot is full", parkinglotcntlr.route_command(Commands.PARK.value, ["E","Yellow"]))


        self.assertEqual("Slot number 4 is free", parkinglotcntlr.route_command(Commands.LEAVE.value, *['4']))



if __name__ == "__main__":
    unittest.main()