import os
import sys
import tensorflow as tf
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from pruning import prune_model
from GUI._Helper import dataloader_pruning


class Prune_model(QThread):
    
    request_signal = pyqtSignal()
    
    def __init__(self, datascript_path, model_path, prun_factor_dense, prun_factor_conv, optimizations):
        QThread.__init__(self)
        self.datascript_path = datascript_path
        self.model_path = model_path
        self.prun_factor_dense = prun_factor_dense
        self.prun_factor_conv = prun_factor_conv
        self.optimizations = optimizations
        

    def run(self):
        if 'Pruning' in self.optimizations:
            model = tf.keras.models.load_model(self.model_path)

            train_it, val_it, num_classes = dataloader_pruning(self.datascript_path, model.input.shape[1], model.input.shape[2], model.input.shape[3])
            pruned_model = prune_model(self.model_path, self.prun_factor_dense, self.prun_factor_conv, metric='L1',comp=None, num_classes=num_classes)
            
            train_epochs = 10
            callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
            # fit model
            pruned_model.fit_generator(train_it, steps_per_epoch=len(train_it),
                validation_data=val_it, validation_steps=len(val_it), epochs=train_epochs, callbacks=[callback])
            pruned_model.save(str(self.model_path[:-3]) + '_pruned.h5', include_optimizer=False)
        self.request_signal.emit()
        
    def stop_thread(self):
        self.terminate()