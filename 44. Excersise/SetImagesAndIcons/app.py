import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.text_edit = qtw.QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.setupMenuBar()
        self.setupToolbar()
        self.setupDockWidget()
        self.setupStatusBar()

    def setupMenuBar(self):
        menubar = self.menuBar()
     
        file_menu = menubar.addMenu('&File')
        edit_menu = menubar.addMenu('E&dit')
        help_menu = menubar.addMenu('&Help')

        # Add actions to File menu
        open_action = file_menu.addAction('Open')
        save_action = file_menu.addAction('Save')
        file_menu.addSeparator()
        quit_action = file_menu.addAction('Quit', self.close)

        # Add actions to Edit menu
        undo_action = edit_menu.addAction('Undo', self.text_edit.undo)

        # Create QAction manually for Redo
        redo_action = qtg.QAction('Redo', self)
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)

        # Add additional actions
        edit_menu.addAction('Set font', self.set_font)
        edit_menu.addAction('Settings', self.show_settings)

    def set_font(self):
        print('Set font')
   
    def show_settings(self):
        print('Show settings')

    def setupDockWidget(self):
        dock = qtw.QDockWidget('Replace', self)
        self.addDockWidget(qtc.Qt.DockWidgetArea.LeftDockWidgetArea, dock)

        # Add a QTextEdit or any widget inside the dock widget
        replace_widget = qtw.QTextEdit()
        dock.setWidget(replace_widget)

        # Set dock widget features using QDockWidgetFeature
        dock.setFeatures(qtw.QDockWidget.DockWidgetFeature.DockWidgetMovable |
                         qtw.QDockWidget.DockWidgetFeature.DockWidgetClosable)

    def setupStatusBar(self):
        self.status_bar = qtw.QStatusBar()
        self.setStatusBar(self.status_bar)

        self.status_bar.showMessage('Welcome to My Text Editor')

    def setupToolbar(self):
        toolbar = self.addToolBar('File')
        toolbar.setMovable(False)
        toolbar.setFloatable(False)

        toolbar.setAllowedAreas(qtc.Qt.ToolBarArea.TopToolBarArea | qtc.Qt.ToolBarArea.BottomToolBarArea)

        # Add Help action to the toolbar
        self.help_action = qtg.QAction(self.style().standardIcon(qtw.QStyle.StandardPixmap.SP_DialogHelpButton), 'Help', self)

        # Connect the action to show a message box
        self.help_action.triggered.connect(lambda _: qtw.QMessageBox.information(self, 'Not implemented', 'Sorry, no help yet!'))

        toolbar.addAction(self.help_action)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())