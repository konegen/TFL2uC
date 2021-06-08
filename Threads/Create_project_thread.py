import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Auto_TF_to_uC.create_project import *
import subprocess as sub


class Convert_Build_Loading(QThread):
    
    request_signal = pyqtSignal()
    
    def __init__(self, model_path, project_name, output_path, optimizations, datascript_path, quant_dtype):
        QThread.__init__(self)
        self.model_path = model_path
        self.project_name = project_name
        self.output_path = output_path
        self.optimizations = optimizations
        self.datascript_path = datascript_path
        self.quant_dtype = quant_dtype
        

    def run(self):
          
        convert_and_write(self.model_path, self.project_name, self.output_path, self.optimizations, self.datascript_path, self.quant_dtype)
        self.request_signal.emit()
        
    def stop_thread(self):
        self.terminate()
