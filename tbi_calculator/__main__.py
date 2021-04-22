from .controller import Controller
from .view import TkView

app = Controller(view=TkView(), model=None)
app.start()
