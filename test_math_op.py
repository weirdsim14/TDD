import pytest
from math_op import add

@pytest.fixture
def sample_input():
    return (1, 2)

def test_add(sample_input):
    assert add(sample_input[0], sample_input[1]) == 3
