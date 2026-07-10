import pytest
from pnp import fibonacci

@pytest.mark.parametrize(
    "n, result",
    [
        (1, [1]),
        (2, [1, 1]),
        (3, [1, 1, 2]),
        (4, [1, 1, 2, 3]),
        (5, [1, 1, 2, 3, 5])
    ])
def test_fibonacci(n, result):
    assert list(fibonacci(n)) == result
        

def test_fibonacci_broken():
    with pytest.raises(ValueError):
        list(fibonacci(0))
