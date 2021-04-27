from threading import Thread

from ..model.base import Model
from ..view.base import View
from .base import ControllerBase


class Controller(ControllerBase):
    def __init__(self, view: View, model: Model):
        super().__init__(view, model)

    def start(self) -> None:
        self.view.setup(self)
        self.view.start_main_loop()

    def execute(self) -> None:
        thread = Thread(target=self.second_thread)
        thread.start()

    def second_thread(self) -> None:
        try:
            self.normal_operation()
        except ValueError:
            self.view.status = "Error! Please check config.ini"

    def normal_operation(self) -> None:
        self.view.status = "Downloading Data..."
        self.model.fetch_data(
            metabase_email=self.view.email, metabase_password=self.view.password
        )

        self.view.status = "Filtering orders.."
        self.model.filter()

        self.view.status = "Calculating Totals..."
        self.view.new_sales = self.model.total_sales("New")
        self.view.retread_sales = self.model.total_sales("Retread")

        self.view.status = "Ready!"
