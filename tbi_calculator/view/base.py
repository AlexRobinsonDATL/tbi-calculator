"""Base class for views. Defines the interface that other modules will rely on."""

import abc
from typing import Optional

from ..controller.base import ControllerBase


class View(metaclass=abc.ABCMeta):
    """Base class for views."""

    status: str
    new_sales: Optional[float]
    retread_sales: Optional[float]

    @property
    @abc.abstractmethod
    def password(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def email(self) -> str:
        pass

    @abc.abstractmethod
    def setup(self, controller: ControllerBase) -> None:
        pass

    @abc.abstractmethod
    def start_main_loop(self) -> None:
        pass
