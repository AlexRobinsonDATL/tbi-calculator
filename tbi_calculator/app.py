from tbi_calculator.controller import Controller
from tbi_calculator.model import SSMetabaseModel
from tbi_calculator.view import TkView

app = Controller(view=TkView(), model=SSMetabaseModel())
app.start()
