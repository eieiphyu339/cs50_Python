from um import count

def test_no_um():
    assert count("This is a yummy dessert.") == 0
    assert count("Hmm, what should I say?") == 0

def test_count_um():
    assert count("Um, what do you mean?") == 1
    assert count("Hello, um, world!") == 1
    assert count("Um, um, I don't konw, um.") == 3
    assert count("UM um uM Um.") == 4

def test_um_in_word():
    assert count("The plumber is here.") == 0
    assert count("Yummy food.") == 0

def test_empty_input():
    assert count("") == 0
    assert count("     ") == 0
