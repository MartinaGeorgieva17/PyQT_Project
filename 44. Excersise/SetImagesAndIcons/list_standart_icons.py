import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window geometry
        self.setWindowTitle("PyQt6 Window Example")
        self.setGeometry(300, 300, 400, 300)

        # Create a grid layout
        layout = QGridLayout()

        # Create a button with an icon from the style
        button = QPushButton("Click Me", self)
        icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DialogOkButton)  # Add standard icon
        button.setIcon(icon)

        # Add button to layout
        layout.addWidget(button, 0, 0)  # Position at row 0, column 0

        # Set layout to the main window
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
    