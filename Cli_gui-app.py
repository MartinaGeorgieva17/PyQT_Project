import sys

#Import needed QtWidgets classes
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

#THE MAIN APP INSTANCE FOR OUR application 

app = QApplication([])

#cREATE qT WIDGET, WHICH WILL BE OUR MAIN  WINDOW
window = QWidget()
window.setWindowTitle('Hello World')

btnOk = QPushButton(window)
btnOk.setText('Ok')

print(window.height())


#Show the window 
window.show()

# #Start the event log 
# res = app.exec()
sys.exit(app.exec())

print('END')
# print(f'res={res}')


