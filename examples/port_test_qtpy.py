# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import board

from adafruit_port_test import test_digitalio

input("Remove any jumper from A1 and press return:")
print("Testing digitalio.DigitalInOut board.A1")
test_digitalio.test_pin(board.A1)
print("OK")

input("Jumper A1 to A2 and press return:")
print("Testing digitalio.DigitalInOut between board.A1 and board.A2")
test_digitalio.test_pin_pair(board.A1, board.A2)
print("OK")
