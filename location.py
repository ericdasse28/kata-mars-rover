"""This module implements utilities to help handle the location functions of the Mars Rover"""

from dataclasses import dataclass
from enum import Enum


@dataclass
class Point:
    x: float
    y: float


class CardinalPoint(Enum):
    N = "N"
    S = "S"
    E = "E"
    W = "W"
