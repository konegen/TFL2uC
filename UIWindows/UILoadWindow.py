''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os
import sys
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
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, model_path, project_name, output_path, data_loader_path, optimizations, prun_type, prun_factor_dense, prun_factor_conv, prun_acc_type, prun_acc, quant_dtype, separator, csv_target_label, parent=None):
        super(UILoadWindow, self).__init__(parent)
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT 
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
        self.label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Loadpng = QLabel(self)
        self.Loadpng.setFixedWidth(0.3*self.WINDOW_HEIGHT)
        self.Loadpng.setFixedHeight(0.3*self.WINDOW_HEIGHT)
        img = QPixmap(os.path.join('Images','GUI_loading_images', 'GUI_load_0.png'))
        self.Loadpng.setPixmap(img)
        self.Loadpng.setVisible(False)
        self.Loadpng.setScaledContents(True)
        
        self.model_memory_label = QLabel("Model memory:")
        self.model_memory_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.model_memory_label.setFixedWidth(0.19*self.WINDOW_WIDTH)
        self.model_memory_label.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.model_memory_label.setAlignment(Qt.AlignLeft)
        
        self.model_memory = QLineEdit(self)
        self.model_memory.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.model_memory.setFixedWidth(0.075*self.WINDOW_WIDTH)
        self.model_memory.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.model_memory.setAlignment(Qt.AlignLeft)
        
        self.model_memory_label_kb = QLabel("kB")
        self.model_memory_label_kb.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.model_memory_label_kb.setFixedWidth(0.52*self.WINDOW_WIDTH)
        self.model_memory_label_kb.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.model_memory_label_kb.setAlignment(Qt.AlignLeft)

        self.summary = QLabel("Summary")
        self.summary.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.summary.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.summary.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.summary.setAlignment(Qt.AlignCenter)

        self.project_name_label = QLabel("Projectname: \t" + self.project_name)
        self.project_name_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.project_name_label.setFixedWidth(0.8*self.WINDOW_WIDTH)
        self.project_name_label.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.project_name_label.setAlignment(Qt.AlignLeft)

        self.output_path_label = QLabel("Output path: \t" + self.output_path)
        self.output_path_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.output_path_label.setFixedWidth(0.8*self.WINDOW_WIDTH)
        self.output_path_label.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.output_path_label.setAlignment(Qt.AlignLeft)

        self.model_path_label = QLabel("Model path: \t" + self.model_path)
        self.model_path_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.model_path_label.setFixedWidth(0.8*self.WINDOW_WIDTH)
        self.model_path_label.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.model_path_label.setAlignment(Qt.AlignLeft)

        if "Pruning" in self.optimizations and "Quantization" in self.optimizations:
            self.optimizations_label = QLabel("Optimization: \tPruning + Quantization")
        elif len(self.optimizations) != 0:
            self.optimizations_label = QLabel("Optimization: \t" + self.optimizations[0])
        else:
            self.optimizations_label = QLabel("Optimization: \t-")
        self.optimizations_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.optimizations_label.setFixedWidth(0.8*self.WINDOW_WIDTH)
        self.optimizations_label.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.optimizations_label.setAlignment(Qt.AlignLeft)

        self.pruning_label = QLabel()
        if "Pruning" in self.optimizations:
            if "Factor" in self.prun_type:
                self.pruning_label = QLabel("Pruning: \tPruningfactor dense: " + str(self.prun_factor_dense) + "%" + "   Pruningfactor conv: " + str(self.prun_factor_conv) + "%")
            else:
                if "Minimal Accuracy" in self.prun_acc_type:
                    self.pruning_label = QLabel("Pruning: \tMinimal accuracy to reach: " + str(self.prun_acc) + "%")
                else:
                    self.pruning_label = QLabel("Pruning: \tMaximal accuracy loss: " + str(self.prun_acc) + "%")
            self.pruning_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
            self.pruning_label.setFixedWidth(0.8*self.WINDOW_WIDTH)
            self.pruning_label.setFixedHeight(0.05*self.WINDOW_HEIGHT)
            self.pruning_label.setAlignment(Qt.AlignLeft)
        else:
            self.pruning_label.setVisible(False)

        self.quantization_label = QLabel()
        if "Quantization" in self.optimizations:
            if "int8 only" in self.quant_dtype:
                self.quantization_label = QLabel("Quantization: \tInt8 only")
            else:
                self.quantization_label = QLabel("Quantization: \tInt8 with float32 fallback")
            self.quantization_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
            self.quantization_label.setFixedWidth(0.8*self.WINDOW_WIDTH)
            self.quantization_label.setFixedHeight(0.05*self.WINDOW_HEIGHT)
            self.quantization_label.setAlignment(Qt.AlignLeft)
        else:
            self.quantization_label.setVisible(False)

        self.data_loader_label = QLabel()
        if len(self.optimizations) != 0:
            self.data_loader_label = QLabel("Dataloader: \t" + self.data_loader_path)
            self.data_loader_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
            self.data_loader_label.setFixedWidth(0.8*self.WINDOW_WIDTH)
            self.data_loader_label.setFixedHeight(0.05*self.WINDOW_HEIGHT)
            self.data_loader_label.setAlignment(Qt.AlignLeft)
        else:
            self.data_loader_label.setVisible(False)
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.025*self.WINDOW_HEIGHT)
        self.step.setFixedWidth(0.35*self.WINDOW_WIDTH)
        step_img = QPixmap(os.path.join('Images', 'GUI_progress_bar_Demonstrator', 'GUI_demonstrator_step_4.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        self.step.setScaledContents(True)
        
        self.Finish = QPushButton("Finish", self)
        self.Finish.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.Finish.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.Finish.setVisible(False)
        self.Finish.setStyleSheet("""QPushButton {
                           font: 20px """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           font: 13px """ + FONT_STYLE + """
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 

        self.Finish_placeholder = QLabel("", self)
        self.Finish_placeholder.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.Finish_placeholder.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.Back.setFixedHeight(0.05*self.WINDOW_HEIGHT)

        self.Load = QPushButton(self)
        self.Load.setIcon(QIcon(os.path.join('Images', 'load_arrow.png')))
        self.Load.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.Load.setFixedHeight(0.05*self.WINDOW_HEIGHT)

        self.Back_Load_placeholder = QLabel("", self)
        self.Back_Load_placeholder.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.Back_Load_placeholder.setVisible(False)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.model_memory_label)
        self.horizontal_box[1].addWidget(self.model_memory)
        self.horizontal_box[1].addWidget(self.model_memory_label_kb)
        # self.horizontal_box[1].addItem(QSpacerItem(0.46*self.WINDOW_WIDTH, 0.05*self.WINDOW_HEIGHT))
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.Loadpng)
        self.horizontal_box[2].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addWidget(self.summary)
        self.horizontal_box[3].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.project_name_label)
        self.horizontal_box[4].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addStretch()
        self.horizontal_box[5].addWidget(self.output_path_label)
        self.horizontal_box[5].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.model_path_label)
        self.horizontal_box[6].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.optimizations_label)
        self.horizontal_box[7].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[8].addStretch()
        self.horizontal_box[8].addWidget(self.pruning_label)
        self.horizontal_box[8].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[9].addStretch()
        self.horizontal_box[9].addWidget(self.quantization_label)
        self.horizontal_box[9].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[10].addStretch()
        self.horizontal_box[10].addWidget(self.data_loader_label)
        self.horizontal_box[10].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[11].addStretch()
        self.horizontal_box[11].addWidget(self.Finish)
        self.horizontal_box[11].addWidget(self.Finish_placeholder)
        self.horizontal_box[11].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[12].addWidget(self.Back)
        self.horizontal_box[12].addWidget(self.Back_Load_placeholder)
        self.horizontal_box[12].addStretch()
        self.horizontal_box[12].addWidget(self.step) 
        self.horizontal_box[12].addStretch()         
        self.horizontal_box[12].addWidget(self.Load)
        self.horizontal_box[12].addWidget(self.Back_Load_placeholder)
        self.horizontal_box[12].setAlignment(Qt.AlignBottom)
        
        
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
            