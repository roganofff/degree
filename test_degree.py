"""A module for testing main degree function."""

import pytest

from degree import degree

test_data = [
    (1, 10, 2, 5, 314.37),
    (2, 1, 5, 7, 272.15),
    (1, 0, 0, 0, 0),
    (1, 1, 1, 1, 85.94),
    (10.01, 6.9, 2.4, 6.3, 215.83),
]


@pytest.mark.parametrize('radius, time, acceleration, velocity, expected', test_data)
def test_degree(radius: float, time: float, acceleration: float, velocity: float, expected: float):
    """Test detective function with test_data.

    Args:
        radius: float - radius of the ball.
        time: float - the time in which the ball moves.
        acceleration: float - acceleration of the ball.
        velocity: float - the speed at which the ball moves.
        expected: an actual expected angle.

    Asserts:
        True if the function returns expected answers.
    """
    assert degree(radius, time, acceleration, velocity) == expected
