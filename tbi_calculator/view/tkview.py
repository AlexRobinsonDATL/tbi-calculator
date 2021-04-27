"""View using tkinter"""

import tkinter as tk
from pathlib import Path
from tkinter import ttk

from ..controller.base import ControllerBase
from .base import View

THEME = "azure"
assets_path = Path("assets")
theme_path = assets_path / f"{THEME}.tcl"
icon_path = assets_path / "invoice.png"


class TkView(View):
    def __init__(self):
        self._setup_tkinter()
        self._status = tk.Variable(self.root)
        self._new_sales = tk.Variable(self.root)
        self._retread_sales = tk.Variable(self.root)
        self._password = tk.StringVar(self.root)
        self._email = tk.StringVar(self.root)

        self.status = "Ready!"

    def setup(self, controller: ControllerBase):
        self._create_gui(controller)

    def _setup_tkinter(self) -> None:
        self.root = tk.Tk()
        self.style = ttk.Style(self.root)
        self.root.tk.call("source", str(theme_path))
        self.style.theme_use(THEME)
        self.root.geometry("400x200")
        self.root.title("TBI Calculator")
        icon = tk.PhotoImage(file=icon_path)
        self.root.iconphoto(False, icon)

    def _create_gui(self, controller) -> None:
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.email_label = ttk.Label(self.frame, text="Email", anchor="e")
        self.email_label.place(x=40, y=40)

        self.email_box = ttk.Entry(self.frame, textvariable=self._email)
        self.email_box.place(x=80, y=35, width=275)

        self.password_label = ttk.Label(self.frame, text="Password", anchor="e")
        self.password_label.place(x=20, y=80)
        self.password_box = ttk.Entry(self.frame, textvariable=self._password, show="*")
        self.password_box.place(x=80, y=75, width=275)

        self.status_label = ttk.Label(self.frame, textvariable=self._status)
        self.status_label.pack(side=tk.TOP)

        self.new_sales_label = ttk.Label(self.frame, text="New TBI (£)")
        self.new_sales_label.place(x=20, y=120)
        self.new_sales_box = ttk.Entry(self.frame, textvariable=self._new_sales)
        self.new_sales_box.place(x=90, y=115, width=80)

        self.retread_sales_label = ttk.Label(self.frame, text="Retread TBI (£)")
        self.retread_sales_label.place(x=180, y=120)
        self.retread_sales_box = ttk.Entry(self.frame, textvariable=self._retread_sales)
        self.retread_sales_box.place(x=260, y=115, width=80)

        self.go_button = ttk.Button(self.frame, text="Go!", command=controller.execute)
        self.go_button.pack(side=tk.BOTTOM)

    def start_main_loop(self) -> None:
        self.root.mainloop()

    @property
    def email(self) -> str:
        return self._email.get()

    @property
    def password(self) -> str:
        return self._password.get()

    @property  # type: ignore
    def status(self) -> str:  # type: ignore
        return self._status.get()

    @status.setter
    def status(self, value: str) -> None:
        self._status.set(value)

    @property  # type: ignore
    def new_sales(self) -> float:  # type: ignore
        return self._new_sales.get()

    @new_sales.setter
    def new_sales(self, value: float) -> None:
        rounded_value = round(value, 2)
        self._new_sales.set(rounded_value)

    @property  # type: ignore
    def retread_sales(self) -> float:  # type: ignore
        return self._retread_sales.get()

    @retread_sales.setter
    def retread_sales(self, value: float) -> None:
        rounded_value = round(value, 2)
        self._retread_sales.set(rounded_value)
