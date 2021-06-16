import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import pandas as pd

class UICSVDataloaderWindow(QWidget):
    def __init__(self, FONT_STYLE):
        super().__init__()
        
        self.FONT_STYLE = FONT_STYLE 

        self.window_width, self.window_height = 400, 300
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

        self.cb1 = QCheckBox('Tab stop', self)
        self.cb1.setStyleSheet("font: 11pt " + FONT_STYLE)
        layout.addWidget(self.cb1)

        self.cb2 = QCheckBox('Semicolon', self)
        self.cb2.setStyleSheet("font: 11pt " + FONT_STYLE)
        layout.addWidget(self.cb2)

        self.cb3 = QCheckBox('Comma', self)
        self.cb3.setStyleSheet("font: 11pt " + FONT_STYLE)
        layout.addWidget(self.cb3)

        self.cb4 = QCheckBox('Space', self)
        self.cb4.setStyleSheet("font: 11pt " + FONT_STYLE)
        layout.addWidget(self.cb4)

        self.cb5 = QCheckBox('other', self)
        self.cb5.setStyleSheet("font: 11pt " + FONT_STYLE)

        self.other_delimiter = QLineEdit()
        self.other_delimiter.setFixedWidth(50)
        self.other_delimiter.setMaxLength(1)
        self.other_delimiter.setStyleSheet("font: 11pt " + FONT_STYLE)

        sublayout_other = QHBoxLayout()
        sublayout_other.addWidget(self.cb5)
        sublayout_other.addWidget(self.other_delimiter)
        sublayout_other.addStretch()
        layout.addLayout(sublayout_other)


        self.w = None