# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from digitalio import DigitalInOut, Direction, Pull, DriveMode

def reset_pin(pin):
    dio = DigitalInOut(pin)
    dio.deinit()

def test_pin(pin):
    dio = DigitalInOut(pin)

    # Initially: input, no pull, value is low, no drive mode
    assert dio.direction == Direction.INPUT, f"{pin} .direction should be INPUT to start"
    assert dio.pull is None, f"{pin} .pull should be None to start"

    try:
        dio.value = True
        raise AssertionError(f"{pin} .value should not work when INPUT")
    except AttributeError:
        pass

    try:
        _ = dio.drive_mode
        raise AssertionError(f"{pin} .drive_mode should not work when INPUT")
    except AttributeError:
        pass

    dio.pull = Pull.UP
    assert dio.pull == Pull.UP, f"{pin} .pull should be UP"
    assert dio.value is True, f"{pin} .value should be True after setting .pull to UP"

    dio.pull = Pull.DOWN
    assert dio.pull == Pull.DOWN, f"{pin} .pull should be DOWN"
    assert dio.value is False, f"{pin} .value should be False after setting .pull to DOWN"

    dio.pull = None
    assert dio.pull is None, f"{pin} .pull should be None"

    dio.switch_to_input(pull=None)
    assert dio.direction == Direction.INPUT, f"{pin} .direction should be INPUT"
    assert dio.pull is None, f"{pin} .pull should be None after switch_to_input()"

    dio.switch_to_input(pull=Pull.UP)
    assert dio.direction == Direction.INPUT, f"{pin} .direction should be INPUT after switch_to_input"
    assert dio.pull == Pull.UP, f"{pin} .pull should be UP"
    assert dio.value is True, f"{pin} .value should be True after setting .pull to UP"

    dio.switch_to_input(pull=Pull.DOWN)
    assert dio.direction == Direction.INPUT, f"{pin} .direction should be INPUT after switch_to_input()"
    assert dio.pull == Pull.DOWN, f"{pin} .pull should be DOWN"
    assert dio.value is False, f"{pin} .value should be False after setting .pull to DOWN"

    dio.switch_to_output()
    try:
        _ = dio.pull
        raise AssertionError(f"{pin} .pull should not work when OUTPUT")
    except AttributeError:
        pass

    dio.switch_to_output(value=False, drive_mode=DriveMode.PUSH_PULL)
    assert dio.direction == Direction.OUTPUT, f"{pin} .direction should be OUTPUT after switch_to_output()"
    assert dio.drive_mode == DriveMode.PUSH_PULL, f"{pin} .drive_mode should be PUSH_PULL"
    assert dio.value is False, f"{pin} .value should be False"

    dio.switch_to_output(value=False, drive_mode=DriveMode.OPEN_DRAIN)
    assert dio.direction == Direction.OUTPUT, f"{pin} .direction should be OUTPUT after switch_to_output()"
    assert dio.drive_mode == DriveMode.OPEN_DRAIN, f"{pin} .drive_mode should be OPEN_DRAIN"
    assert dio.value is False, f"{pin} .value should be False"

    dio.switch_to_output(value=False, drive_mode=DriveMode.PUSH_PULL)
    assert dio.direction == Direction.OUTPUT, f"{pin} .direction should be OUTPUT after switch_to_output()"
    assert dio.drive_mode == DriveMode.PUSH_PULL, f"{pin} .drive_mode should be PUSH_PULL"
    assert dio.value is False, f"{pin} .value should be False"

    dio.switch_to_output(value=False, drive_mode=DriveMode.OPEN_DRAIN)
    assert dio.direction == Direction.OUTPUT, f"{pin} .direction should be OUTPUT after switch_to_output()"
    assert dio.drive_mode == DriveMode.OPEN_DRAIN, f"{pin} .drive_mode should be OPEN_DRAIN"
    assert dio.value is False, f"{pin} .value should be False"

    dio.switch_to_output(value=True, drive_mode=DriveMode.PUSH_PULL)
    assert dio.direction == Direction.OUTPUT, f"{pin} .direction should be OUTPUT after switch_to_output()"
    assert dio.drive_mode == DriveMode.PUSH_PULL, f"{pin} .drive_mode should be PUSH_PULL"
    assert dio.value is True, f"{pin} .value should be True"

    dio.switch_to_output(value=True, drive_mode=DriveMode.OPEN_DRAIN)
    assert dio.direction == Direction.OUTPUT, f"{pin} .direction should be OUTPUT after switch_to_output()"
    assert dio.drive_mode == DriveMode.OPEN_DRAIN, f"{pin} .drive_mode should be OPEN_DRAIN"
    assert dio.value is True, f"{pin} .value should be True"

    dio.switch_to_input()
    assert dio.direction == Direction.INPUT, f"{pin} .direction should be INPUT after switch_to_input()"

    dio.deinit()
    try:
        _ = dio.value
        assert AssertionError(".value should not work after deinit()")
    except ValueError:
        pass


def test_pin_pair(pin1, pin2):
    dio1 = DigitalInOut(pin1)
    dio2 = DigitalInOut(pin2)

    # Test that pulls work.
    dio1.pull = Pull.UP
    assert dio2.value is True, "other pin should be high due to .pull UP"

    dio1.pull = Pull.DOWN
    assert dio2.value is False, "other pin should be low due to .pull DOW"

    dio1.pull = None

    dio1.switch_to_output(value=False, drive_mode=DriveMode.PUSH_PULL)

    assert dio2.value is False, f"{pin1} should be low"

    dio1.value = True
    assert dio2.value is True, f"{pin1} should be high"

    dio1.value = False
    dio1.drive_mode = DriveMode.OPEN_DRAIN
    assert dio2.value is False, f"{pin1} should be low"

    dio1.deinit()
    dio2.deinit()
