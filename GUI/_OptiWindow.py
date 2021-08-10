''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from UIWindows.UIOptiWindow import *


def OptiWindow(self, n, LastWindow):
    """Activates the GUI window to select the optimizations.

    Before the GUI is activated, the previous window is checked. If
    "Next" is pressed, it is checked whether data has been entered
    for the project name, output path and model path. If everything
    is correct the GUI gets activated. If not a message box appears
    with a warning. Via the two buttons Pruning and Quantization,
    the optimization algorithms can be selected, if desired. The
    pruning factors can be entered via input fields and the data types
    for the quantization via buttons.

    Args:
        n:          Is the window reached by the "Next" or "Back" button
        LastWindow: Which window was the last one
    """
    
    if n == "Next":
        
        self.project_name = LastWindow.project_name.text()
        self.output_path = LastWindow.output_path_label.text()
        self.model_path = LastWindow.model_path_label.text()
            
        if self.project_name == "" or self.model_path == "" or self.output_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            
            msg.setText("Please enter your data")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            
            return
    
    if n == "Back" and hasattr(LastWindow, 'model_memory'):
        if LastWindow.model_memory != "":
            try:
                self.model_memory = int(LastWindow.model_memory.text())
            except:
                self.model_memory = None


    self.Window2 = UIOptiWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
    
    if "Pruning" in self.optimizations:
        self.Window2.Pruning.setChecked(True)
        self.set_pruning(self.Window2)
    if "Quantization" in self.optimizations:
        self.Window2.Quantization.setChecked(True)
        self.set_quantization(self.Window2)

    self.Window2.Pruning.toggled.connect(lambda:self.set_pruning(self.Window2))
    self.Window2.Quantization.toggled.connect(lambda:self.set_quantization(self.Window2))
    
    self.Window2.prun_fac.clicked.connect(lambda:self.set_prun_type("Factor", self.Window2, False))
    self.Window2.prun_acc.clicked.connect(lambda:self.set_prun_type("Accuracy", self.Window2, False))
    
    self.Window2.min_acc.clicked.connect(lambda:self.set_prun_acc_type("Minimal accuracy", self.Window2))
    self.Window2.acc_loss.clicked.connect(lambda:self.set_prun_acc_type("Accuracy loss", self.Window2))
    
    self.Window2.quant_int.clicked.connect(lambda:self.set_quant_dtype("int8 with float fallback", self.Window2))
    self.Window2.quant_int_only.clicked.connect(lambda:self.set_quant_dtype("int8 only", self.Window2))
    
    self.Window2.Back.clicked.connect(lambda:self.StartWindow("Back", self.Window2))
    self.Window2.Next.clicked.connect(lambda:nextWindow(self, self.optimizations))
    
    self.setCentralWidget(self.Window2)
    self.show()


def nextWindow(self, optimizations):
    """
    Defines which one is the next window to open if you
    press "Next". If optimization algorithms were selected,
    the data loader is the next window otherwise the 
    optimization window.

    Args:
        optimizations: Selected optimization algorithms
    """
    if optimizations:
        self.DataloaderWindow("Next", self.Window2)
    else:
        self.LoadWindow(self.Window2)