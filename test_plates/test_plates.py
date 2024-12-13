import sys
sys.path.append("../plates")
import plates

def test_length():
    assert plates.is_valid("A") == 0
    assert plates.is_valid("ABCDEFG") == 0

    assert plates.is_valid("AB") == 1
    assert plates.is_valid("ABC123") == 1

def test_start_with_letters():
    assert plates.is_valid("1ABC") == 0
    assert plates.is_valid("A1BC") == 0

    assert plates.is_valid("AB123") == 1

def test_alphanumeric():
    assert plates.is_valid("ABC@123") == 0
    assert plates.is_valid("AB C") == 0
    assert plates.is_valid("12345") == 0

    assert plates.is_valid("ABC123") == 1
    assert plates.is_valid("XYZ") == 1

def test_number_placement():
    assert plates.is_valid("AB12C3") == 0

    assert plates.is_valid("AB123") == 1
    assert plates.is_valid("ABC") == 1

def test_no_leading_zero():
    assert plates.is_valid("ABC012") == 0
    assert plates.is_valid("ABC0") == 0

    assert plates.is_valid("ABC1") == 1
    assert plates.is_valid("ABC123") == 1

def test_valid_cases():
    assert plates.is_valid("CS50") == 1
    assert plates.is_valid("AB1234") == 1
    assert plates.is_valid("AA100") == 1
    assert plates.is_valid("ZXC2") == 1

def test_invalid_cases():
    assert plates.is_valid("") == 0
    assert plates.is_valid("123456") == 0
    assert plates.is_valid("1234AB") == 0
    assert plates.is_valid("A123456") == 0
    assert plates.is_valid("ABC@123") == 0
