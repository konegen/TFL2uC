import sys
import os
import matplotlib.image as mpimg
import numpy as np
import random
import cv2
from numpy.lib.stride_tricks import as_strided
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import csv
import pandas as pd
import math

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def get_output_path(self, CurWindow):
    """Get the path where the genareted Project should be stored

    A Browse window opens and you can navigate to the directory
    you wanna store the project.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    self.output_path = QFileDialog.getExistingDirectory(self, "Select the output path", os.path.expanduser('~'))
    CurWindow.output_path.setText(self.output_path)
    print(CurWindow.output_path.text())

def get_model_path(self, CurWindow):
    """Get the keras model which should be converted

    A Browse window opens and you can navigate to the keras
    model file you wanna convert to TensorFlow lite for
    microcontrollers.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    self.model_path = QFileDialog.getOpenFileName(self, "Select your model", os.path.expanduser('~'))[0]
    CurWindow.model_path.setText(self.model_path)
    print(CurWindow.model_path.text())

def get_data_loader(self, CurWindow):
    """Get the file or path to load your training data.

    A Browse window opens and you can navigate to the directory
    containing your training data. Otherwise you can select a file
    which loads your training. If the file is a CSV the 
    CSVDataloaderWindow() function is executed. 

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if "Select PATH with data" in CurWindow.dataloader_list.currentText():
        self.data_loader_path = QFileDialog.getExistingDirectory(self, "Select your trainingdata path", os.path.expanduser('~'))
    elif "Select FILE with data" in CurWindow.dataloader_list.currentText():
        self.data_loader_path = QFileDialog.getOpenFileName(self, "Select your data loader script", os.path.expanduser('~'), 'CSV(*.csv);; Python(*.py)')[0]
    CurWindow.Daten_Pfad.setText(self.data_loader_path)
    print(CurWindow.Daten_Pfad.text())

    if ".csv" in self.data_loader_path:
        print("SIE HABEN EINE CSV-DATEI AUSGEWÄHLT")
        self.CSVDataloaderWindow()
    else:
        print("KEINE CSV-DATEI")


def set_pruning(self, CurWindow):
    """Adds or removes pruning from optimization.

    If "self.optimizations" doesn't contain pruning it gets added.
    Otherwise it gets removed. Furthermore the input fields for the
    pruning factors appear or disappear.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if CurWindow.Pruning.isChecked() == True:
        if not "Pruning" in self.optimizations:
            self.optimizations.append("Pruning")
            print(self.optimizations)

        CurWindow.prun_fac.setVisible(True)
        CurWindow.prun_acc.setVisible(True)

        if self.prun_type != None:
            set_prun_type(self, self.prun_type, CurWindow, True)


        # CurWindow.Quantization.setIconSize(QSize(100, 100))
        # CurWindow.Quantization.setGeometry(540, 85, 120, 120)

    else:
        if "Pruning" in self.optimizations:
            self.optimizations.remove("Pruning")
            print(self.optimizations)
        CurWindow.prun_fac.setVisible(False)
        CurWindow.prun_acc.setVisible(False) 
        
        CurWindow.Pruning_Dense.setVisible(False)
        CurWindow.Pruning_Conv.setVisible(False)
        CurWindow.Pruning_Conv_label.setVisible(False)
        CurWindow.Pruning_Dense_label.setVisible(False)

        CurWindow.min_acc.setVisible(False)
        CurWindow.acc_loss.setVisible(False)   
        CurWindow.prun_acc_label.setVisible(False)
        CurWindow.prun_acc_edit.setVisible(False) 

        # CurWindow.Pruning.setIconSize(QSize(150, 150))
        # CurWindow.Pruning.setGeometry(120, 85, 170, 170)

def set_quantization(self, CurWindow):
    """Adds or removes quantization from optimization.

    If "self.optimizations" doesn't contain quantization it gets added.
    Otherwise it gets removed. Furthermore the buttons for the
    quantization type appear or disappear.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if CurWindow.Quantization.isChecked() == True:
        if not "Quantization" in self.optimizations:
            self.optimizations.append("Quantization")
        if self.quant_dtype != None:
            if "int8 with float fallback" in self.quant_dtype:
                CurWindow.quant_int_only.setChecked(False)
                CurWindow.quant_int.setChecked(True)
            elif "int8 only" in self.quant_dtype:
                CurWindow.quant_int_only.setChecked(True)
                CurWindow.quant_int.setChecked(False)
        CurWindow.quant_int.setVisible(True)
        CurWindow.quant_int_only.setVisible(True)

        # CurWindow.Quantization.setIconSize(QSize(100, 100))
        # CurWindow.Quantization.setGeometry(540, 85, 120, 120)

    else:
        if "Quantization" in self.optimizations:
            self.optimizations.remove("Quantization")
        CurWindow.quant_int.setChecked(False)
        CurWindow.quant_int_only.setChecked(False)
        CurWindow.quant_int.setVisible(False)
        CurWindow.quant_int_only.setVisible(False)

    print(self.optimizations)

        # CurWindow.Quantization.setIconSize(QSize(150, 150))
        # CurWindow.Quantization.setGeometry(515, 85, 170, 170)

def set_prun_type(self, prun_type, CurWindow, Pruning_button):
    """Sets the pruning type.

    Checks which button of the pruning type is pressed and
    sets it as pruning type.

    Args:
        prun_type:      Defines the pruning type.
        CurWindow:      GUI window from which the function is executed.
        Pruning_button: Was the Pruning button pressed or not
    """
    if "Factor" in prun_type:
        CurWindow.prun_acc.setChecked(False)
        if self.prun_type == None or not "Factor" in self.prun_type or Pruning_button == True:
            CurWindow.prun_fac.setChecked(True)
            self.prun_type = prun_type
            if self.prun_factor_dense == None and self.prun_factor_conv == None:
                CurWindow.Pruning_Dense.setText("10")
                CurWindow.Pruning_Conv.setText("10")
            else:
                CurWindow.Pruning_Dense.setText(str(self.prun_factor_dense))
                CurWindow.Pruning_Conv.setText(str(self.prun_factor_conv))
            CurWindow.Pruning_Dense.setVisible(True)
            CurWindow.Pruning_Conv.setVisible(True)
            CurWindow.Pruning_Conv_label.setVisible(True)
            CurWindow.Pruning_Dense_label.setVisible(True)

            CurWindow.min_acc.setVisible(False)
            CurWindow.acc_loss.setVisible(False)
            CurWindow.prun_acc_label.setVisible(False)
            CurWindow.prun_acc_edit.setVisible(False) 
        else:
            self.prun_type = None
            try:
                self.prun_factor_dense = int(CurWindow.Pruning_Dense.text())
                self.prun_factor_conv = int(CurWindow.Pruning_Conv.text())
            except:
                self.prun_factor_dense = None
                self.prun_factor_conv = None
            CurWindow.Pruning_Dense.setVisible(False)
            CurWindow.Pruning_Conv.setVisible(False)
            CurWindow.Pruning_Conv_label.setVisible(False)
            CurWindow.Pruning_Dense_label.setVisible(False)

    elif "Accuracy" in prun_type:
        CurWindow.prun_fac.setChecked(False)
        if self.prun_type == None or not "Accuracy" in self.prun_type or Pruning_button == True:
            CurWindow.prun_acc.setChecked(True)
            self.prun_type = prun_type
            
            CurWindow.min_acc.setVisible(True)
            CurWindow.acc_loss.setVisible(True)

            if self.prun_acc_type != None and "Minimal accuracy" in self.prun_acc_type:
                CurWindow.min_acc.setChecked(True)
                CurWindow.acc_loss.setChecked(False)
                CurWindow.prun_acc_label.setVisible(True)
                CurWindow.prun_acc_label.setText("Min accuracy\nto reach in %")
                CurWindow.prun_acc_edit.setVisible(True)
                CurWindow.prun_acc_edit.setText(str(self.prun_acc))

            elif self.prun_acc_type != None and  "Accuracy loss" in self.prun_acc_type:
                CurWindow.min_acc.setChecked(False)
                CurWindow.acc_loss.setChecked(True)
                CurWindow.prun_acc_label.setVisible(True)
                CurWindow.prun_acc_label.setText("Max accuracy\nloss in %")
                CurWindow.prun_acc_edit.setVisible(True)
                CurWindow.prun_acc_edit.setText(str(self.prun_acc))

            try:
                self.prun_factor_dense = int(CurWindow.Pruning_Dense.text())
                self.prun_factor_conv = int(CurWindow.Pruning_Conv.text())
            except:
                self.prun_factor_dense = None
                self.prun_factor_conv = None
            CurWindow.Pruning_Dense.setVisible(False)
            CurWindow.Pruning_Conv.setVisible(False)
            CurWindow.Pruning_Conv_label.setVisible(False)
            CurWindow.Pruning_Dense_label.setVisible(False)
        else:
            self.prun_type = None
            
            CurWindow.min_acc.setVisible(False)
            CurWindow.acc_loss.setVisible(False)
            CurWindow.prun_acc_label.setVisible(False)
            CurWindow.prun_acc_edit.setVisible(False) 

    print(self.prun_type)

def set_prun_acc_type(self, prun_type, CurWindow):
    """Sets the pruning for accuracy type.

    Sets and unsets the checked pruning for accuracy type.

    Args:
        prun_acc_type: Defines the pruning for accuracy type.
        CurWindow:     GUI window from which the function is executed.
    """
    if "Minimal accuracy" in prun_type:
        CurWindow.acc_loss.setChecked(False)
        if self.prun_acc_type == None or not "Minimal accuracy" in self.prun_acc_type:  
            self.prun_acc_type = prun_type
            CurWindow.prun_acc_label.setVisible(True)
            CurWindow.prun_acc_label.setText("Min accuracy\nto reach in %")
            CurWindow.prun_acc_edit.setVisible(True)
            CurWindow.prun_acc_edit.setText("")
            self.prun_acc = None
        else:
            self.prun_acc_type = None  
            CurWindow.prun_acc_label.setVisible(False)
            CurWindow.prun_acc_edit.setVisible(False)
    elif "Accuracy loss" in prun_type:
        CurWindow.min_acc.setChecked(False)
        if self.prun_acc_type == None or not "Accuracy loss" in self.prun_acc_type:
            self.prun_acc_type = prun_type
            CurWindow.prun_acc_label.setVisible(True)
            CurWindow.prun_acc_label.setText("Max accuracy\nloss in %")
            CurWindow.prun_acc_edit.setVisible(True)
            CurWindow.prun_acc_edit.setText("")
            self.prun_acc = None
        else:
            self.prun_acc_type = None
            CurWindow.prun_acc_label.setVisible(False)
            CurWindow.prun_acc_edit.setVisible(False)
    print(self.prun_acc_type)
        
def set_quant_dtype(self, dtype, CurWindow):
    """Sets the quantization type.

    Checks which button of the quantization type is pressed and
    sets it as quantization type.

    Args:
        dtype:     Defines the quantization type.
        CurWindow: GUI window from which the function is executed.
    """
    if "int8 with float fallback" in dtype:
        CurWindow.quant_int_only.setChecked(False)
        if CurWindow.quant_int.isChecked() == False:
            self.quant_dtype = None
        else:
            self.quant_dtype = dtype
    elif "int8 only" in dtype:
        CurWindow.quant_int.setChecked(False)
        if CurWindow.quant_int_only.isChecked() == False:
            self.quant_dtype = None
        else:
            self.quant_dtype = dtype
    print(self.quant_dtype)

def get_optimization(self, button): #Wird nirgends verwendet!
    """Returns the selected optimizations.

    Returns the selected optimizations according to the
    button of the optimizaiton type is pressed or not.

    Args:
        button: Pruning or quantization button.
    """
    if button.text() == "Pruning":
        if button.isChecked() == True:
            if not "Pruning" in self.optimizations:
                self.optimizations.append(button.text())
            # print(button.text() " is selected")
        else:
            if "Pruning" in self.optimizations:
                self.optimizations.remove(button.text())
            # print(button.text() " is deselected")

    if button.text() == "Quantization":
        if button.isChecked() == True:
            if not "Quantization" in self.optimizations:
                self.optimizations.append(button.text())
            # print(button.text() " is selected")
        else:
            if "Quantization" in self.optimizations:
                self.optimizations.remove(button.text())
            # print(button.text() " is deselected")

    print(self.optimizations)

# def set_optimizations(self, optimizations, CurWindow):
#     if "Pruning" in optimizations:
#         CurWindow.b[0].setChecked(True)

#     if "Quantization" in optimizations:
#         CurWindow.b[1].setChecked(True)

def model_pruning(self, CurWindow):
    """Starts the thread to prune the model.

    The thread for pruning the model is started. Also, the two 
    buttons of the GUI window are hidden and the thread for the 
    loading screen is started.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    CurWindow.Back.setVisible(False)
    CurWindow.Load.setVisible(False)

    CurWindow.loading_images.start()
    CurWindow.prune_model.start()

def download(self, CurWindow):
    """Starts the thread to convert the model and create the project.

    The thread for pruning the model gets terminated and the thread
    to convert the model and create the project gets started.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    try:
        CurWindow.prune_model.stop_thread()
        print("To uC start")
        CurWindow.conv_build_load.start()
    except:
        print("Error")

def terminate_thread(self, CurWindow):
    """End of converting the model and creating the project.

    Terminates the threads for pruning the model and converting the
    model and creating the project. Additionally, the "Finish" button
    becomes visible to close the GUI and the image of the loading
    screen signals the end of the process.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    try:
        print("Finish!")
        CurWindow.loading_images.stop_thread()
        CurWindow.conv_build_load.stop_thread()
        CurWindow.Finish.setVisible(True)
        CurWindow.Loadpng.setPixmap(
            QPixmap(
                os.path.join(
                    "Images", "GUI_loading_images", "GUI_load_finish.png"
                )
            )
        )
    except:
        print("Error")


def dataloader_quantization(data_loader_path, image_height, image_width, separator, csv_target_label):
    """Get Training data for quantization.

    Checks if your training data is inside a path or a file. Extracts
    the data from the directories or the file and returns it.

    Args:
        data_loader_path: Path or file of training data
        image_height:    Height of image
        image_width:     Width of image

    Returns:
        Training data which is needed for quantization.
    """
    train_images = []

    if os.path.isfile(data_loader_path):
        if ".csv" in data_loader_path:
            # Hier muss das extrahieren der Daten aus der CSV Datei implemntiert werden
            df = pd.read_csv(data_loader_path, sep=separator, header=0)

            features = df.loc[:, df.columns != csv_target_label]

            X_temp=[]
            for row in features[features.columns[0]]:
                res = row.strip('][').split(', ')
                X_temp.append([float(x) for x in res])
            X = np.asarray(X_temp, dtype=float)[..., np.newaxis]
            
            return X

        else:
            sys.path.append(os.path.dirname(data_loader_path))
            datascript = __import__(os.path.splitext(os.path.basename(data_loader_path))[0])
            x_train, _, _, _ = datascript.get_data()

        return x_train

    elif os.path.isdir(data_loader_path):

        classes = os.listdir(data_loader_path)
        print("Num classes: " + str(len(classes)))
        for folders in classes:
            if os.path.isdir(data_loader_path + "/" + folders):
                images = os.listdir(data_loader_path + "/" + folders)
            for i in range(0,int(500/len(classes))):
                rand_img = random.choice(images)
                img = mpimg.imread(data_loader_path + "/" + folders + "/" + rand_img)
                resized_image = cv2.resize(img, (image_height, image_width))
                train_images.append(resized_image)
        
        train_images = np.asarray(train_images)
        if len(train_images.shape) == 3:
            train_images = np.expand_dims(train_images, axis=3) 

        return train_images



def dataloader_pruning(data_loader_path, separator, csv_target_label, image_height, image_width, num_channels, num_classes):
    """Get data for retraining the model after pruning.

    Checks if your data is inside a path or a file. Extracts the
    data from the directories or the file. If it is a file there
    is also a check if the label is one hot encoded or not. If it
    is a path data genarators are initialized.  

    Args:
        data_loader_path: Path or file of training data
        separator:       Delimiter to use
        image_height:    Height of image
        image_width:     Width of image
        num_channels:    Number of channels of the image
        num_classes:     Number of different classes of the model

    Returns:
        If the dataloader is a file training data, the labels and
        whether the label is one hot encoded or not is returned.
        If the dataloader is a path the datagenerators for training
        and validation data is returned. Furthermore "False" is
        returned, because it is not one hot encoded. 
    """
    if os.path.isfile(data_loader_path):
        if ".csv" in data_loader_path:
            # Hier muss das extrahieren der Daten aus der CSV Datei implemntiert werden
            df = pd.read_csv(data_loader_path, sep=separator, index_col=False)

            if "First" in csv_target_label:
                X = np.array(df.iloc[:,1:].values)[..., np.newaxis]
                Y = np.array(df.iloc[:,0].values).astype(np.int8)
            else:
                X = np.array(df.iloc[:,:-1].values)[..., np.newaxis]
                Y = np.array(df.iloc[:,-1].values).astype(np.int8)

            return X, Y, False

        else:
            sys.path.append(os.path.dirname(data_loader_path))
            datascript = __import__(os.path.splitext(os.path.basename(data_loader_path))[0])
            x_train, y_train, _, _ = datascript.get_data()
            if len(y_train.shape) > 1:
                label_one_hot = True
            else:
                label_one_hot = False
                
            return x_train, y_train, label_one_hot

    elif os.path.isdir(data_loader_path):

        print(num_channels)

        # create data generator
        train_datagen = ImageDataGenerator(rescale=1.0/255.0, validation_split=0.2)
        # prepare iterators
        if num_channels == 1:
            if num_classes > 2:
                train_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode='grayscale', class_mode='sparse', batch_size=128, subset='training')
                val_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode='grayscale', class_mode='sparse', batch_size=128, subset='validation')
            else:
                train_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode='grayscale', class_mode='binary', batch_size=128, subset='training')
                val_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode='grayscale', class_mode='binary', batch_size=128, subset='validation')
        
        elif num_channels == 3:
            if num_classes > 2:
                train_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode='rgb', class_mode='sparse', batch_size=128, subset='training')
                val_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode='rgb', class_mode='sparse', batch_size=128, subset='validation')
            else:
                train_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode='rgb', class_mode='binary', batch_size=128, subset='training')
                val_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode='rgb', class_mode='binary', batch_size=128, subset='validation')

        return train_it, val_it, False



def browseCSVData(self):
    """Get the CSV file which contains your data.

    A Browse window opens and you can navigate to the CSV
    file which contains your data.
    """
    self.data_loader_path = QFileDialog.getOpenFileName(
        self, "Select your data loader script", os.path.expanduser('~'), 'CSV(*.csv)')[0]
    
    print(self.data_loader_path)

        

def previewCSVData(self, CurWindow):
    """Gives a preview of the CSV data structure.

    Read the CSV file and separate the data according the selected
    separators. The data is represented by a table. Additionally, a
    drop-down list appears where the column of the data label can
    be selected. Also the number of rows and columns of the data get
    displayed.

    Args:
        CurWindow: GUI window from which the function is executed.
    """    
    try:
    
        if self.data_loader_path != None and ".csv" in self.data_loader_path:
            self.get_separator(CurWindow)
            if not self.separator:
                df = pd.read_csv(self.data_loader_path, index_col=False)
            else:
                df = pd.read_csv(self.data_loader_path, index_col=False, sep=self.separator)
            if df.size == 0:
                return
            df.fillna('', inplace=True)
            CurWindow.table.setRowCount(df.shape[0])
            CurWindow.table.setColumnCount(df.shape[1])
            # CurWindow.table.setHorizontalHeaderLabels(df.columns)
            # returns pandas array object
            for row in df.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    # if isinstance(value, (float, int)):
                        # value = '{0:0,}'.format(value)
                    tableItem = QTableWidgetItem(str(value))
                    CurWindow.table.setItem(row[0], col_index, tableItem)

            CurWindow.table.setColumnWidth(2, 300)
            CurWindow.label_col.setVisible(True)
            CurWindow.cb_label_col.setVisible(True)

            CurWindow.numRow.setText("Number of Rows:    " + str(df.shape[0]))
            CurWindow.numCol.setText("Number of Columns: " + str(df.shape[1]))
        
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
                
            msg.setText("The selected file is no CSV.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
    
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
            
        msg.setText("This separator cannot be used")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        


def loadCSVData(self, CurWindow):
    """Stores the target column of the CSV file and closes the window.
    """
    if CurWindow.cb_label_col.isVisible() == True:
        self.csv_target_label = CurWindow.cb_label_col.currentText()
        CurWindow.close()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
            
        msg.setText("You have to preview the data before you can load it.")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        return



def get_separator(self, CurWindow):
    """Read the selected separators.

    Checks if the different separator check boxes are checked or
    not. If a checkbox is selected, the corresponding separator is 
    written to the variable "self.separator".

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    self.separator = None

    if CurWindow.cbTab.isChecked():
        if self.separator == None:
            self.separator = r'\t'
        else:
            self.separator += r'|\t'
    if CurWindow.cbSemicolon.isChecked():
        if self.separator == None:
            self.separator = ';'
        else:
            self.separator += '|;'
    if CurWindow.cbComma.isChecked():
        if self.separator == None:
            self.separator = ','
        else:
            self.separator += '|,'
    if CurWindow.cbSpace.isChecked():
        if self.separator == None:
            self.separator = r'\s+'
        else:
            self.separator += r'|\s+'
    if CurWindow.cbOther.isChecked():
        if self.separator == None:
            self.separator = CurWindow.other_separator.text()
        else:
            self.separator += '|' + CurWindow.other_separator.text()
        
    print(self.separator)



class ThresholdCallback(tf.keras.callbacks.Callback):
    """Custom callback for model training.

    This is a custom callback function. You can define an accuracy threshold
    value when the model training should be stopped.

    Attributes:
        threshold: Accuracy value to stop training.
    """

    def __init__(self, threshold):
        super(ThresholdCallback, self).__init__()
        self.threshold = threshold

    def on_epoch_end(self, epoch, logs=None): 
        val_acc = logs["val_accuracy"]        
        if val_acc >= self.threshold:
            self.model.stop_training = True