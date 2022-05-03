# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import board

from .. import test_digitalio

CONNECTED_PINS = (
    (board.A0, board.A1),
    (board.A2, board.A3),
    # triple connection: SDA, SCL, TX
    (board.SDA, board.SCL),
    (board.SDA, board.TX),
    (board.RX, board.SCK),
    (board.MISO, board.MOSI),
    (board.SDA1, board.SCL1),
    )

ALL_PINS = set()
ALL_PINS.update(*CONNECTED_PINS)

test_digitalio.test(ALL_PINS, CONNECTED_PINS)
