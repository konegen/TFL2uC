import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UIStartWindow import *

def StartWindow(self):
    self.Window1 = UIStartWindow(self.FONT_STYLE, self)
    
    if self.output_path != None:
        self.Window1.Output_Pfad.setText(self.output_path)
    
    if self.project_name != None:
        self.Window1.Projekt_Name.setText(self.project_name)
    
    if self.model_path != None:
        self.Window1.Model_Pfad.setText(self.model_path)

    
    self.Window1.Output_Pfad_Browse.clicked.connect(lambda:self.get_output_path(self.Window1))
    self.Window1.Modell_einlesen_Browse.clicked.connect(lambda:self.get_model_path(self.Window1))
    
    self.Window1.Next.clicked.connect(lambda:self.OptiWindow("Next", self.Window1))
    
    self.setCentralWidget(self.Window1)
    self.show()