''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

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
        self.data_loader_path = LastWindow.data_path.text()
        
        if  self.data_loader_path == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Please enter a data loader.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return     


    
    self.Window4 = UILoadWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self.model_path, self.project_name, self.output_path, self.data_loader_path, self.optimizations, self.prun_type, self.prun_factor_dense, self.prun_factor_conv, self.prun_acc_type, self.prun_acc, self.quant_dtype, self.separator, self.csv_target_label, self)
    
    if isinstance(self.model_memory, int):
        self.Window4.model_memory.setText(str(self.model_memory))

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