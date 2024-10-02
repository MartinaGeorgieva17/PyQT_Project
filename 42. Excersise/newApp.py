import sys
from PyQt6 import QtWidgets as qtw 
from PyQt6 import QtCore as qtc 
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super(). __init__ (*args, **kwargs)
        self.btnOK= qtw .QPushButton("OK", parent=self)


if __name__ == "__main__":
    app=qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
