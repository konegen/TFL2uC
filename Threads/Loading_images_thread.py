import time
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Loading_images(QThread):
    """Loading screen thread.

    Attributes:
        Loadpng:     The image which is represented on the "LoadWindow"
        loading_img: The different images representing the loadingscreen
    """
    
    def __init__(self, Loadpng):
        QThread.__init__(self)
        self.Loadpng = Loadpng
        self.loading_img = 0

    def run(self):
        """Activates the thread

        Changes the image of the loading screen every 0.75 seconds.
        """          
            
        while(self.isRunning()):
            
            if self.loading_img < 15:
                self.loading_img += 1
            else:
                self.loading_img = 1
            
            time.sleep(0.75)
            
            self.Loadpng.setPixmap(QPixmap(os.path.join('Images','GUI_loading_images', 'GUI_load_' + str(self.loading_img) + '.png')))
            
        
    def stop_thread(self):
        """Ends the thread
        """
        self.terminate()