# # 1. Example 1......................

# import sys

# from PyQt6 import QtWidgets as qtw
# from PyQt6 import QtCore as qtc 
# from PyQt6 import QtGui as qtg

# class MainWindow(qtw.QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.setWindowTitle('Primary')
#         self.setFixedSize(600, 400)

#         self.child = qtw.QWidget(parent=self)
#         self.child.setWindowTitle('Child')
#         self.child.setFixedSize(300, 100)
#         self.child.show()
#         print('Child was created')

# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)

# window = MainWindow()
# # print('Back in main')

# window.show()
# sys.exit(app.exec())



# 2. Example 2..Contructor Example ........................

# class A: 
#     def __init__(self):
#         self.age = 34
#         print('Constructor is called!')
#         self.greet("Pesho")

#     def greet(self, name): 
#         print(f'Hello {name}')

# a = A()
# a.greet('Ada')



