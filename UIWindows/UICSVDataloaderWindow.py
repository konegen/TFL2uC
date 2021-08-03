import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UICSVDataloaderWindow(QWidget):
    """Get a preview and load CSV data. 

    This GUI window shows the data format of CSV files, selected
    from the dataloader. You can also choose how to separate the 
    different columns and whats the target column.
    """
    def __init__(self, FONT_STYLE, parent=None):
        super(UICSVDataloaderWindow, self).__init__(parent)

        self.setWindowModality(Qt.ApplicationModal)

        self.window_width, self.window_height = 700, 500
        self.setFixedSize(self.window_width, self.window_height)
        self.setWindowTitle('CSV dataloader')
        self.setWindowIcon(QIcon(os.path.join("Images", "Window_Icon_blue.png")))
        
        self.FONT_STYLE = FONT_STYLE 

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.Browse = QPushButton('Browse...')
        self.Browse.setFixedWidth(150)
        self.Browse.setFixedHeight(30)
        self.Browse.setToolTip('Select a CSV file')
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
        self.Preview.setToolTip('Show an overview of how the data will look with\n'
                                'the selected settings, in the table above.')
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
        self.Load_data.setToolTip('Closes the CSV dataloader window and takes the\n'
                                  'chosen settings for the later optimization.')
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

        self.label_col = QLabel("Label column:")
        self.label_col.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.label_col.setFixedWidth(250)
        self.label_col.setVisible(False)

        self.cbTab = QCheckBox('Tab stop', self)
        self.cbTab.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbTab.setFixedWidth(150)
        layout.addWidget(self.cbTab)

        sublayout2 = QHBoxLayout()
        sublayout2.addWidget(self.cbTab)
        sublayout2.addStretch()
        sublayout2.addWidget(self.label_col)
        sublayout2.addStretch()
        sublayout2.addStretch()
        layout.addLayout(sublayout2)
        
        self.cb_label_col = QComboBox()
        self.cb_label_col.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cb_label_col.setFixedWidth(80)
        self.cb_label_col.addItems(["First", "Last"])
        self.cb_label_col.setVisible(False)

        self.cbSemicolon = QCheckBox('Semicolon', self)
        self.cbSemicolon.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbSemicolon.setFixedWidth(150)

        sublayout3 = QHBoxLayout()
        sublayout3.addWidget(self.cbSemicolon)
        sublayout3.addStretch()
        sublayout3.addWidget(self.cb_label_col)
        sublayout3.addStretch()
        sublayout3.addStretch()
        sublayout3.addStretch()
        sublayout3.addStretch()
        layout.addLayout(sublayout3)

        self.numRow = QLabel()
        self.numRow.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.numRow.setFixedWidth(250)
        self.numRow.setAlignment(Qt.AlignLeft)

        self.cbComma = QCheckBox('Comma', self)
        self.cbComma.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbComma.setFixedWidth(150)

        sublayout4 = QHBoxLayout()
        sublayout4.addWidget(self.cbComma)
        sublayout4.addStretch()
        sublayout4.addWidget(self.numRow)
        sublayout4.addStretch()
        sublayout4.addStretch()
        layout.addLayout(sublayout4)

        self.numCol = QLabel()
        self.numCol.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.numCol.setFixedWidth(250)
        self.numCol.setAlignment(Qt.AlignLeft)

        self.cbSpace = QCheckBox('Space', self)
        self.cbSpace.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbSpace.setFixedWidth(150)

        sublayout5 = QHBoxLayout()
        sublayout5.addWidget(self.cbSpace)
        sublayout5.addStretch()
        sublayout5.addWidget(self.numCol)
        sublayout5.addStretch()
        sublayout5.addStretch()
        layout.addLayout(sublayout5)

        self.cbOther = QCheckBox('other', self)
        self.cbOther.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.cbOther.setFixedWidth(65)

        self.other_separator = QLineEdit()
        self.other_separator.setFixedWidth(30)
        self.other_separator.setMaxLength(1)
        self.other_separator.setStyleSheet("font: 11pt " + FONT_STYLE)

        sublayout6 = QHBoxLayout()
        sublayout6.addWidget(self.cbOther)
        sublayout6.addWidget(self.other_separator)
        sublayout6.addStretch()
        layout.addLayout(sublayout6)