# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from digitalio import DigitalInOut, Direction, Pull, DriveMode

def test_pin(pin):
    dio = DigitalInOut(pin)

    # Initially: input, no pull, value is low, no drive mode
    assert dio.direction == Direction.INPUT
    assert dio.pull is None

    try:
        dio.value = True
        raise AssertionError(".value worked when input")
    except AttributeError:
        pass

    try:
        dio.drive_mode
        raise AssertionError(".drive_mode worked when input")
    except AttributeError:
        pass

    dio.pull = Pull.UP
    assert dio.pull == Pull.UP
    assert dio.value is True

    dio.pull = Pull.DOWN
    assert dio.pull == Pull.DOWN
    assert dio.value is False

    dio.pull = None
    assert dio.pull is None

    dio.switch_to_input(pull=None)
    assert dio.direction == Direction.INPUT
    assert dio.pull is None

    dio.switch_to_input(pull=Pull.UP)
    assert dio.direction == Direction.INPUT
    assert dio.pull == Pull.UP
    assert dio.value is True

    dio.switch_to_input(pull=Pull.DOWN)
    assert dio.direction == Direction.INPUT
    assert dio.pull == Pull.DOWN
    assert dio.value is False

    dio.switch_to_output()
    try:
        dio.pull
        raise AssertionError(".pull worked when output")
    except AttributeError:
        pass

    dio.switch_to_output(value=False, drive_mode=DriveMode.PUSH_PULL)
    assert dio.direction == Direction.OUTPUT
    assert dio.drive_mode == DriveMode.PUSH_PULL
    assert dio.value is False

    dio.switch_to_output(value=False, drive_mode=DriveMode.OPEN_DRAIN)
    assert dio.direction == Direction.OUTPUT
    assert dio.drive_mode == DriveMode.OPEN_DRAIN
    assert dio.value is False

    dio.switch_to_output(value=False, drive_mode=DriveMode.PUSH_PULL)
    assert dio.direction == Direction.OUTPUT
    assert dio.drive_mode == DriveMode.PUSH_PULL
    assert dio.value is False

    dio.switch_to_output(value=False, drive_mode=DriveMode.OPEN_DRAIN)
    assert dio.direction == Direction.OUTPUT
    assert dio.drive_mode == DriveMode.OPEN_DRAIN
    assert dio.value is False

    dio.switch_to_output(value=True, drive_mode=DriveMode.PUSH_PULL)
    assert dio.direction == Direction.OUTPUT
    assert dio.drive_mode == DriveMode.PUSH_PULL
    assert dio.value is True

    dio.switch_to_output(value=True, drive_mode=DriveMode.OPEN_DRAIN)
    assert dio.direction == Direction.OUTPUT
    assert dio.drive_mode == DriveMode.OPEN_DRAIN
    assert dio.value is True

    dio.switch_to_input()
    assert dio.direction == Direction.INPUT

    dio.deinit()
    try:
        dio.value
        assert AssertionError(".value worked after deinit()")
    except ValueError:
        pass


def test_pin_pair(pin1, pin2):
    dio1 = DigitalInOut(pin1)
    dio2 = DigitalInOut(pin2)

    dio1.pull = Pull.UP
    assert dio2.value is True

    dio1.pull = Pull.DOWN
    assert dio2.value is False

    dio1.pull = None

    dio2.switch_to_output(value=False, drive_mode=DriveMode.PUSH_PULL)

    assert dio1.value is False

    dio2.value = True
    assert dio1.value is True

    dio2.value = False
    dio2.drive_mode = DriveMode.OPEN_DRAIN
    assert dio1.value is False  ## ?

    dio1.pull = Pull.UP
    assert dio1.value is False

    dio2.value = True
    assert dio1.value is True

    dio1.deinit()
    dio2.deinit()



def test(all_pins, connected_pins):
    for pin in all_pins:
        print("testing pin:", pin)
        test_pin(pin)

    for (pin1, pin2) in connected_pins:
        print("testing pin pair:", pin1, pin2)
        test_pin_pair(pin1, pin2)

        print("testing pin pair:", pin2, pin1)
        test_pin_pair(pin2, pin1)
