''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os

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
        set_output_path_label,
        get_model_path,
        set_model_path_label,
        get_data_loader,
        set_data_loader_label,
        set_pruning,
        set_quantization,
        set_prun_type,
        set_prun_acc_type,
        set_quant_dtype,
        model_pruning,
        download,
        terminate_thread,
        dataloader_quantization,
        dataloader_pruning,
        browseCSVData,
        previewCSVData,
        loadCSVData,
        get_separator
    )

    def __init__(self, screen_width, screen_height, parent=None):
        
        super(MainWindow, self).__init__(parent)

        """Set width and height of the window in respect to the resolution of the screen
        """
        if screen_width/screen_height >= 2: #>= 2:1
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.4*screen_width), int(0.64*screen_height)
        elif screen_width/screen_height <= 0.5: #>= 2:1 Hochformat
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.85*screen_width), int(0.3*screen_height)
        elif abs(screen_width/screen_height - 4/3) < 0.1: #4:3
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.55*screen_width), int(0.5*screen_height)
        elif abs(screen_width/screen_height - 3/4) < 0.1: #4:3 Hochformat
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.75*screen_width), int(0.4*screen_height)
        elif abs(screen_width/screen_height - 16/10) < 0.1: #16:10
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.5*screen_width), int(0.6*screen_height)
        elif abs(screen_width/screen_height - 10/16) < 0.1: #16:10 Hochformat
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.8*screen_width), int(0.35*screen_height)
        else:
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.45*screen_width), int(0.6*screen_height)

        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.setWindowTitle("TFL2uC")
        self.setWindowIcon(QIcon(os.path.join("Images", "Window_Icon_blue.png")))

        self.FONT_STYLE = "Helvetica"

        self.project_name = None
        self.output_path = None
        self.model_path = None
        self.data_loader_path = None
        self.optimizations = []

        self.prun_type = None
        self.prun_factor_dense = None
        self.prun_factor_conv = None
        self.prun_acc_type = None
        self.prun_acc = None
        self.quant_dtype = None
        
        self.separator = None
        self.csv_target_label = None

        self.model_memory = None

        self.StartWindow(None,None)