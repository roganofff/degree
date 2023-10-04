""""Module for calculating the rotation of the ball in degrees."""

from math import pi


def degree(radius: float, time: float, acceleration: float, velocity: float = 0) -> float:
    """Calculate degree of rotation of the ball from the starting position.

    Args:
        radius: float - radius of the ball.
        time: float - the time in which the ball moves .
        acceleration: float - accelerating the ball.
        velocity: float - the speed at which the ball moves.

    Returns:
        float - degree of rotation of the ball.
    """
    distance = velocity * time + (acceleration * time ** 2) / 2
    length = 2 * pi * radius
    new_degree = ((distance % length) / length) * 360
    return round(new_degree, 2)
