import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UILoadWindow import *


def LoadWindow(self, LastWindow):  

    if self.optimizations:
        self.data_loader_path = LastWindow.Daten_Pfad.text()
        
        if  self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Please enter a data loader.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return     
             

    
    self.Window4 = UILoadWindow(self.FONT_STYLE, self.model_path, self.project_name, self.output_path, self.data_loader_path, self.prun_factor_dense, self.prun_factor_conv, self.optimizations, self.quant_dtype, self)
    
    self.Window4.Back.clicked.connect(lambda:nextWindow(self, self.optimizations))
    
    self.Window4.Load.clicked.connect(lambda:self.model_pruning(self.Window4))
    
    self.Window4.prune_model.request_signal.connect(lambda:self.download(self.Window4))
    self.Window4.conv_build_load.request_signal.connect(lambda:self.terminate_thread(self.Window4))
    
    self.Window4.Finish.clicked.connect(self.close)
    
    self.setCentralWidget(self.Window4)
    self.show()


def nextWindow(self, optimizations):
    if optimizations:
        self.DataloaderWindow("Back", self.Window4)
    else:
        self.OptiWindow("Back", self.Window4)