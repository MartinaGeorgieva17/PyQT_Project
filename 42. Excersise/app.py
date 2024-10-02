import sys
from PyQt6 import QtWidgets as qtw
from Ui_LoginForm import Ui_Form
from Ui_Buttons import UiButtons


class MainWindow(qtw.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.label.setText('Changed @@@@@@@@@@@@')

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())