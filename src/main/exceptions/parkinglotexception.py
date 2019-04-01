class InvalidOperationException(Exception):
    "Invalid Operation Exeception raised when an operation is invalid"
    pass

class IllegalArgumentException(Exception):
    " Illegal Argument execption raised when an argument is invalid"
    pass

class InvalidCapacityException(Exception):
    pass

class ParkingLotCapacityFilledException(Exception):
    pass

class CarAlreadyException(Exception):
    pass

class SlotAlreadyVacantException(Exception):
    pass