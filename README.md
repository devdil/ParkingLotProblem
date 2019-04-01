# Parking Lot 

ParkingLot is a small software to enable you to manage your parking needs. 
Some of the notable features include

# Features

  - Create a parking lot with given size
  - Park a car given a registration number
  - Check the status of the parking lot in a neat format
  - Remove/Vacate a parking slot
  - Interactive terminal
  - Get the registration numbers of parked colors by a given color
  - Get the slot number of a car given a registration number
  - Get the slot numnbers given a color of the car.

### Tech

* Python2.7 

### Installation

Parkinglot requires [Python 2.7.X](https://www.python.org/download/releases/2.7/) 
Note: Refer guide to installing [pip](https://pip.pypa.io/en/stable/installing/)
Install the dependencies using pip and start the server.

```sh
$ pip install virtualenv
$ virtualenv parkinglot
$ source parkinglot/bin/activate
$ ./bin/parking_lot
```

For develop environments...

```sh
$ pip install virtualenv
$ virtualenv parkinglot
$ source parkinglot/bin/activate
$ ./bin/setup
```
Note: Make sure your TEST PASSES [OK]

### Todos

 - Write MORE Tests
 - Refactor to make it more even beautiful.

### Avaialable Commands/Usage
- create_parking_lot <capacity_int>
  Example: create_parking_lot 6
  Success message: create_parking_lot 6
- park <car_reg_no> <color>
  Example: park KA-01-HH-1234 White
  Success message: Allocated slot number: 1
  Error Message: Sorry, parking lot is full
- leave <slot_number>
  Example: leave 6
  Success Message: Slot number 6 is free
- status
  Example: status
  Sucess Message:
    Slot No.  Registration No    Color
    1         KA-01-HH-1234      White
    2         KA-01-HH-9999      White

- registration_numbers_for_cars_with_colour <car_color>
  Example: registration_numbers_for_cars_with_colour White
  Success Message: KA-01-P-333, KA-01-HH-9999, KA-01-HH-1234

- slot_numbers_for_cars_with_colour <car_color>
  Example: slot_numbers_for_cars_with_colour White
  Success Message: 1, 2, 4

- slot_number_for_registration_number <car_reg_no>
  Example: slot_number_for_registration_number KA-01-HH-3141
  SuccessMessage: 6
  Error Message: Not found

- exit
  Example: exit
  Sucess Message: None




### Examples
```
.parking_lot)$ ./bin/setup
create_parking_lot 6
Created a parking lot with 6 slots
park KA-01-HH-1234 White
Allocated slot number: 1
park KA-01-HH-9999 White
Allocated slot number: 2
park KA-01-BB-0001 Black
Allocated slot number: 3
park KA-01-HH-7777 Red
Allocated slot number: 4
park KA-01-HH-2701 Blue
Allocated slot number: 5
park KA-01-HH-3141 Black
Allocated slot number: 6
leave 4
Slot number 4 is free
status
Slot No.  Registration No    Color
1         KA-01-HH-1234      White
2         KA-01-HH-9999      White
3         KA-01-BB-0001      Black
5         KA-01-HH-2701      Blue
6         KA-01-HH-3141      Black
park KA-01-P-333 White
Allocated slot number: 4
park DL-12-AA-9999 White
Sorry, parking lot is full
registration_numbers_for_cars_with_colour White
KA-01-P-333, KA-01-HH-9999, KA-01-HH-1234
slot_numbers_for_cars_with_colour White
1, 2, 4
slot_number_for_registration_number KA-01-HH-3141
6
slot_number_for_registration_number MH-04-AY-1111
Not found
exit
(parking_lot) $
```



License
----

MIT


**Free Software, Hell Yeah!**

