from seasons import calculate_age_in_minutes, convert_to_words
from datetime import date
import pytest

def test_calculate_age_in_minutes():
    birth_date = date(2000, 1, 1)
    today = date(2024, 12, 4)
    assert calculate_age_in_minutes(birth_date,today)

def test_convert_to_words():
    assert convert_to_words(12450654)

def test_leap_year():
    birth_date = date(2019,1,1)
    today = date(2024, 12, 4)
    assert calculate_age_in_minutes(birth_date,today)
