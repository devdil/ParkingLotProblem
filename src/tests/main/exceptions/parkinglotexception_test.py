from src.main.exceptions.parkinglotexception import *
import unittest

class ParkingLotExceptionTest(unittest.TestCase):

    def test_self(self):

        with self.assertRaises(InvalidCapacityException):
            raise InvalidCapacityException("message")

        with self.assertRaises(InvalidOperationException):
            raise InvalidOperationException("message")


        with self.assertRaises(IllegalArgumentException):
            raise IllegalArgumentException("message")


        with self.assertRaises(ParkingLotCapacityFilledException):
            raise ParkingLotCapacityFilledException("message")




if __name__ == "__main__":
    unittest.main()