from enum import Enum


class OutageStatus(Enum):
    ON = 1
    OFF = -1
    FIRST_HALF_OFF = 0
