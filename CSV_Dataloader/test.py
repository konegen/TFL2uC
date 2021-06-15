import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import pandas as pd

class UICSVDataloaderWindow2(QWidget):
    def __init__(self):
        super(UICSVDataloaderWindow2, self).__init__()
        self.window_width, self.window_height = 800, 600
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle('CSV dataloader')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.Browse = QPushButton('Browse')
        self.Browse.setFixedWidth(150)
        self.Browse.setFixedHeight(30)
        self.Browse.clicked.connect(self.browseCSVData)

        self.Preview = QPushButton('Preview')
        self.Preview.setFixedWidth(150)
        self.Preview.setFixedHeight(30)
        self.Preview.clicked.connect(self.previewCSVData)

        self.Load_data = QPushButton('Load data')
        self.Load_data.setFixedWidth(150)
        self.Load_data.setFixedHeight(30)
        self.Load_data.clicked.connect(self.loadCSVData)

        sublayout = QHBoxLayout()
        sublayout.addWidget(self.Browse)
        sublayout.addWidget(self.Preview)
        sublayout.addWidget(self.Load_data)
        layout.addLayout(sublayout)

        self.NumRowCol = QLabel()
        self.NumRowCol.setFixedWidth(250)
        self.NumRowCol.setFixedHeight(60)
        layout.addWidget(self.NumRowCol)

        self.cb1 = QCheckBox('Tab stop', self)
        layout.addWidget(self.cb1)

        self.cb2 = QCheckBox('Semicolon', self)
        layout.addWidget(self.cb2)

        self.cb3 = QCheckBox('Comma', self)
        layout.addWidget(self.cb3)

        self.cb4 = QCheckBox('Space', self)
        layout.addWidget(self.cb4)

        self.cb5 = QCheckBox('other', self)

        self.other_delimiter = QLineEdit()
        self.other_delimiter.setFixedWidth(50)
        self.other_delimiter.setMaxLength(1)

        sublayout_other = QHBoxLayout()
        sublayout_other.addWidget(self.cb5)
        sublayout_other.addWidget(self.other_delimiter)
        sublayout_other.addStretch()
        layout.addLayout(sublayout_other)


        self.delimiter = None
        self.data_loader_path = None
        self.df = None


    def browseCSVData(self):

        self.data_loader_path = QFileDialog.getOpenFileName(
            self, "Select your data loader script", os.path.expanduser(os.getenv('USERPROFILE')), 'CSV(*.csv)'
        )[0]
        
        print(self.data_loader_path)

        

    def previewCSVData(self):
        
        try:
        
            if self.data_loader_path != None and ".csv" in self.data_loader_path:

                self.get_delimiter()

                if not self.delimiter:
                    self.df = pd.read_csv(self.data_loader_path, index_col=False)
                else:
                    self.df = pd.read_csv(self.data_loader_path, index_col=False, sep=self.delimiter)
                if self.df.size == 0:
                    return

                self.df.fillna('', inplace=True)
                self.table.setRowCount(self.df.shape[0])
                self.table.setColumnCount(self.df.shape[1])
                self.table.setHorizontalHeaderLabels(self.df.columns)

                # returns pandas array object
                for row in self.df.iterrows():
                    values = row[1]
                    for col_index, value in enumerate(values):
                        # if isinstance(value, (float, int)):
                            # value = '{0:0,}'.format(value)
                        tableItem = QTableWidgetItem(str(value))
                        self.table.setItem(row[0], col_index, tableItem)

                self.table.setColumnWidth(2, 300)

                self.NumRowCol.setText("Number of Trainingsamples: " + str(self.df.shape[0]) + "\nNumber of Features: " + str(self.df.shape[1]))
            
            else:
                print("File is no CSV")
        
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("This separator cannot be used")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            


    def loadCSVData(self):
        return self.df


    def get_delimiter(self):

        self.delimiter = None

        if self.cb1.isChecked():
            if self.delimiter == None:
                self.delimiter = r'\t'
            else:
                self.delimiter += r'|\t'
        if self.cb2.isChecked():
            if self.delimiter == None:
                self.delimiter = ';'
            else:
                self.delimiter += '|;'
        if self.cb3.isChecked():
            if self.delimiter == None:
                self.delimiter = ','
            else:
                self.delimiter += '|,'
        if self.cb4.isChecked():
            if self.delimiter == None:
                self.delimiter = r'\s+'
            else:
                self.delimiter += r'|\s+'
        if self.cb5.isChecked():
            if self.delimiter == None:
                self.delimiter = self.other_delimiter.text()
            else:
                self.delimiter += '|' + self.other_delimiter.text()
            
        print(self.delimiter)

        


app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        font-size: 17px;
    }
''')

myApp = UICSVDataloaderWindow2()
myApp.show()

sys.exit(app.exec())