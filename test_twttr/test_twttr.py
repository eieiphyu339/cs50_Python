# from twttr import shorten
import sys
sys.path.append("../twttr")
import twttr

def test_shorten_lowercase():
    assert twttr.shorten("hello") == "hll"
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("aeiou") == ""

def test_shorten_uppercase():
    assert twttr.shorten("HELLO") == "HLL"
    assert twttr.shorten("TWITTER") == "TWTTR"
    assert twttr.shorten("AEIOU") == ""

def test_shorten_mixed_case():
    assert twttr.shorten("Hello World") == "Hll Wrld"
    assert twttr.shorten("TwItTeR") == "TwtTR"

def test_shorten_with_numbers_and_symbols():
    assert twttr.shorten("123abc") == "123bc"
    assert twttr.shorten("!@#AEIOU") == "!@#"

def test_shorten_empty_string():
    assert twttr.shorten("") == ""
