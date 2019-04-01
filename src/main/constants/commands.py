from command_enums import Commands

SUPPORTED_COMMANDS = \
    {Commands.LEAVE.value:
        {
            "description": "Leave the parking lot given a slot number",
            "validate_regex": "^leave\s[0-9]+",
            "success_message": "Slot number {} is free"

        },
        Commands.PARK.value:
            {
                "description": "Park a car given a registration number and color of the car",
                "validate_regex": "^park\s[a-zA-z0-9-]+\s[a-zA-Z]+",
                "success_message": "Allocated slot number: {}"

            },
        Commands.CREATE_PARKING_LOT.value:
            {
                "description": "Create a parking lot with the size of the parking lot",
                "validate_regex": "^create_parking_lot\s[0-9]+",
                "success_message": "Created a parking lot with {} slots"
            },
        Commands.REGISTRATION_NUMBER_BY_COLOR.value:
            {
                "description": "Returns the registration numner of cars by color",
                "validate_regex": "^registration_numbers_for_cars_with_colour\s[a-zA-Z]+"

            },
        Commands.SLOT_NUMBERS_BV_COLOR.value:
            {
                "description": "Returns the slot numbers given the color of the car",
                "validate_regex": "^slot_numbers_for_cars_with_colour\s[a-zA-Z]+"

            },
        Commands.SLOT_NUMBER_BY_REG_NO.value:
            {
                "description": "give the slot number given the registration_number",
                "validate_regex": "^slot_number_for_registration_number\s[a-zA-Z0-9-]+"
            },
        Commands.EXIT.value: {
            "description": "Exit the command line interface",
            "validate_regex": "^exit"
        },
        Commands.STATUS.value: {
            "description": "Returns status of slots",
            "validate_regex": "^status"
        }
    }
