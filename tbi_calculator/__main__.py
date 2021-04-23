from .controller import Controller
from .model import SSMetabaseModel
from .view import TkView

app = Controller(view=TkView(), model=SSMetabaseModel())
app.start()
