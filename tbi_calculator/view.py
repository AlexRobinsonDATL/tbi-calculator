import abc
import tkinter as tk

from .controller.base import ControllerBase


class View(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def password(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def email(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def api_key(self) -> str:
        pass

    @abc.abstractmethod
    def setup(self, controller: ControllerBase) -> None:
        pass

    @abc.abstractmethod
    def start_main_loop(self) -> None:
        pass

    @property
    @abc.abstractmethod
    def status(self) -> str:
        pass


class TkView(View):
    def __init__(self):
        self._setup_tkinter()
        self._status = tk.Variable(self.root)
        self._api_key = tk.StringVar(self.root)
        self._password = tk.StringVar(self.root)
        self._email = tk.StringVar(self.root)

        self.status = "Ready!"

    def setup(self, controller: ControllerBase):
        self._create_gui(controller)

    def _setup_tkinter(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("400x200")
        self.root.title("TBI Calc")

    def _create_gui(self, controller) -> None:
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.email_label = tk.Label(self.frame, text="Email", anchor="e")
        self.email_label.place(x=40, y=40)

        self.email_box = tk.Entry(self.frame, textvariable=self._email)
        self.email_box.place(x=80, y=40, width=275)

        self.password_label = tk.Label(self.frame, text="Password", anchor="e")
        self.password_label.place(x=20, y=80)
        self.password_box = tk.Entry(self.frame, textvariable=self._password, show="*")
        self.password_box.place(x=80, y=80, width=275)

        self.api_key_label = tk.Label(self.frame, text="API Key", anchor="e")
        self.api_key_label.place(x=20, y=120)
        self.api_key_box = tk.Entry(self.frame, textvariable=self._api_key)
        self.api_key_box.place(x=80, y=120, width=275)

        self.status_label = tk.Label(self.frame, textvariable=self._status)
        self.status_label.pack(side=tk.TOP)

        self.go_button = tk.Button(self.frame, text="Go!", command=controller.execute)
        self.go_button.pack(side=tk.BOTTOM)

    def start_main_loop(self) -> None:
        self.root.mainloop()

    @property
    def email(self) -> str:
        return self._email.get()

    @property
    def password(self) -> str:
        return self._password.get()

    @property
    def api_key(self) -> str:
        return self._api_key.get()

    @property
    def status(self) -> str:
        return self._status.get()

    @status.setter
    def status(self, value: str) -> None:
        self._status.set(value)
