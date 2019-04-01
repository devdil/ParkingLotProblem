from src.main.services.parkingservice import ParkingService
from src.main.constants.command_enums import Commands

class ParkingController(object):

    def __init__(self):
        self.parkingservice = ParkingService()

    def route_command(self, command, kwargs):
        if Commands.CREATE_PARKING_LOT.value == command:
            output = self.create_parking_lot(command, int(kwargs[0]))
            return output

        if Commands.LEAVE.value == command:
            output = self.leave_parking_slot(command, int(kwargs[0]))
            return output

        if Commands.PARK.value == command:
            output = self.park_car(command, str(kwargs[0]), str(kwargs[1]))
            return output

        if Commands.EXIT.value == command:
            self.exit(command)

        if Commands.SLOT_NUMBER_BY_REG_NO.value == command:
            output = self.get_slot_number_by_registration_number(command, str(kwargs[0]))
            return output

        if Commands.REGISTRATION_NUMBER_BY_COLOR.value == command:
            output = ", ".join(self.get_registration_numbers_by_color(command, kwargs[0]))
            return output

        if Commands.SLOT_NUMBERS_BV_COLOR.value == command:
            output = ", ".join(map(lambda x: str(x), self.get_slot_numbers_by_color(command, kwargs[0])))
            return output

        if Commands.STATUS.value == command:
            output = self.display_parking_slot(command)
            return output



    def create_parking_lot(self,command, capacity):
        return self.parkingservice.create_parking_slot(command, capacity)

    def park_car(self, command, registration_number, color):
        return self.parkingservice.park_car(command, registration_number, color)

    def leave_parking_slot(self, command, slot_number):
        return self.parkingservice.leave_parking_slot(command, slot_number)

    def get_registration_numbers_by_color(self, command, color):
        return self.parkingservice.get_registration_numbers_by_color(command, color)

    def get_slot_numbers_by_color(self, command, color):
        return self.parkingservice.get_slot_numbers_by_color(command, color)

    def get_slot_number_by_registration_number(self, command, registration_number):
        return self.parkingservice.get_slot_number_by_registration_number(command, registration_number)

    def display_parking_slot(self, command):
        return self.parkingservice.display_parking_lot(command)

    def exit(self, command):
        return self.parkingservice.exit(command)



