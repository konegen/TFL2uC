import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UIDataloaderWindow import *

def DataloaderWindow(self):

    self.Window3 = UIDataloaderWindow(self.FONT_STYLE, self)


    self.Window3.Daten_einlesen_Browse.clicked.connect(self.CSVDataloaderWindow)
    
    self.setCentralWidget(self.Window3)
    self.show()