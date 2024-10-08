import sys

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg



class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = qtw.QLabel('Main Title')
        self.line_edit = qtw.QLineEdit()
        self.button1 = qtw.QPushButton('Button1')
        self.button2 = qtw.QPushButton('Button2')
        self.button2.setObjectName('btn1')
        
        self.main_layout = qtw.QVBoxLayout()
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        self.main_layout.addWidget(self.button1)
        self.main_layout.addWidget(self.button2)
        self.setLayout(self.main_layout)

        self.apply_style()
    
    def apply_style(self):
        with open(r"F:\Python_2024\Projects\PyQT_Project\44. Excersise\SetImagesAndIcons\main.css") as fh:
            sheet = fh.read()

        self.setStyleSheet(sheet)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())