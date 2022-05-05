# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import board

from adafruit_port_test import test_digitalio

PIN1 = board.A1
PIN2 = board.A2

input(f"Remove any jumper from {PIN1} and press return:")
print(f"Testing digitalio.DigitalInOut on {PIN1}")
test_digitalio.test_pin(PIN1)
print("OK")

input(f"Jumper {PIN1} to {PIN2} and press enter:")
print(f"Testing digitalio.DigitalInOut between {PIN1} and {PIN2}")

test_digitalio.test_pin_pair(PIN1, PIN2)
print("OK")
