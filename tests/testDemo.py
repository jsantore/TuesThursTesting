import pytest

import main

def test_add():
    result = main.add_it_up(5, 6)
    assert result == 11

def test_distance():
    result = main.find_distance((0, 3), (4, 0))
    assert result == 5
    result2 = main.find_distance((0, 0), (6, 5))
    assert result2 == pytest.approx(7.81024967590, 0.0000000001)
    result3 = main.find_distance((-3, -5), (-3, -5))
    assert result3 == 0

def test_bad_data():

    result = main.find_distance((2, 4, 6,), (3, 5, 7))

