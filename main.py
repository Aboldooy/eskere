from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui import Ui_MainWindow

class EditorWindow(QMainWindow) :
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def choose_note(self):
        pass

    def create_note(self):
        pass

    def delete_note(self):
        pass

    def save_note(self):
        pass

    def creat_tag(self):
        pass

    def delete_tag(self):
        pass
    
    def find_by_tag(self):
        pass

app = QApplication([])
window = EditorWindow()

window.show()
app.exec()