import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UICSVDataloaderWindow import *

def CSVDataloaderWindow(self):

    self.Window4 = UICSVDataloaderWindow(self.FONT_STYLE, self)

    self.Window4.Browse.clicked.connect(self.browseCSVData)
    self.Window4.Preview.clicked.connect(lambda: self.previewCSVData(self.Window4))
    self.Window4.Load_data.clicked.connect(self.loadCSVData)

    self.setCentralWidget(self.Window4)
    self.Window4.show()