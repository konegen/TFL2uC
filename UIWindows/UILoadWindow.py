import os
import sys

from tensorflow.python.ops.ragged.ragged_tensor import _assert_sparse_indices_are_ragged_right
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Threads.Loading_images_thread import * 
from Threads.Create_project_thread import *
from Threads.Prune_model_thread import *



class UILoadWindow(QWidget):
    """Builds the project. 

    If selected the model get optimized. After that it gets converted
    and all necessary files get created.
    """
    def __init__(self, FONT_STYLE, model_path, project_name, output_path, data_loader_path, optimizations, prun_type, prun_factor_dense, prun_factor_conv, prun_acc_type, prun_acc, quant_dtype, separator, csv_target_label, parent=None):
        super(UILoadWindow, self).__init__(parent)
        
        self.FONT_STYLE = FONT_STYLE 
        self.model_path = model_path       
        self.project_name = project_name
        self.output_path = output_path
        self.data_loader_path = data_loader_path
        self.optimizations = optimizations
        self.prun_type = prun_type
        self.prun_factor_dense = prun_factor_dense
        self.prun_factor_conv = prun_factor_conv
        self.prun_acc_type = prun_acc_type
        self.prun_acc = prun_acc
        self.quant_dtype = quant_dtype
        self.separator = separator
        self.csv_target_label = csv_target_label
        
        
        self.label = QLabel("Create Projectfiles")
        self.label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
        self.Loadpng = QLabel(self)
        img = QPixmap(os.path.join('Images','GUI_loading_images', 'GUI_load_0.png'))
        self.Loadpng.setPixmap(img)
        self.Loadpng.setVisible(False)

        self.summary = QLabel("Summary")
        self.summary.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.summary.setFixedWidth(90)
        self.summary.setFixedHeight(30)
        self.summary.setAlignment(Qt.AlignCenter)

        self.project_name_label = QLabel("Projectname: \t" + self.project_name)
        self.project_name_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.project_name_label.setFixedWidth(600)
        self.project_name_label.setFixedHeight(30)
        self.project_name_label.setAlignment(Qt.AlignLeft)

        self.output_path_label = QLabel("Output path: \t" + self.output_path)
        self.output_path_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.output_path_label.setFixedWidth(600)
        self.output_path_label.setFixedHeight(30)
        self.output_path_label.setAlignment(Qt.AlignLeft)

        self.model_path_label = QLabel("Model path: \t" + self.model_path)
        self.model_path_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.model_path_label.setFixedWidth(600)
        self.model_path_label.setFixedHeight(30)
        self.model_path_label.setAlignment(Qt.AlignLeft)

        if "Pruning" in self.optimizations and "Quantization" in self.optimizations:
            self.optimizations_label = QLabel("Optimizations: \tPruning + Quantization")
        elif len(self.optimizations) != 0:
            self.optimizations_label = QLabel("Optimizations: \t" + self.optimizations[0])
        else:
            self.optimizations_label = QLabel("Optimizations: \t-")
        self.optimizations_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.optimizations_label.setFixedWidth(600)
        self.optimizations_label.setFixedHeight(30)
        self.optimizations_label.setAlignment(Qt.AlignLeft)

        self.pruning_label = QLabel()
        if "Pruning" in self.optimizations:
            if "Factor" in self.prun_type:
                self.pruning_label = QLabel("Pruning: \tPruningfactor dense: " + str(self.prun_factor_dense) + "   Pruningfactor conv: " + str(self.prun_factor_conv))
            else:
                if "Minimal Accuracy" in self.prun_acc_type:
                    self.pruning_label = QLabel("Pruning: \tMinimal accuracy to reach: " + str(self.prun_acc))
                else:
                    self.pruning_label = QLabel("Pruning: \tMaximal accuracy loss: " + str(self.prun_acc))
            self.pruning_label.setStyleSheet("font: 12pt " + FONT_STYLE)
            self.pruning_label.setFixedWidth(600)
            self.pruning_label.setFixedHeight(30)
            self.pruning_label.setAlignment(Qt.AlignLeft)
        else:
            self.pruning_label.setVisible(False)

        self.quantization_label = QLabel()
        if "Quantization" in self.optimizations:
            if "int8 only" in self.quant_dtype:
                self.quantization_label = QLabel("Quantization: \tInt8 only")
            else:
                self.quantization_label = QLabel("Quantization: \tInt8 with float32 fallback")
            self.quantization_label.setStyleSheet("font: 12pt " + FONT_STYLE)
            self.quantization_label.setFixedWidth(600)
            self.quantization_label.setFixedHeight(30)
            self.quantization_label.setAlignment(Qt.AlignLeft)
        else:
            self.quantization_label.setVisible(False)

        self.data_loader_label = QLabel()
        if len(self.optimizations) != 0:
            self.data_loader_label = QLabel("Dataloader: \t" + self.data_loader_path)
            self.data_loader_label.setStyleSheet("font: 12pt " + FONT_STYLE)
            self.data_loader_label.setFixedWidth(600)
            self.data_loader_label.setFixedHeight(30)
            self.data_loader_label.setAlignment(Qt.AlignLeft)
        else:
            self.data_loader_label.setVisible(False)
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar_Demonstrator', 'GUI_demonstrator_step_4.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Finish = QPushButton("Finish", self)
        self.Finish.setFixedWidth(125)
        self.Finish.setVisible(False)
        self.Finish.setToolTip('...')
        self.Finish.setStyleSheet("""QPushButton {
                           font: 12pt """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)

        self.Load = QPushButton(self)
        self.Load.setIcon(QIcon(os.path.join('Images', 'load_arrow.png')))
        self.Load.setIconSize(QSize(25, 25))
        self.Load.setFixedHeight(30)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.Loadpng)
        self.horizontal_box[1].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.summary)
        self.horizontal_box[2].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addWidget(self.project_name_label)
        self.horizontal_box[3].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.output_path_label)
        self.horizontal_box[4].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addStretch()
        self.horizontal_box[5].addWidget(self.model_path_label)
        self.horizontal_box[5].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.optimizations_label)
        self.horizontal_box[6].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.pruning_label)
        self.horizontal_box[7].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[8].addStretch()
        self.horizontal_box[8].addWidget(self.quantization_label)
        self.horizontal_box[8].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[9].addStretch()
        self.horizontal_box[9].addWidget(self.data_loader_label)
        self.horizontal_box[9].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[10].addStretch()
        self.horizontal_box[10].addWidget(self.Finish)
        self.horizontal_box[10].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[11].addWidget(self.Back)
        self.horizontal_box[11].addStretch()
        self.horizontal_box[11].addWidget(self.Schritt) 
        self.horizontal_box[11].addStretch()         
        self.horizontal_box[11].addWidget(self.Load)
        self.horizontal_box[11].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)
        
        self.loading_images = Loading_images(self.Loadpng)
        
        self.prune_model = Prune_model(self.model_path, self.data_loader_path, self.optimizations, self.prun_type, self.prun_factor_dense, self.prun_factor_conv, self.prun_acc_type, self.prun_acc, self.separator, self.csv_target_label)

        
        if 'Pruning' in optimizations:
            self.conv_build_load = Convert_Build(str(self.model_path[:-3]) + '_pruned.h5', self.project_name, self.output_path, self.optimizations, self.data_loader_path, self.quant_dtype, self.separator, self.csv_target_label)
        else:
            self.conv_build_load = Convert_Build(self.model_path, self.project_name, self.output_path, self.optimizations, self.data_loader_path, self.quant_dtype, self.separator, self.csv_target_label)
            