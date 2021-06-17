import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UICSVDataloaderWindow import *

def CSVDataloaderWindow(self):
    """Activates the GUI window to preview and load CSV data.

    With the help of the check boxes the separators can be selected 
    There are three buttons to interact with. With "Browse" you can
    select the CSV file you want to use. "Preview" shows format of
    the CSV file according to the selected separators. "Load data"
    selects the settings of the preview and take them to train the
    model later.    
    """

    self.Window4 = UICSVDataloaderWindow(self.FONT_STYLE)

    self.Window4.Browse.clicked.connect(self.browseCSVData)
    self.Window4.Preview.clicked.connect(lambda: self.previewCSVData(self.Window4))
    self.Window4.Load_data.clicked.connect(self.loadCSVData)

    # self.setCentralWidget(self.Window4)
    self.Window4.show()