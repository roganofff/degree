"""A module for testing main degree function."""
from typing import Tuple

import pytest

from degree import degree

test_data = [
    ((1, 10, 2, 5), 314.37),
    ((2, 1, 5, 7), 272.15),
    ((1, 0, 0, 0), 0),
    ((1, 1, 1, 1), 85.94),
    ((10.01, 6.9, 2.4, 6.3), 215.83),
    ((6.1, 47.92, 9.89, 20.02), 108.84),
    ((9.11, 9.99, 7.77, 8.88), 116.45),
    ((7.16, 42.74, 9.29, 7.22), 168.5),
    ((16.52, 4.52, 21.91, 12.71), 255.5),
    ((2.6, 28.67, 10.97, 5.25), 70.0),
    ((73.12, 5.2, 0.5, 1.07), 9.66),
    ((29.34, 51.34, 8.48), 224.29),
    ((18.22, 29.31, 14.84), 245.17),
    ((19.51, 48.31, 7.22), 262.67),
    ((11.03, 38.98, 21.15), 306.3),
    ((7.23, 11.71, 22.17), 165.75),
    ((12.86, 45.81, 2.72), 115.73),
    ((1526.32, 2155.52, 1.33), 65.26),
    ((634.11, 2.01, 1756.81), 320.66),
    ((15.32, 38.16, 10.12), 196.95),
    ((14.29, 41.44, 11.52), 59.97),
]


@pytest.mark.parametrize('inputs, expected', test_data)
def test_degree(inputs: Tuple[float], expected: float):
    """Test detective function with test_data.

    Args:
        inputs: tuple with values that are inserted
        expected: an actual expected angle.

    Asserts:
        True if the function returns expected answers.
    """
    assert degree(*inputs) == expected


@pytest.mark.xfail(raises=Exception)
def test_exc():
    """This is exception test."""
    assert degree(0, 0, 0, 0)
