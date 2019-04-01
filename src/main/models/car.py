class Car(object):

    def __init__(self, registration_number, color):
        self.registration_number = registration_number
        self.color = color

    @property
    def registration_number(self):
        return self.__registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        self.__registration_number = registration_number

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color




