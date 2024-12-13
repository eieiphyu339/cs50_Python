import sys
sys.path.append("../bank")
import bank

def test_value_hello():
    assert bank.value("hello") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("HELLO there") == 0

def test_value_h():
    assert bank.value("hi") == 20
    assert bank.value("hey there") == 20
    assert bank.value("HOLA") == 20

def test_value_other():
    assert bank.value("good morning") == 100
    assert bank.value("what's up?") == 100
    assert bank.value("") == 100

