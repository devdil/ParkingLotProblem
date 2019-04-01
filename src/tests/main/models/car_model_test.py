from src.main.models.parking_lot import Car

import unittest

class CarModelTest(unittest.TestCase):

    def test_car_initialization(self):

        car = Car('R1', 'white')

        self.assertEqual('white', car.color)
        self.assertEqual('R1', car.registration_number)

if __name__ == "__main__":
    unittest.main()