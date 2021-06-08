import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from UIWindows.UILoadWindow import *


def LoadWindow(self, n, LastWindow):  

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
                
        if self.optimizations and self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Please enter a data loader at the start window.")
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

        print(self.prun_factor_dense, self.prun_factor_conv)
        print(self.quant_dtype)
        
        if self.optimizations and self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Please enter a data loader at the start window.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            
            return       
    
    self.Window3 = UILoadWindow(self.FONT_STYLE, self.model_path, self.project_name, self.output_path, self.data_loader_path, self.prun_factor_dense, self.prun_factor_conv, self.optimizations, self.quant_dtype, self)
    
    self.Window3.Back.clicked.connect(lambda:self.OptiWindow("Back", self.Window3))
    
    self.Window3.Load.clicked.connect(lambda:self.model_pruning(self.Window3))
    
    self.Window3.prune_model.request_signal.connect(lambda:self.download(self.Window3))
    self.Window3.conv_build_load.request_signal.connect(lambda:self.terminate_thread(self.Window3))
    
    self.Window3.Finish.clicked.connect(self.close)
    
    self.setCentralWidget(self.Window3)
    self.show()