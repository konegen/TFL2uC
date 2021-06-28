import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    """Initialization of the GUI main window.

    All initializations of the different GUI windows get imported.
    Also all functions get from the '_Helper.py' file imported.
    The window size and title get initialized as well as all attributes
    needed. In addition, the GUI is started.

    Attributes:
        FONT_STYLE:        Font which is used in the GUI
        project_name:      Name of the project to be created
        output_path:       Output path of the project to be created
        model_path:        Path of the model to convert
        data_loader_path:  Path of the folder or file with the training data
        optimizations:     Selected optimization algorithms
        prun_factor_dense: Pruning factor for fully connected layers
        prun_factor_conv:  Pruning factor for convolution layers
        quant_dtype:       Data type to quantize to
        separator:         Separator for reading a CSV file
        csv_target_label:  Target label from the CSV file
    """
    from ._CSVDataloaderWindow import CSVDataloaderWindow
    from ._DataloaderWindow import DataloaderWindow
    from ._LoadWindow import LoadWindow
    from ._OptiWindow import OptiWindow
    from ._StartWindow import StartWindow

    from ._Helper import (
        get_output_path,
        get_model_path,
        get_data_loader,
        set_pruning,
        set_quantization,
        set_prun_type,
        set_quant_dtype,
        get_optimization,
        model_pruning,
        download,
        terminate_thread,
        browseCSVData,
        previewCSVData,
        loadCSVData,
        get_separator
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

        self.prun_type = None
        self.prun_factor_dense = None
        self.prun_factor_conv = None
        self.quant_dtype = None
        
        self.separator = None
        self.csv_target_label = None

        self.StartWindow(None)