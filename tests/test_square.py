from main import square

def test_square_2():
    assert square(2) == 4

def test_square_5():
    assert square(5) == 25

def test_negative():
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
