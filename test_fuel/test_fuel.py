import sys
sys.path.append("../fuel")
import fuel

def test():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/2") == 50
    assert fuel.convert("1/1") == 100
    assert fuel.convert("0/4") == 0

    try:
        assert fuel.convert("cat/dog")
    except ValueError:
        pass

    try:
        assert fuel.convert("3/0")
    except ZeroDivisionError:
        pass

    assert fuel.gauge(100) == "F"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(75) == "75%"
