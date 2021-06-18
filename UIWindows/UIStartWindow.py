import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UIStartWindow(QWidget):
    """Select project name, output path and model path. 

    This GUI window has an input field and two buttons to pass
    project name, output path and model path.
    """
    def __init__(self, FONT_STYLE, parent=None):
        super(UIStartWindow, self).__init__(parent)
        
        self.FONT_STYLE = FONT_STYLE       
        
        self.project_name_label = QLabel("Projectname:")
        self.project_name_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        
        self.Modell_einlesen_label = QLabel("Keras model:")
        self.Modell_einlesen_label.setStyleSheet("font: 12pt " + FONT_STYLE)     

        self.Modelpng = QLabel(self)
        Modelimg = QPixmap(os.path.join('Images', 'network.png'))
        Modelimg= Modelimg.scaledToWidth(150)
        self.Modelpng.setPixmap(Modelimg)
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar_Demonstrator', 'GUI_demonstrator_step_1.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Abstand_oben = QLabel()
        self.Abstand_oben.setFixedHeight(20)
        
        self.Abstand_unten = QLabel()
        self.Abstand_unten.setFixedHeight(50)
        
        self.project_name = QLineEdit()
        self.project_name.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.project_name.setFixedWidth(200)
        
        self.model_path = QLabel("")
        self.model_path.setFixedWidth(300)
        self.model_path.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.model_path.setAlignment(Qt.AlignCenter)
        
        self.output_path = QLabel("")
        self.output_path.setFixedWidth(300)
        self.output_path.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.output_path.setAlignment(Qt.AlignCenter)
        
        self.output_path_Browse = QPushButton(" Output path... ", self)
        self.output_path_Browse.setToolTip('...')
        self.output_path_Browse.setStyleSheet("""QPushButton {
                           font: 12pt """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""")  
        
        self.read_model_browse = QPushButton(" Select Model... ", self)
        self.read_model_browse.setToolTip('...')
        self.read_model_browse.setStyleSheet("""QPushButton {
                           font: 12pt """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 

        self.Next = QPushButton(self)
        self.Next.setIcon(QIcon(os.path.join('Images', 'next_arrow.png')))
        self.Next.setIconSize(QSize(25, 25))
        self.Next.setFixedHeight(30)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addWidget(self.project_name_label)
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.project_name)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Abstand_oben)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.output_path)
        self.horizontal_box[3].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addWidget(self.output_path_Browse)
        self.horizontal_box[4].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addWidget(self.Abstand_oben)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.Modell_einlesen_label)
        self.horizontal_box[6].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.Modelpng)
        self.horizontal_box[7].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[8].addStretch()
        self.horizontal_box[8].addWidget(self.model_path)
        self.horizontal_box[8].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[9].addStretch()
        self.horizontal_box[9].addWidget(self.read_model_browse)
        self.horizontal_box[9].addStretch()
    
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[10].addWidget(self.Abstand_unten)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Abstand_oben, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.Schritt, 0, 1)
        sublayout.addWidget(self.Next, 0, 2, Qt.AlignRight)
        self.horizontal_box[11].addLayout(sublayout)
        self.horizontal_box[11].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)