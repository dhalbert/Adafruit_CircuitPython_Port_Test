# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import board

from adafruit_port_test import test_analogio

AIN_PIN = board.A0
AOUT_PIN = board.A2

input("Remove any jumpers and press Enter:")
print(f"Testing analogio.AnalogIn on {AIN_PIN}")
test_analogio.test_analogin_pin(AIN_PIN)
print("OK")

print(f"Testing analogio.AnalogOut on {AOUT_PIN}")
test_analogio.test_pin(AOUT_PIN)
print("OK")

input("Jumper {PIN1} to {PIN2} and press enter:".format(PIN1=PIN1, PIN2=PIN2))
print(
    "Testing digitalio.DigitalInOut between {PIN1} and {PIN2}".format(
        PIN1=PIN1, PIN2=PIN2
    )
)
test_digitalio.test_pin_pair(PIN1, PIN2)
print("OK")
