''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from UIWindows.UIStartWindow import *


def StartWindow(self, n, LastWindow):
    """Activates the GUI window to select output path, project name
       and model path.

    The GUI gets activated. If you get "Back" from the "OptiWindow"
    "project_name", "output_path" and "model_path" get set. This data
    can be entered/selected via an input field and browse window.
    not a message box appears

    Args:
        n:          Is the window reached by the "Next" or "Back" button
        LastWindow: Which window was the last one
    """

    self.Window1 = UIStartWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
    
    if n == "Back":
        self.Window1.project_name.setText(self.project_name)
        self.set_output_path_label(self.Window1)
        self.set_model_path_label(self.Window1)

        try:
            if "Factor" in self.prun_type:
                self.prun_factor_dense = int(LastWindow.Pruning_Dense.text())
                self.prun_factor_conv = int(LastWindow.Pruning_Conv.text())
            elif "Accuracy" in self.prun_type:
                self.prun_acc = int(LastWindow.prun_acc_edit.text())
        except:
            self.prun_acc = ""
            self.prun_factor_dense = ""
            self.prun_factor_conv = ""


    self.Window1.output_path_Browse.clicked.connect(lambda:self.get_output_path(self.Window1))
    self.Window1.read_model_browse.clicked.connect(lambda:self.get_model_path(self.Window1))
    
    self.Window1.Next.clicked.connect(lambda:self.OptiWindow("Next", self.Window1))
    
    self.setCentralWidget(self.Window1)
    self.show()