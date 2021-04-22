from threading import Thread
from time import sleep

from ..view import View
from .base import ControllerBase


class Controller(ControllerBase):
    def __init__(self, view: View, model=None):
        self.view = view

    def start(self) -> None:
        self.view.setup(self)
        self.view.start_main_loop()

    def execute(self) -> None:
        thread = Thread(target=self.logic_thread)
        thread.start()

    def logic_thread(self) -> None:
        self.view.status = "Running!"
        email = self.view.email
        password = self.view.password
        api_key = self.view.api_key

        sleep(5)
        print(email, password, api_key)
        self.view.status = "Ready!"
