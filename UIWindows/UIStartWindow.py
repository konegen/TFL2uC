import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class UIStartWindow(QWidget):
    def __init__(self, FONT_STYLE, parent=None):
        super(UIStartWindow, self).__init__(parent)
        
        self.FONT_STYLE = FONT_STYLE       
        
        self.Projekt_Name_label = QLabel("Projectname:")
        self.Projekt_Name_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        
        self.Modell_einlesen_label = QLabel("Keras model:")
        self.Modell_einlesen_label.setStyleSheet("font: 12pt " + FONT_STYLE)     

        self.Modelpng = QLabel(self)
        Modelimg = QPixmap(os.path.join('Images', 'network.png'))
        Modelimg= Modelimg.scaledToWidth(150)
        self.Modelpng.setPixmap(Modelimg)
        
        self.Daten_label = QLabel("Training data:")
        self.Daten_label.setStyleSheet("font: 12pt " + FONT_STYLE)
        
        self.Datapng = QLabel(self)
        Dataimg = QPixmap(os.path.join('Images', 'Database.png'))
        Dataimg= Dataimg.scaledToWidth(150)
        self.Datapng.setPixmap(Dataimg)
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('Images', 'GUI_progress_bar_Demonstrator', 'GUI_demonstrator_step_1.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Abstand_oben = QLabel()
        self.Abstand_oben.setFixedHeight(20)
        
        self.Abstand_unten = QLabel()
        self.Abstand_unten.setFixedHeight(50)
        
        self.Projekt_Name = QLineEdit()
        self.Projekt_Name.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.Projekt_Name.setFixedWidth(200)
        
        self.Model_Pfad = QLabel("")
        self.Model_Pfad.setFixedWidth(300)
        self.Model_Pfad.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.Model_Pfad.setAlignment(Qt.AlignCenter)
        
        self.Output_Pfad = QLabel("")
        self.Output_Pfad.setFixedWidth(300)
        self.Output_Pfad.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.Output_Pfad.setAlignment(Qt.AlignCenter)
        
        self.Daten_Pfad = QLabel("")
        self.Daten_Pfad.setFixedWidth(300)
        self.Daten_Pfad.setStyleSheet("font: 11pt " + FONT_STYLE)
        self.Daten_Pfad.setAlignment(Qt.AlignCenter)

        self.dataloader_list = QComboBox()
        self.dataloader_list.setFixedWidth(170)
        self.dataloader_list.addItems(["Select PATH with data", "Select SCRIPT with data"])

        self.Abstand_dataloader_list = QLabel("")
        self.Abstand_dataloader_list.setFixedWidth(170)
        
        self.Output_Pfad_Browse = QPushButton(" Output path... ", self)
        self.Output_Pfad_Browse.setToolTip('...')
        self.Output_Pfad_Browse.setStyleSheet("""QPushButton {
                           font: 12pt """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""")  
        
        self.Modell_einlesen_Browse = QPushButton(" Select Model... ", self)
        self.Modell_einlesen_Browse.setToolTip('...')
        self.Modell_einlesen_Browse.setStyleSheet("""QPushButton {
                           font: 12pt """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 
        
        self.Daten_einlesen_Browse = QPushButton(" Select Data... ", self)
        self.Daten_einlesen_Browse.setToolTip('...')
        self.Daten_einlesen_Browse.setStyleSheet("""QPushButton {
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
        self.horizontal_box[0].addWidget(self.Projekt_Name_label)
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.Projekt_Name)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Abstand_oben)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.Output_Pfad)
        self.horizontal_box[3].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addWidget(self.Output_Pfad_Browse)
        self.horizontal_box[4].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addWidget(self.Abstand_oben)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.Modell_einlesen_label)
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.Daten_label)
        self.horizontal_box[6].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.Modelpng)
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.Datapng)
        self.horizontal_box[7].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[8].addStretch()
        self.horizontal_box[8].addWidget(self.Model_Pfad)
        self.horizontal_box[8].addStretch()
        self.horizontal_box[8].addStretch()
        self.horizontal_box[8].addWidget(self.Daten_Pfad)
        self.horizontal_box[8].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[9].addStretch()
        self.horizontal_box[9].addWidget(self.Abstand_dataloader_list)
        self.horizontal_box[9].addStretch()
        self.horizontal_box[9].addStretch()
        self.horizontal_box[9].addWidget(self.dataloader_list)
        self.horizontal_box[9].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[10].addStretch()
        self.horizontal_box[10].addWidget(self.Modell_einlesen_Browse)
        self.horizontal_box[10].addStretch()
        self.horizontal_box[10].addStretch()
        self.horizontal_box[10].addWidget(self.Daten_einlesen_Browse)
        self.horizontal_box[10].addStretch()
    
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[11].addWidget(self.Abstand_unten)
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.Abstand_oben, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.Schritt, 0, 1)
        sublayout.addWidget(self.Next, 0, 2, Qt.AlignRight)
        self.horizontal_box[12].addLayout(sublayout)
        self.horizontal_box[12].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)