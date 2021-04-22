import abc


class ControllerBase(metaclass=abc.ABCMeta):
    password: str

    @abc.abstractmethod
    def start(self) -> None:
        pass
