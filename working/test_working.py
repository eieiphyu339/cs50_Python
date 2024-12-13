import pytest
from working import convert

def test_valid_conversion():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_overnight_conversion():
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:65 PM to 5:00 AM")

def test_missing():
    with pytest.raises(ValueError):
        convert("12 PM 5:30 PM")
