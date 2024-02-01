from my_calculator import my_adder

def test_positive_with_positive():
    assert my_adder(1, 2) == 3

def test_negative_with_positive():
    assert my_adder(-1, 2) == 1