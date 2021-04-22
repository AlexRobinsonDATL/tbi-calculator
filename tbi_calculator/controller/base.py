import abc


class ControllerBase(metaclass=abc.ABCMeta):
    password: str

    @abc.abstractmethod
    def start(self) -> None:
        pass

    @abc.abstractmethod
    def execute(self) -> None:
        pass
