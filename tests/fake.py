from tbi_calculator.controller.base import ControllerBase
from tbi_calculator.model.base import Model
from tbi_calculator.view.base import View


class FakeController(ControllerBase):
    def __init__(self, view=None, model=None):
        if view is None:
            view = FakeView()
        if model is None:
            model = FakeModel()

        super().__init__(view, model)

    def start(self) -> None:
        pass

    def execute(self) -> None:
        self.view.status = "Fake Status"


class FakeModel(Model):
    def __init__(self):
        self.data = []

    def fetch_data(self, *args, **kwargs):
        self.data = [1, 2, 3]

    def total_sales(self, tyre_type: str) -> float:
        return 5

    def filter(self) -> None:
        self.is_filtered = True


class FakeView(View):
    def __init__(self):
        self.status = ""
        self.new_sales = ""
        self.retread_sales = ""
        self._password = "my password"
        self._email = "test.email@testing.com"

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password

    def setup(self, *args, **kwargs):
        self.is_setup = True

    def start_main_loop(self):
        self.is_looping = True
