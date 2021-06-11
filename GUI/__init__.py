"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""



import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """
    from ._DataloaderWindow import DataloaderWindow
    from ._LoadWindow import LoadWindow
    from ._OptiWindow import OptiWindow
    from ._StartWindow import StartWindow

    from ._Helper import (
        get_output_path,
        get_model_path,
        get_data_loader_path,
        set_pruning,
        set_quantization,
        set_quant_dtype,
        get_optimization,
        model_pruning,
        download,
        terminate_thread,
        # optimization_before_load
    )

    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("TFL2uC")
        self.setWindowIcon(QIcon(os.path.join("Images", "Window_Icon_blue.png")))
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        self.FONT_STYLE = "Helvetica"

        self.project_name = None
        self.output_path = None
        self.model_path = None
        self.data_loader_path = None
        self.optimizations = []

        self.prun_factor_dense = None
        self.prun_factor_conv = None
        self.quant_dtype = None

        self.StartWindow()