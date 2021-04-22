import tkinter as tk

from .controller.base import ControllerBase


class TkView:
    def setup(self, controller: ControllerBase):
        self._setup_tkinter()
        self._create_gui(controller)
        self.status: str = ""

    def _setup_tkinter(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("TBI Calc")

    def _create_gui(self, controller: ControllerBase) -> None:
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.label = tk.Label(self.frame, text="Result")
        self.label.pack()

    def start_main_loop(self) -> None:
        self.root.mainloop()
