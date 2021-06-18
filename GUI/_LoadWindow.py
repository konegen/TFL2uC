import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UILoadWindow import *


def LoadWindow(self, LastWindow):
    """Activates the GUI window to create the project.

    Before the GUI is activated, the previous window is checked. If
    pruning and/or quantization have been selected as optimization
    algorithms, it is checked whether a data loader was selected.
    If everything is correct the GUI gets activated. If not
    a message box appears with a warning. When the load button is
    selected, the optimization algorithms are applied if any are
    selected. Also, the model is converted and the files are created.

    Args:
        LastWindow: Which window was the last one
    """

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
             

    
    self.Window4 = UILoadWindow(self.FONT_STYLE, self.model_path, self.project_name, self.output_path, self.data_loader_path, self.prun_factor_dense, self.prun_factor_conv, self.optimizations, self.quant_dtype, self.separator, self.csv_target_label, self)
    
    self.Window4.Back.clicked.connect(lambda:nextWindow(self, self.optimizations))
    
    self.Window4.Load.clicked.connect(lambda:self.model_pruning(self.Window4))
    
    self.Window4.prune_model.request_signal.connect(lambda:self.download(self.Window4))
    self.Window4.conv_build_load.request_signal.connect(lambda:self.terminate_thread(self.Window4))
    
    self.Window4.Finish.clicked.connect(self.close)
    
    self.setCentralWidget(self.Window4)
    self.show()


def nextWindow(self, optimizations):
    """
    Defines which one is the next window to open if you
    press "Back". If optimization algorithms were previously
    selected, the data loader is the next window otherwise
    the optimization window.

    Args:
        optimizations: Selected optimization algorithms
    """
    if optimizations:
        self.DataloaderWindow("Back", self.Window4)
    else:
        self.OptiWindow("Back", self.Window4)