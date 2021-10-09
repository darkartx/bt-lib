"""
Bt exchange models
"""

from collections import namedtuple
from enum import Enum

__all__ = ('Kline', 'Klines', 'Symbol', 'IntervalType', 'Interval')


Kline = namedtuple(
    'Kline', (
        'open_time',
        'close_time',
        'open',
        'high',
        'low',
        'close',
        'volume'
        )
)


Klines = list[Kline]


Symbol = namedtuple(
    'Symbol', ('base', 'asset')
)


class IntervalType(Enum):
    """
    Interval type
    """
    MINUTE = 1
    HOUR = 2
    DAY = 3
    WEEK = 4
    MONTH = 5

Interval = namedtuple(
    'Interval', ('interval', 'value')
)
