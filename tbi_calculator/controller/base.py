import abc


class ControllerBase(metaclass=abc.ABCMeta):
    def __init__(self, view, model):
        self.view = view
        self.model = model

    @abc.abstractmethod
    def start(self) -> None:
        pass

    @abc.abstractmethod
    def execute(self) -> None:
        pass
