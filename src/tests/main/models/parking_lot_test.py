from src.main.models.parking_lot import ParkingLot
from src.main.exceptions.parkinglotexception import *

import unittest

class TestParkingLot(unittest.TestCase):


    def test_invalid_values_on_initialization(self):

        with self.assertRaises(InvalidCapacityException):
            ParkingLot(None)
        with self.assertRaises(InvalidCapacityException):
            ParkingLot(0)
        with self.assertRaises(InvalidCapacityException):
            ParkingLot("foobar")


    def test_return_capacity(self):

        parking_lot = ParkingLot(10)
        self.assertEqual(10, parking_lot._get_count_available_slots())
        self.assertEqual(sorted([x+1 for x in xrange(10)]), sorted(parking_lot._get_available_slots()))


    def test_leave_when_there_is_cars(self):
        parking_lot = ParkingLot(5)

        with self.assertRaises(IllegalArgumentException):
            parking_lot.leave("blah")
            parking_lot.leave(None)
            parking_lot.leave(True)

        with self.assertRaises(SlotAlreadyVacantException):
            for x in xrange(5):
                parking_lot.leave(5)


    def test_when_parked_to_its_capacity(self):

        parking_lot = ParkingLot(5)

        parking_lot.park('A','violet')
        parking_lot.park('B', 'blue')
        parking_lot.park('C', 'green')
        parking_lot.park('D', 'yellow')
        parking_lot.park('E', 'green')

        with self.assertRaises(ParkingLotCapacityFilledException):
            parking_lot.park('F', 'green')


    def test_when_registration_duplicate(self):

        parking_lot = ParkingLot(1)

        parking_lot.park('A', 'white')

        with self.assertRaises(CarAlreadyException):
            parking_lot.park('A', 'white')


    def test_parking_lot_add_remove(self):

        parking_lot = ParkingLot(2)

        self.assertEqual(2, parking_lot._get_count_available_slots())

        parking_lot.park('A', 'white')
        parking_lot.park('B', 'blue')

        self.assertEqual(0, parking_lot._get_count_available_slots())
        parking_lot.leave(2)
        self.assertEqual(1, parking_lot._get_count_available_slots())

        parking_lot.park('B', 'blue')
        self.assertEqual(0, parking_lot._get_count_available_slots())

        self.assertEqual([], parking_lot._get_available_slots())

        parking_lot.leave(1)
        parking_lot.leave(2)

        self.assertEqual(2, parking_lot._get_count_available_slots())

        with self.assertRaises(SlotAlreadyVacantException):
            parking_lot.leave(1)
            parking_lot.leave(2)

    def test_registration_number_by_color_invalid_color(self):

        parking_lot = ParkingLot(2)

        self.assertEqual(2, parking_lot._get_count_available_slots())

        parking_lot.park('A', 'white')
        parking_lot.park('B', 'blue')

        with self.assertRaises(InvalidOperationException):
            parking_lot.get_registration_numbers_by_color('foobar')

        with self.assertRaises(InvalidOperationException):
            parking_lot.get_registration_numbers_by_color('yellow')


    def test_registration_number_color_valid_color(self):

        parking_lot = ParkingLot(2)

        self.assertEqual(2, parking_lot._get_count_available_slots())

        parking_lot.park('A', 'white')
        parking_lot.park('B', 'blue')

        self.assertEqual(['A'], parking_lot.get_registration_numbers_by_color('white'))
        self.assertEqual(['B'], parking_lot.get_registration_numbers_by_color('blue'))

    def test_registration_number_color_valid_same_color(self):

        parking_lot = ParkingLot(2)

        self.assertEqual(2, parking_lot._get_count_available_slots())

        parking_lot.park('A', 'white')
        parking_lot.park('B', 'white')

        self.assertEqual(['A', 'B'], parking_lot.get_registration_numbers_by_color('white'))


    def test_slot_number_by_registration_invalid_reg_no(self):


        parking_lot = ParkingLot(2)

        self.assertEqual(2, parking_lot._get_count_available_slots())

        parking_lot.park('A', 'white')
        parking_lot.park('B', 'blue')

        with self.assertRaises(InvalidOperationException):
            parking_lot.get_slot_number_by_registrationno('foobbar')

    def test_slot_number_by_registration_valid_reg_no(self):


        parking_lot = ParkingLot(4)

        self.assertEqual(4, parking_lot._get_count_available_slots())

        parking_lot.park('A', 'white')
        parking_lot.park('B', 'blue')
        parking_lot.park('C', 'grey')
        parking_lot.park('D', 'orange')

        self.assertEqual(1, parking_lot.get_slot_number_by_registrationno('A'))
        self.assertEqual(2, parking_lot.get_slot_number_by_registrationno('B'))

        parking_lot.leave(2)
        parking_lot.leave(3)

        parking_lot.park('E', 'blue')

        self.assertEqual(2, parking_lot.get_slot_number_by_registrationno('E'))


    def test_slot_numbers_by_color_white_valid(self):

        parking_lot = ParkingLot(3)

        self.assertEqual(3, parking_lot._get_count_available_slots())

        parking_lot.park('A', 'blue')
        parking_lot.park('B', 'blue')
        parking_lot.park('C', 'blue')

        self.assertEqual([1,2,3], parking_lot.get_slot_numbers_by_color('blue'))

        parking_lot.leave(1)
        parking_lot.leave(3)

        self.assertEqual([2], parking_lot.get_slot_numbers_by_color('blue'))


    def test_slot_numbers_by_color_white_invalid(self):

        parking_lot = ParkingLot(3)

        self.assertEqual(3, parking_lot._get_count_available_slots())

        parking_lot.park('A', 'blue')
        parking_lot.park('B', 'blue')
        parking_lot.park('C', 'blue')

        with self.assertRaises(InvalidOperationException):
            parking_lot.get_slot_numbers_by_color('foobar')


    def test_slot_numbers_by_color_white_valid_but_when_exhausted(self):

        parking_lot = ParkingLot(3)

        self.assertEqual(3, parking_lot._get_count_available_slots())

        parking_lot.park('A', 'blue')
        parking_lot.park('B', 'blue')
        parking_lot.park('C', 'blue')

        parking_lot.leave(1)
        parking_lot.leave(2)
        parking_lot.leave(3)


    def test_parking_lot_display_when_there_are_no_items(self):

        parking_lot = ParkingLot(3)

        self.assertEqual([], parking_lot.get_parking_slot_display())

    def test_parking_lot_display_when_there_are_valid_items(self):

        parking_lot = ParkingLot(3)
        parking_lot.park('A', 'blue')
        parking_lot.park('B', 'blue')
        parking_lot.park('C', 'blue')

        self.assertEqual([['1','A','blue'],['2','B','blue'],['3','C','blue']], map(lambda car_info: [car_info['slot_no'], car_info['regno'], car_info['color']],
                                                             parking_lot.get_parking_slot_display()))


if __name__ == "__main__":
    unittest.main()