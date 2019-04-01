from src.main.models.parking_lot import ParkingLot
from src.main.constants.commands import SUPPORTED_COMMANDS

import sys

class ParkingService(object):

    MEMORY_CACHE = {}

    def __init__(self):
        self.parking_slot_instance = None

    def create_parking_slot(self, command, capacity):
        if not self.parking_slot_instance:
            try:
                self.parking_slot_instance = ParkingLot(capacity)
            except Exception as error:
                return error.message
            else:
                return SUPPORTED_COMMANDS[command]['success_message'].format(capacity)

    def park_car(self, command, registration_number, color):
        if self.is_parking_slot_created():
            try:
                slot_number = self.parking_slot_instance.park(registration_number, color)
            except Exception as error:
                return error.message
            else:
                if slot_number:
                    return SUPPORTED_COMMANDS[command]['success_message'].format(slot_number)


    def leave_parking_slot(self, command, slot_number):
        if self.is_parking_slot_created():
            try:
                is_success = self.parking_slot_instance.leave(slot_number)
            except Exception as error:
                return error.message
            else:
                if is_success:
                    return SUPPORTED_COMMANDS[command]['success_message'].format(slot_number)


    def get_registration_numbers_by_color(self, command, color):
        if self.is_parking_slot_created():
            try:
                registration_numbers  = self.parking_slot_instance.get_registration_numbers_by_color(color)
            except Exception as error:
                return error.message
            else:
                if registration_numbers:
                    return registration_numbers


    def get_slot_numbers_by_color(self, command, color):
        if self.is_parking_slot_created():
            try:
                slot_numbers_by_color = self.parking_slot_instance.get_slot_numbers_by_color(color)
            except Exception as error:
                return error.message
            else:
                if slot_numbers_by_color:
                    return slot_numbers_by_color

    def get_slot_number_by_registration_number(self, command, registration_number):
        if self.is_parking_slot_created():
            try:
                slot_number = self.parking_slot_instance.get_slot_number_by_registrationno(registration_number)
            except Exception as error:
                return error.message
            else:
                if slot_number:
                    return slot_number

    def display_parking_lot(self, command):
        if self.is_parking_slot_created():
            try:
                parking_lot_info  = self.parking_slot_instance.get_parking_slot_display()
            except Exception as error:
                return error.message
            else:
                if parking_lot_info:
                    normalized_items = map(lambda car_info: [car_info['slot_no'], car_info['regno'], car_info['color']],
                                                             parking_lot_info)
                    return self.formatter(normalized_items)
                else:
                    return self.formatter([])


    def formatter(self, row_items):
        table = []
        headings = ['Slot No.  ', 'Registration No    ', 'Color']
        columns = len(headings)

        table.append(headings)

        for row in row_items:
            table.append(row)

        max_each_column = []
        for row_item in table:
            if not max_each_column:
                max_each_column = map(lambda x: len(x), row_item)
                continue
            else:
                max_each_column = map(
                    lambda index: (max_each_column[index]) if max_each_column[index] >= len(row_item[index]) else
                    len(row_item[index]), xrange(columns))

        display_row = []

        for row_item in table:
            temp_string = ""
            for index in xrange(len(row_item)):
                temp_string += str(row_item[index] + " " * ((max_each_column[index]) - len(row_item[index])))
            display_row.append(temp_string)

        return "\n".join(display_row)


    def is_parking_slot_created(self):
        return True if self.parking_slot_instance else False

    def exit(self, command):
        sys.exit(0)

