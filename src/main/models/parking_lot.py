from src.main.exceptions.parkinglotexception import *
from src.main.exceptions.parkinglotexception import IllegalArgumentException
from src.main.models.car import Car

import heapq

class ParkingLot(object):

    def __init__(self, capacity):
        """
        Initializes parking lot with parking capacity

        Args:
            capacity(int) : The size of the parking lot
        """
        if not capacity or type(capacity) is not int or capacity <= 0:
            raise InvalidCapacityException("Capacity is not proper. capacity should be a valid integer and should be > 0")
        else:
            self.capacity = capacity
            self.available_slots = [x+1 for x in xrange(capacity)]
            heapq.heapify(self.available_slots)
            self.slot_to_car_map = {}
            self.color_to_registration_map = {}
            self.regno_to_slot_map = {}
            self.color_to_slots = {}
            self.filled  = 0


    def leave(self, slot_number):
        """
        API to vacate a slot given a slot number

        Args:
            slot_number(int): The slot number you want to vacate

        Returns:
             True if operation is successfull
        Raises:
            InvalidOperationException: if operation is invalid
        """
        if self.is_slot_valid(slot_number):
            # algorithm
            # get the car_info and get its color and reg no
            # update the slot_map to an empty dict
            # remove the car reg number from the registration number to slot map
            # remove the reg number from color to car map
            # remove the value of color_slots if length of value is 1 or just remove the key

            car_info = self.slot_to_car_map[slot_number]
            car_color = car_info.color
            car_regno = car_info.registration_number


            del self.slot_to_car_map[slot_number]
            del self.regno_to_slot_map[car_regno]
            del self.color_to_registration_map[car_color][car_regno]

            if len(self.color_to_slots[car_color]) > 1:
                del self.color_to_slots[car_color][slot_number]
            else:
                del self.color_to_slots[car_color]

            heapq.heappush(self.available_slots, slot_number)
            heapq.heapify(self.available_slots)
            self.filled -= 1

            return True

    def park(self, registration_number, color):

        """
            Parks a car given a registration number and color

            Args:
                registration_number(string) : The registration number for the car
                color(string): the color
            Returns:
                available_slot_number(int): The slot number allocated to the car
            Raises:
                CarAlreadyException : if car is already parked
                ParkingLotCapacityFilledException: if there is no room for the cars to be parked.

        """

        if self._can_be_parked(registration_number):
            car = Car(registration_number, color)
            available_slot_number = self._get_free_slot()
            self.slot_to_car_map[available_slot_number] = car
            
            # update color to registration number map

            if color in self.color_to_registration_map:
                self.color_to_registration_map[color].update({ registration_number : True})
            else:
                self.color_to_registration_map[color] = { registration_number : True}

            # update registration number to slot map
            self.regno_to_slot_map[registration_number] = available_slot_number

            if color in self.color_to_slots:
                self.color_to_slots[color].update({available_slot_number: True})
            else:
                self.color_to_slots[color] = {available_slot_number: True}

            self.filled += 1

            return available_slot_number

    def is_slot_valid(self, slot_number):
        if type(slot_number) != int:
            raise IllegalArgumentException("Slot number should an int")
        if slot_number > self.capacity and slot_number >0:
            raise IllegalArgumentException("Slot number should be a valid range betwen 1 and {}".format(self.capacity))
        elif slot_number not in self.slot_to_car_map:
            raise SlotAlreadyVacantException("Slot number {} is already vacant! Please enter a valid slot number".format(slot_number))
        else:
            return True

    def _update_available_slots(self, slot_number):
        del self.available_slots[slot_number]

    def _get_free_slot(self):
        available_slot = heapq.heappop(self.available_slots)
        return available_slot


    def _can_be_parked(self, registration_number):
        # check if the registration number is already parked
        # check if there are enough spaces to park
        if registration_number in self.regno_to_slot_map:
            raise CarAlreadyException("Car with reg no {} is already parked!".format(registration_number))
        elif self.filled == self.capacity:
            raise ParkingLotCapacityFilledException("Sorry, parking lot is full")
        else:
            return True

    def _get_available_slots(self):
        return [x for x in self.available_slots]


    def _get_count_available_slots(self):
        return (self.capacity - self.filled)


    def get_registration_numbers_by_color(self, color):
        if self.color_to_registration_map:
            if color not in self.color_to_registration_map:
                raise InvalidOperationException("Color {} does not exist in the Parking lot! Please try aga" \
                                                "with a valid color");
            else:
                return [registration_number for registration_number in self.color_to_registration_map[color].keys()]
        else:
            raise InvalidOperationException("No cars inside parking lot")

    def get_slot_numbers_by_color(self, color):
        if self.color_to_slots:
            if color not in self.color_to_slots:
                raise InvalidOperationException("Color {} does not exist in the Parking lot! Please try aga" \
                                                "with a valid color");
            else:
                return [slot_number for slot_number in self.color_to_slots[color].keys()]
        else:
            raise InvalidOperationException("No cars inside parking lot")


    def get_slot_number_by_registrationno(self, registration_number):
        if self.regno_to_slot_map:
            if registration_number not in self.regno_to_slot_map:
                raise InvalidOperationException("Not found")
            else:
                return self.regno_to_slot_map[registration_number]
        else:
            raise InvalidOperationException("No cars parked in the parking lot")

    def get_parking_slot_display(self):
        if self.slot_to_car_map:
            final_items = []
            for slot_number, car_info in self.slot_to_car_map.iteritems():
                final_items.append({'slot_no' :  str(slot_number), 'regno' : car_info.registration_number, 'color' : car_info.color })
            return final_items
        else:
            return []













