from math_op import add, subtract, wrong_user_display

import pytest


@pytest.fixture
def sample_input():
    return (1, 2)


def test_add(sample_input):
    assert add(sample_input[0], sample_input[1]) == 3


def test_subtract():
    assert subtract(5, 3) == 2


# Test with zero
def test_add_with_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5


def test_subtract_with_zero():
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5


# Test with negative numbers
def test_add_with_negatives():
    assert add(-1, -2) == -3


def test_subtract_with_negatives():
    assert subtract(-1, -2) == 1


def test_wrong_user_display():
    assert wrong_user_display() == "John (30)"
