from enum import Enum

class Commands(Enum):
    LEAVE="leave"
    PARK="park"
    CREATE_PARKING_LOT="create_parking_lot"
    REGISTRATION_NUMBER_BY_COLOR="registration_numbers_for_cars_with_colour"
    SLOT_NUMBERS_BV_COLOR="slot_numbers_for_cars_with_colour"
    SLOT_NUMBER_BY_REG_NO="slot_number_for_registration_number"
    STATUS="status"
    EXIT="exit"
