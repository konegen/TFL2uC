import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UIOptiWindow(QWidget):
    """Select a optimization algorithm. 

    This GUI window has two buttons to choose the optimazion algorithms
    pruning and quantization. The pruning factors can be passed via
    input fields, and the quantization data type via buttons.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UIOptiWindow, self).__init__(parent)

        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE       
        
        self.label = QLabel("Optimization")
        self.label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.gap = QLabel(self)
        self.gap.setFixedWidth(0.15*self.WINDOW_WIDTH)
        self.gap.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        self.gap_label = QLabel(self)
        self.gap_label.setFixedWidth(0.025*self.WINDOW_WIDTH)
        self.gap_label.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        self.button_placeholder = QLabel()
        self.button_placeholder.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.button_placeholder.setFixedHeight(0.07*self.WINDOW_HEIGHT)
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.025*self.WINDOW_HEIGHT)
        self.step.setFixedWidth(0.35*self.WINDOW_WIDTH)
        step_img = QPixmap(os.path.join('Images', 'GUI_progress_bar_Demonstrator', 'GUI_demonstrator_step_2.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)
        self.step.setScaledContents(True)
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.Back.setFixedHeight(0.05*self.WINDOW_HEIGHT)    
        
        self.Next = QPushButton(self)
        self.Next.setIcon(QIcon(os.path.join('Images', 'next_arrow.png')))
        self.Next.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.Next.setFixedHeight(0.05*self.WINDOW_HEIGHT)    
        
        self.Pruning = QPushButton(self)
        self.Pruning.setIcon(QIcon(os.path.join('Images', 'Pruning_Button.png')))
        self.Pruning.setIconSize(QSize(0.33*self.WINDOW_WIDTH, 0.33*self.WINDOW_WIDTH))
        self.Pruning.setCheckable(True)
        self.Pruning.setFixedWidth(0.35*self.WINDOW_WIDTH)
        self.Pruning.setFixedHeight(0.35*self.WINDOW_WIDTH)
        self.Pruning.setToolTip('Optimize the network through pruning. This\n'
                                'involves reducing the size of the network\n'
                                'by removing neurons from the fully connected\n'
                                'layers or feature maps from the convolution\n'
                                'layers. The pruning factors determine the\n'
                                'percentage of neurons or feature maps to\n'
                                'be removed from each layer.') 
        self.Pruning.setStyleSheet("""QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")
        
        
        self.Quantization = QPushButton(self)
        self.Quantization.setIcon(QIcon(os.path.join('Images', 'Quantization_Button.png')))
        self.Quantization.setIconSize(QSize(0.33*self.WINDOW_WIDTH, 0.33*self.WINDOW_WIDTH))
        self.Quantization.setCheckable(True)
        self.Quantization.setFixedWidth(0.35*self.WINDOW_WIDTH)
        self.Quantization.setFixedHeight(0.35*self.WINDOW_WIDTH)
        self.Quantization.setToolTip('Optimize the network through quantization.\n'
                                     'This reduces the number of bits required\n'
                                     'to represent the value of the weights.\n'
                                     'For example, a fourfold reduction of the\n'
                                     'required memory space can be achieved by\n'
                                     'converting the weights from 32-bit float\n'
                                     'values to 8-bit integer values.')
        self.Quantization.setStyleSheet("""QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")
        
        self.prun_fac = QPushButton("Factor", self)
        self.prun_fac.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.prun_fac.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.prun_fac.setCheckable(True)
        self.prun_fac.setVisible(False)
        self.prun_fac.setToolTip('For the fully connected and convolutional layers, a\n'
                                 'factor is specified in each case, which indicates\n'
                                 'the percentage of neurons or filters to be deleted\n'
                                 'from the layer.')
        self.prun_fac.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")

        self.prun_acc = QPushButton("Accuracy", self)
        self.prun_acc.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.prun_acc.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.prun_acc.setCheckable(True)
        self.prun_acc.setVisible(False)
        self.prun_acc.setToolTip('The minimum accuracy of the neural network or the\n'
                                 'loss of accuracy that may result from pruning can\n'
                                 'be specified here.')
        self.prun_acc.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")

        self.Pruning_Dense_label = QLabel("Dense layer\nfactor in %", self)
        self.Pruning_Dense_label.setStyleSheet("font: " + str(int(0.025*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.Pruning_Dense_label.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.Pruning_Dense_label.setFixedHeight(0.07*self.WINDOW_HEIGHT)
        self.Pruning_Dense_label.setAlignment(Qt.AlignCenter)
        self.Pruning_Dense_label.setVisible(False)
        
        self.Pruning_Conv_label = QLabel("Conv layer\nfactor in %", self)
        self.Pruning_Conv_label.setStyleSheet("font: " + str(int(0.025*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.Pruning_Conv_label.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.Pruning_Conv_label.setFixedHeight(0.07*self.WINDOW_HEIGHT)
        self.Pruning_Conv_label.setAlignment(Qt.AlignCenter)
        self.Pruning_Conv_label.setVisible(False)
        
        self.Pruning_Dense = QLineEdit(self)
        self.Pruning_Dense.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.Pruning_Dense.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.Pruning_Dense.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.Pruning_Dense.setAlignment(Qt.AlignCenter)
        self.Pruning_Dense.setVisible(False)

        self.Pruning_Conv = QLineEdit(self)
        self.Pruning_Conv.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.Pruning_Conv.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.Pruning_Conv.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.Pruning_Conv.setAlignment(Qt.AlignCenter)
        self.Pruning_Conv.setVisible(False)

        self.min_acc = QCheckBox('Mininmal\naccuracy', self)
        self.min_acc.setStyleSheet("font: " + str(int(0.025*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.min_acc.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.min_acc.setFixedHeight(0.07*self.WINDOW_HEIGHT)
        self.min_acc.setVisible(False)

        self.acc_loss = QCheckBox('Accuracy\nloss', self)
        self.acc_loss.setStyleSheet("font: " + str(int(0.025*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.acc_loss.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.acc_loss.setFixedHeight(0.07*self.WINDOW_HEIGHT)
        self.acc_loss.setVisible(False)
        
        self.prun_acc_label = QLabel(self)
        self.prun_acc_label.setStyleSheet("font: " + str(int(0.025*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.prun_acc_label.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.prun_acc_label.setFixedHeight(0.07*self.WINDOW_HEIGHT)
        self.prun_acc_label.setAlignment(Qt.AlignCenter)
        self.prun_acc_label.setVisible(False)

        self.prun_acc_edit = QLineEdit(self)
        self.prun_acc_edit.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.prun_acc_edit.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.prun_acc_edit.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.prun_acc_edit.setAlignment(Qt.AlignCenter)
        self.prun_acc_edit.setVisible(False)

        self.quant_int = QPushButton("int8+float32", self)
        self.quant_int.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.quant_int.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.quant_int.setCheckable(True)
        self.quant_int.setVisible(False)
        self.quant_int.setToolTip('This quantization approach converts all weights\n'
                                  'to int8 values. But the input and output still\n'
                                  'remain 32-bit float.')
        self.quant_int.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")
        
        self.quant_int_only = QPushButton("int8 only", self)
        self.quant_int_only.setFixedWidth(0.12*self.WINDOW_WIDTH)
        self.quant_int_only.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.quant_int_only.setCheckable(True)
        self.quant_int_only.setVisible(False)
        self.quant_int_only.setToolTip('This quantization approach converts all weights\n'
                                       'to int8 values. Also the input and output will\n'
                                       'be converted to 8-bit integer.')
        self.quant_int_only.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px
                           }
                           QPushButton::hover
                           {
                           background-color : rgb(10, 100, 200);
                           }""")

        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.Pruning)
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.Quantization)
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addItem(QSpacerItem(0.02*self.WINDOW_WIDTH, 0.02*self.WINDOW_HEIGHT))
        self.horizontal_box[2].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.prun_fac, 0, 0, Qt.AlignBottom)
        sublayout.addWidget(self.gap_label, 0, 1, Qt.AlignBottom)
        sublayout.addWidget(self.prun_acc, 0, 2, Qt.AlignBottom)
        sublayout.addWidget(self.gap, 0, 3, Qt.AlignBottom)
        sublayout.addWidget(self.quant_int, 0, 4, Qt.AlignBottom)
        sublayout.addWidget(self.gap_label, 0, 5, Qt.AlignBottom)
        sublayout.addWidget(self.quant_int_only, 0, 6, Qt.AlignBottom)
        sublayout.addWidget(self.Pruning_Dense_label, 1, 0, Qt.AlignBottom)
        sublayout.addWidget(self.min_acc, 1, 0, Qt.AlignBottom)
        sublayout.addWidget(self.gap_label, 1, 1, Qt.AlignCenter)
        sublayout.addWidget(self.Pruning_Conv_label, 1, 2, Qt.AlignBottom)
        sublayout.addWidget(self.acc_loss, 1, 2, Qt.AlignBottom)
        sublayout.addWidget(self.gap, 1, 3, Qt.AlignCenter)
        sublayout.addWidget(self.button_placeholder, 1, 4, Qt.AlignCenter)
        sublayout.addWidget(self.gap_label, 1, 5, Qt.AlignCenter)
        sublayout.addWidget(self.button_placeholder, 1, 6, Qt.AlignCenter)
        sublayout.addWidget(self.Pruning_Dense, 2, 0, Qt.AlignCenter)
        sublayout.addWidget(self.prun_acc_label, 2, 0, Qt.AlignCenter)
        sublayout.addWidget(self.gap_label, 2, 1, Qt.AlignCenter)
        sublayout.addWidget(self.Pruning_Conv, 2, 2, Qt.AlignCenter)
        sublayout.addWidget(self.prun_acc_edit, 2, 2, Qt.AlignCenter)
        sublayout.addWidget(self.gap, 2, 3, Qt.AlignCenter)
        sublayout.addWidget(self.button_placeholder, 2, 4, Qt.AlignCenter)
        sublayout.addWidget(self.gap_label, 2, 5, Qt.AlignCenter)
        sublayout.addWidget(self.button_placeholder, 2, 6, Qt.AlignCenter)
        sublayout.addWidget(self.button_placeholder, 3, 0, Qt.AlignCenter)
        sublayout.addWidget(self.gap_label, 3, 1, Qt.AlignCenter)
        sublayout.addWidget(self.button_placeholder, 3, 2, Qt.AlignCenter)
        sublayout.addWidget(self.gap, 3, 3, Qt.AlignCenter)
        sublayout.addWidget(self.button_placeholder, 3, 4, Qt.AlignCenter)
        sublayout.addWidget(self.gap_label, 3, 5, Qt.AlignCenter)
        sublayout.addWidget(self.button_placeholder, 3, 6, Qt.AlignCenter)
        sublayout.setAlignment(Qt.AlignCenter)
        self.horizontal_box[3].addLayout(sublayout)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1, Qt.AlignCenter)
        sublayout.addWidget(self.Next, 0, 2, Qt.AlignRight)
        self.horizontal_box[4].addLayout(sublayout)

        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)