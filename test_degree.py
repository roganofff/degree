"""A module for testing main degree function."""

import pytest

from degree import degree

test_data = [
    (1, 10, 2, 5, 314.37),
    (2, 1, 5, 7, 272.15),
    (1, 0, 0, 0, 0.0),
    (1, 1, 1, 1, 85.94),
    (10.01, 6.9, 2.4, 6.3, 215.83),
]

@pytest.mark.parametrize('radius, time, acceleration, velocity, expected', test_data)
def test_degree(radius: float, time: float, acceleration: float, velocity: float, expected: float):
    assert degree(radius, time, acceleration, velocity) == expected