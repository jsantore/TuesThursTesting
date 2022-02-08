import main

def test_add():
    result = main.add_it_up(5, 6)
    assert result == 11

def test_distance():
    result = main.find_distance((0, 3), (4, 0))
    assert result == 5
