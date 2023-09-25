import pytest
from math_op import add, divide, multiply

@pytest.fixture
def sample_input():
    return (1, 2)

def test_add(sample_input):
    assert add(sample_input[0], sample_input[1]) == 3

@pytest.fixture
def sample_divide_input():
    return (4, 2)

def test_divide(sample_divide_input):
    assert divide(sample_divide_input[0], sample_divide_input[1]) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)

@pytest.fixture
def sample_multiply_input():
    return (3, 4)

def test_multiply(sample_multiply_input):
    assert multiply(sample_multiply_input[0], sample_multiply_input[1]) == 12
