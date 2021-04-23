"""Defines Model interface"""

import abc


class Model(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch_data(self, *args, **kwargs) -> None:
        pass

    @abc.abstractmethod
    def total_sales(self, tyre_type: str) -> float:
        pass

    @abc.abstractmethod
    def filter(self) -> None:
        pass
