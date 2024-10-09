import sys

from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.showTable()
        self.applyStyle()

    def showTable(self):
        data=[
            [1,2,3],
            [4,5,6]
        ]

        row_count =len(data)
        column_count= len(data[0])
        
        table = qtw.QTableWidget(self)
        table.setColumnCount(column_count)
        table.setRowCount(row_count)
        table.setHorizontalHeaderLabels(['Column1', 'Column2', "Column3"])
        table.setFixedSize(400,200)
        # table.resizeColumnsToContents() промяна на размер на редове 
        # table.resizeRowsToContents() промяна на размер на колони

        table.setContextMenuPolicy(qtc.Qt.ContextMenuPolicy.CustomContextMenu)
        table.customContextMenuRequested.connect(self.context_actions)
        table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.ResizeMode.Stretch)


        for row_idx, row in enumerate(data):
            for col_idx, el in enumerate(row):
                table.setItem(row_idx, col_idx, qtw.QTableWidgetItem(str(el)))

        self.table=table

        layout = qtw.QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
    
    def context_actions(self,position):
        menu = qtw.QMenu()

        current_row = self.table.currentRow()
        menu.addAction("Add row", lambda: self.table.insertRow(current_row if current_row >=0 else self.table.rowCount()))
        
        menu.exec(self.table.viewport().mapToGlobal(position))

    def applyStyle(self):
        try:
            with open("PyQT_Project\\45. Excersise\\main.css", "r") as f:
                style_sheet = f.read()
                self.setStyleSheet(style_sheet)
        except Exception as e:
            print(f"Неуспешно зареждане на стиловете: {e}")
     
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())