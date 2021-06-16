import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UIDataloaderWindow import *

def DataloaderWindow(self, n, LastWindow):

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

                print("Prunfactor Dense: " + str(self.prun_factor_dense) + ", Prunfactor Conv: " + str(self.prun_factor_conv))
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

        if "Quantization" in self.optimizations:
            if LastWindow.quant_int_only.isChecked():
                self.quant_dtype = "int8 only"
            elif LastWindow.quant_int.isChecked():
                self.quant_dtype = "int8 with float fallback"
            else:
                print("No datatype for quantization is selected.")

            print(self.quant_dtype)


    self.Window3 = UIDataloaderWindow(self.FONT_STYLE, self)
    
    if self.data_loader_path != None:
        self.Window3.Daten_Pfad.setText(self.data_loader_path)


    self.Window3.Daten_einlesen_Browse.clicked.connect(lambda:self.get_data_loader(self.Window3))
    
    self.Window3.Next.clicked.connect(lambda:self.LoadWindow(self.Window3))
    self.Window3.Back.clicked.connect(lambda:self.OptiWindow("Back", self.Window3))
    
    self.setCentralWidget(self.Window3)
    self.show()