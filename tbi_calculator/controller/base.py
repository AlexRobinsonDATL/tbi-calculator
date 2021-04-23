import abc

from ..model.base import Model
from ..view.base import View


class ControllerBase(metaclass=abc.ABCMeta):
    def __init__(self, view: View, model: Model):
        self.view = view
        self.model = model

    @abc.abstractmethod
    def start(self) -> None:
        pass

    @abc.abstractmethod
    def execute(self) -> None:
        pass
