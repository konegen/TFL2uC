import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import pandas as pd

class UICSVDataloaderWindow(QWidget):
    """Get a preview and load CSV data. 

    This GUI window shows the data format of CSV files, selected
    from the dataloader retrain the model. You can also choose
    how to separate the different columns.
    """
    def __init__(self, FONT_STYLE, parent=None):
        super(UICSVDataloaderWindow, self).__init__(parent)#, Qt.WindowStaysOnTopHint)

        self.setWindowModality(Qt.ApplicationModal)
        
        self.FONT_STYLE = FONT_STYLE 

        self.window_width, self.window_height = 700, 400
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle('CSV dataloader')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.Browse = QPushButton('Browse')
        self.Browse.setFixedWidth(150)
        self.Browse.setFixedHeight(30)
        self.Browse.setStyleSheet("""QPushButton {
                           font: 12pt """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 

        self.Preview = QPushButton('Preview')
        self.Preview.setFixedWidth(150)
        self.Preview.setFixedHeight(30)
        self.Preview.setStyleSheet("""QPushButton {
                           font: 12pt """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 

        self.Load_data = QPushButton('Load data')
        self.Load_data.setFixedWidth(150)
        self.Load_data.setFixedHeight(30)
        self.Load_data.setStyleSheet("""QPushButton {
                           font: 12pt """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 

        sublayout = QHBoxLayout()
        sublayout.addWidget(self.Browse)
        sublayout.addWidget(self.Preview)
        sublayout.addWidget(self.Load_data)
        layout.addLayout(sublayout)

        self.separator = QLabel("Separator:")
        self.separator.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.separator.setFixedWidth(200)
        layout.addWidget(self.separator)

        self.cbTab = QCheckBox('Tab stop', self)
        self.cbTab.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbTab.setFixedWidth(150)
        layout.addWidget(self.cbTab)
        
        self.target_col = QComboBox()
        self.target_col.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.target_col.setFixedWidth(200)
        self.target_col.setVisible(False)

        self.cbSemicolon = QCheckBox('Semicolon', self)
        self.cbSemicolon.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbSemicolon.setFixedWidth(150)
        # layout.addWidget(self.cbSemicolon)

        sublayout2 = QHBoxLayout()
        sublayout2.addWidget(self.cbSemicolon)
        sublayout2.addStretch()
        sublayout2.addWidget(self.target_col)
        sublayout2.addStretch()
        sublayout2.addStretch()
        layout.addLayout(sublayout2)

        self.numRow = QLabel()
        self.numRow.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.numRow.setFixedWidth(200)

        self.cbComma = QCheckBox('Comma', self)
        self.cbComma.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbComma.setFixedWidth(150)
        # layout.addWidget(self.cbComma)

        sublayout3 = QHBoxLayout()
        sublayout3.addWidget(self.cbComma)
        sublayout3.addStretch()
        sublayout3.addWidget(self.numRow)
        sublayout3.addStretch()
        sublayout3.addStretch()
        layout.addLayout(sublayout3)

        self.numCol = QLabel()
        self.numCol.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.numCol.setFixedWidth(200)

        self.cbSpace = QCheckBox('Space', self)
        self.cbSpace.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbSpace.setFixedWidth(150)
        # layout.addWidget(self.cbSpace)

        sublayout4 = QHBoxLayout()
        sublayout4.addWidget(self.cbSpace)
        sublayout4.addStretch()
        sublayout4.addWidget(self.numCol)
        sublayout4.addStretch()
        sublayout4.addStretch()
        layout.addLayout(sublayout4)

        self.cbOther = QCheckBox('other', self)
        self.cbOther.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbOther.setFixedWidth(65)

        self.other_seperator = QLineEdit()
        self.other_seperator.setFixedWidth(30)
        self.other_seperator.setMaxLength(1)
        self.other_seperator.setStyleSheet("font: 11pt " + FONT_STYLE)

        sublayout5 = QHBoxLayout()
        sublayout5.addWidget(self.cbOther)
        sublayout5.addWidget(self.other_seperator)
        sublayout5.addStretch()
        layout.addLayout(sublayout5)