from src.main.services.parkingservice import ParkingService
from src.main.constants.commands import Commands
import unittest

class ParkingServiceTest(unittest.TestCase):

    def test_happy_path(self):

        parkinglotservice = ParkingService()
        parkinglotservice.create_parking_slot(Commands.CREATE_PARKING_LOT.value, 4)
        self.assertEqual("Allocated slot number: 1",parkinglotservice.park_car(Commands.PARK.value, 'A', "Blue"))
        self.assertEqual("Allocated slot number: 2", parkinglotservice.park_car(Commands.PARK.value, 'B', "White"))
        self.assertEqual("Allocated slot number: 3",parkinglotservice.park_car(Commands.PARK.value, 'C', "White"))
        self.assertEqual("Allocated slot number: 4",parkinglotservice.park_car(Commands.PARK.value, 'D', "Blue"))

        self.assertEqual("Sorry, parking lot is full", parkinglotservice.park_car(Commands.PARK.value, "E","Yellow"))


        self.assertEqual("Slot number 4 is free", parkinglotservice.leave_parking_slot(Commands.LEAVE.value, 4))

    def test_happy_path2(self):
        parkinglotservice = ParkingService()
        parkinglotservice.create_parking_slot(Commands.CREATE_PARKING_LOT.value, 6)
        self.assertEqual("Allocated slot number: 1", parkinglotservice.park_car(Commands.PARK.value, 'A', "White"))
        self.assertEqual("Allocated slot number: 2", parkinglotservice.park_car(Commands.PARK.value, 'B', "White"))
        self.assertEqual("Allocated slot number: 3", parkinglotservice.park_car(Commands.PARK.value, 'C', "Black"))
        self.assertEqual("Allocated slot number: 4", parkinglotservice.park_car(Commands.PARK.value, 'D', "Red"))
        self.assertEqual("Allocated slot number: 5", parkinglotservice.park_car(Commands.PARK.value, 'E', "Blue"))
        self.assertEqual("Allocated slot number: 6", parkinglotservice.park_car(Commands.PARK.value, 'F', "Black"))
        self.assertEqual("Slot number 4 is free", parkinglotservice.leave_parking_slot(Commands.LEAVE.value, 4))
        self.assertEqual("Allocated slot number: 4", parkinglotservice.park_car(Commands.PARK.value, 'D', "White"))
        self.assertEqual("Sorry, parking lot is full", parkinglotservice.park_car(Commands.PARK.value, 'G', "White"))


        self.assertEqual(", ".join(sorted(['A', 'B', 'D'])),
                         ", ".join(sorted(parkinglotservice.get_registration_numbers_by_color(
                             Commands.REGISTRATION_NUMBER_BY_COLOR.value, 'White'))))

        self.assertEqual(sorted([1,2,4])    ,
                         sorted(parkinglotservice.get_slot_numbers_by_color(Commands.SLOT_NUMBERS_BV_COLOR.value,
                                                                          'White')))

        self.assertEqual(1, parkinglotservice.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'A'))
        self.assertEqual(2, parkinglotservice.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'B'))
        self.assertEqual(3, parkinglotservice.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'C'))
        self.assertEqual(4, parkinglotservice.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'D'))
        self.assertEqual(5, parkinglotservice.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'E'))
        self.assertEqual(6, parkinglotservice.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'F'))

        self.assertEqual("Not found", parkinglotservice.get_slot_number_by_registration_number(Commands.SLOT_NUMBER_BY_REG_NO.value,
                                                                                   'Z'))

    def test_formatter_when_there_is_nocar(self):

        parkinglotservice = ParkingService()
        parkinglotservice.create_parking_slot(Commands.CREATE_PARKING_LOT.value, 4)

        self.assertEqual('Slot No.  Registration No    Color', parkinglotservice.display_parking_lot(Commands.STATUS.value))

    def test_formatter_when_there_is_valid_car(self):

        parkinglotservice = ParkingService()
        parkinglotservice.create_parking_slot(Commands.CREATE_PARKING_LOT.value, 1)
        self.assertEqual("Allocated slot number: 1", parkinglotservice.park_car(Commands.PARK.value, 'A', "White"))

        self.assertEqual('Slot No.  Registration No    Color\n1         A                  White',
                         parkinglotservice.display_parking_lot(Commands.STATUS.value))



