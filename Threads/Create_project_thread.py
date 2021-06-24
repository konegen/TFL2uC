import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Auto_TF_to_uC.create_project import *
import subprocess as sub


class Convert_Build(QThread):
    """Thread to convert the model and build the project.

    Attributes:
        model_path:       Path of the model to convert
        project_name:     Name of the project to be created
        output_path:      Output path of the project to be created
        optimizations:    Selected optimization algorithms
        data_loader_path: Path of the folder or file with the training data
        quant_dtype:      Data type to quantize to
        separator:        Separator for reading a CSV file
        csv_target_label: Target label from the CSV file
    """
    
    request_signal = pyqtSignal()
    
    def __init__(self, model_path, project_name, output_path, optimizations, data_loader_path, quant_dtype, separator, csv_target_label):
        QThread.__init__(self)
        self.model_path = model_path
        self.project_name = project_name
        self.output_path = output_path
        self.optimizations = optimizations
        self.data_loader_path = data_loader_path
        self.quant_dtype = quant_dtype
        self.separator = separator
        self.csv_target_label = csv_target_label

    def run(self):
        """Activates the thread

        Calls the function to convert the model and build the project.
        When the function is finished, a signal is emitted.
        """
        convert_and_write(self.model_path, self.project_name, self.output_path, self.optimizations, self.data_loader_path, self.quant_dtype, self.separator, self.csv_target_label)
        self.request_signal.emit()
        
    def stop_thread(self):
        """Ends the thread
        """
        self.terminate()
