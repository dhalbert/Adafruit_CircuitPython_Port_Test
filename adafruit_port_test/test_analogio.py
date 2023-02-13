# SPDX-FileCopyrightText: Copyright (c) 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
Test analog.AnalogIn and AnalogOut functionality.
"""

from analogio import AnalogIn, AnalogOut
from microcontroller import Pin


def test_analogin_pin(pin: Pin):
    """Test ADC."""

    # Test context manager deinit
    with AnalogIn(pin) as ain:
        try:
            print(f"{ain.reference_voltage=}")
            _ = ain.value
        except Exception:
            # pylint: disable=raise-missing-from
            raise AssertionError("context manager for AnalogIn did not work")
    try:
        _ = ain.value
        raise AssertionError("context manager did not deinit()")
    except ValueError:
        pass


def test_analogout_pin(pin: Pin):
    """Test DAC."""

    # Test context manager deinit
    with AnalogOut(pin) as aout:
        try:
            aout.value = 0
        except Exception:
            # pylint: disable=raise-missing-from
            raise AssertionError("context manager for AnalogOut did not work")
    try:
        aout.value = 0
        raise AssertionError("context manager did not deinit()")
    except ValueError:
        pass


def test_analogin_value(ain: AnalogIn):
    """Test AnalogIn."""
    value = ain.value
    print(f".value: {ain.value=}, voltage={value * ain.reference_voltage}")
    return value
