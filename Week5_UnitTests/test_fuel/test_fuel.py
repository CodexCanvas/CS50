"""  implement two or more functions that collectively test your implementations
of convert and gauge thoroughly, each of whose names should begin with
test_ so that you can execute your tests with:
pytest test_fuel.py
Take care to return, not print, an int in convert and a str in gauge.
Only main should call print.
Note that you can raise an exception like ValueError with code like:
raise ValueError """
# test_fuel.py

import pytest
import fuel_corrected as fuel
from fuel_corrected import convert, gauge

# Table-Driven Test Cases for `convert`
@pytest.mark.parametrize("input_value, expected_output", [
    ("1/2", 50),  # Valid fraction
    ("3/4", 75),  # Valid fraction
    ("1/4", 25),  # Valid fraction
    ("0/1", 0),   # Edge case: numerator is 0
    ("1/1", 100), # Edge case: numerator equals denominator
])
def test_convert_valid(input_value, expected_output):
    assert convert(input_value) == expected_output

@pytest.mark.parametrize("input_value", [
    "2/1",  # Invalid fraction: numerator > denominator
    "1/0",  # Invalid fraction: denominator is 0
    "a/b",  # Invalid format: non-numeric values
    "1.5/2", # Invalid format: decimal values
])
def test_convert_invalid(input_value):
    with pytest.raises(ValueError):
        convert(input_value)

# Table-Driven Test Cases for `gauge`
@pytest.mark.parametrize("input_value, expected_output", [
    (0, "E"),    # Edge case: empty tank
    (1, "E"),    # Near empty tank
    (50, "50%"), # Mid-range value
    (99, "F"),   # Near full tank
    (100, "F"),  # Edge case: full tank
])
def test_gauge(input_value, expected_output):
    assert gauge(input_value) == expected_output