import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UIDataloaderWindow import *

def DataloaderWindow(self, n, LastWindow):
    """Activates the GUI window of the data loader.

    Before the GUI is activated, the previous window is checked. If
    "Next" is pressed and pruning and/or quantization have been
    selected as optimization algorithms, it is checked whether the
    entries are correct and complete. If everything is correct the
    GUI gets activated. If not a message box appears with a warning.
    With the dropdown menu you can select whether the training data
    should be transferred in a file or folder.

    Args:
        n:          Is the window reached by the "Next" or "Back" button
        LastWindow: Which window was the last one
    """
    if n == "Next":
        if "Pruning" in self.optimizations:
            try:
                if int(LastWindow.Pruning_Dense.text()) < 5 or int(LastWindow.Pruning_Dense.text()) > 95  or int(LastWindow.Pruning_Conv.text()) < 5  or int(LastWindow.Pruning_Conv.text()) > 95:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                     
                    msg.setText("Enter prunefactors between 5 and 95")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return
                
                self.prun_factor_dense = int(LastWindow.Pruning_Dense.text())
                self.prun_factor_conv = int(LastWindow.Pruning_Conv.text())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                 
                msg.setText("Please enter a number for pruning or disable it.")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return
        
        if "Quantization" in self.optimizations and self.quant_dtype == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Enter a dtype for quantization.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

    self.Window3 = UIDataloaderWindow(self.FONT_STYLE, self)


    self.Window3.Daten_einlesen_Browse.clicked.connect(lambda: self.get_data_loader(self.Window3))

    self.Window3.Back.clicked.connect(lambda: self.OptiWindow("Back", self.Window3))
    self.Window3.Next.clicked.connect(lambda: self.LoadWindow(self.Window3))
    
    self.setCentralWidget(self.Window3)
    self.show()