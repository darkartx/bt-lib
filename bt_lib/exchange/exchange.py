"""
Bt lib exchange abstraction
"""
import abc

from .models import Klines, Symbol, Interval

__all__ = ('BaseExchange',)


class BaseExchange(abc.ABC):
    """
    Base excahnge definition
    """

    @abc.abstractmethod
    async def klines(self,
                     symbol: Symbol,
                     interval: Interval,
                     start_time: int,
                     end_time: int,
                     limit: int = None) -> Klines:
        """
        Get list of kline
        """
