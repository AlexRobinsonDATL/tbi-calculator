from .base import ControllerBase


class Controller(ControllerBase):
    def start(self):
        raise NotImplementedError
