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
            if self.prun_type == None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                
                msg.setText("Select a pruning type")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return
            
            elif "Factor" in self.prun_type:
                try:
                    if int(LastWindow.Pruning_Dense.text()) > 95  or int(LastWindow.Pruning_Conv.text()) > 95:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        
                        msg.setText("Enter prunefactors less than 95")
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

            elif "Accuracy" in self.prun_type:
                try:
                    if self.prun_acc_type == None:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        
                        msg.setText("Select a type for pruning")
                        msg.setWindowTitle("Warning")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        msg.exec_()
                        return

                    if "Minimal accuracy" in self.prun_acc_type:
                        if int(LastWindow.prun_acc_edit.text()) < 50 or int(LastWindow.prun_acc_edit.text()) > 99:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            
                            msg.setText("Enter a value for minimal Accuracy between 50 and 99")
                            msg.setWindowTitle("Warning")
                            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                            msg.exec_()
                            return
                    else:
                        if int(LastWindow.prun_acc_edit.text()) < 1 or int(LastWindow.prun_acc_edit.text()) > 20:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            
                            msg.setText("Enter a value for maximal accuracy loss between 1 and 20")
                            msg.setWindowTitle("Warning")
                            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                            msg.exec_()
                            return
                    
                    self.prun_acc = int(LastWindow.prun_acc_edit.text())
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
    
    else:
        if LastWindow.model_memory != "":
            try:
                self.model_memory = int(LastWindow.model_memory.text())
            except:
                self.model_memory = None


    self.Window3 = UIDataloaderWindow(self.FONT_STYLE, self)

    if self.data_loader_path != None:
        self.Window3.Daten_Pfad.setText(self.data_loader_path)

    self.Window3.Daten_einlesen_Browse.clicked.connect(lambda: self.get_data_loader(self.Window3))

    self.Window3.Back.clicked.connect(lambda: self.OptiWindow("Back", self.Window3))
    self.Window3.Next.clicked.connect(lambda: self.LoadWindow(self.Window3))
    
    self.setCentralWidget(self.Window3)
    self.show()