import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UIOptiWindow import *
        
def OptiWindow(self, n, LastWindow):
    
    if n == "Next":
        
        self.project_name = LastWindow.Projekt_Name.text()
        self.output_path = LastWindow.Output_Pfad.text()
        self.model_path = LastWindow.Model_Pfad.text()
            
    if self.project_name == "" or self.model_path == "" or self.output_path == "":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
         
        msg.setText("Please enter your data")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        
        return


    self.Window2 = UIOptiWindow(self.FONT_STYLE, self)
    
    if "Pruning" in self.optimizations:
        self.Window2.Pruning.setChecked(True)
        self.set_pruning(self.Window2)
        self.Window2.Pruning_Dense.setText(str(self.prun_factor_dense))
        self.Window2.Pruning_Conv.setText(str(self.prun_factor_conv))
    if "Quantization" in self.optimizations:
        self.Window2.Quantization.setChecked(True)
        self.set_quantization(self.Window2)
        if self.quant_dtype != None:
            if "int8 with float fallback" in self.quant_dtype:
                self.Window2.quant_int_only.setChecked(False)  
                self.Window2.quant_int.setChecked(True)              
            elif "int8 only" in self.quant_dtype:
                self.Window2.quant_int_only.setChecked(True)  
                self.Window2.quant_int.setChecked(False) 

    self.Window2.Pruning.toggled.connect(lambda:self.set_pruning(self.Window2))
    self.Window2.Quantization.toggled.connect(lambda:self.set_quantization(self.Window2))
    
    self.Window2.quant_int.clicked.connect(lambda:self.set_quant_dtype("int8 with float fallback", self.Window2))
    self.Window2.quant_int_only.clicked.connect(lambda:self.set_quant_dtype("int8 only", self.Window2))
    
    self.Window2.Back.clicked.connect(lambda:self.StartWindow())
    self.Window2.Next.clicked.connect(lambda:nextWindow(self, self.optimizations))
    
    self.setCentralWidget(self.Window2)
    self.show()


def nextWindow(self, optimizations):
    if optimizations:
        self.DataloaderWindow("Next", self.Window2)
    else:
        self.LoadWindow("Next", self.Window2)