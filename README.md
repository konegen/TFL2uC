# TFL2uC

Automated optimization of TensorFlow models and conversion of them to a TensorFlow Lite C++ model.



## Table of contents
- [Description](#Description)
- [Installation](#Installation)
- [Usage](#Usage)
- [License](#License)



## Description
The execution of neural networks created with TensorFlow is not readily available for microcontrollers. Currently, the porting steps to run a TensorFlow model on a microcontroller have to be done manually. These steps are automated by "TensorFlow Lite to microcontroller" (TFL2uC), so that the model can be integrated into a C++ project. Furthermore, it is possible to apply the optimization algorithms pruning and quantization to the model. For an easy use of the tool, it is realized with a GUI.

The storage capacity of microcontrollers is only in the kilobyte to megabyte range, which means that large neural networks cannot be implemented on microcontrollers. To reduce the memory requirements of a neural network, the optimization algorithms pruning and quantization can be applied in TFL2uC. Pruning deletes single neurons or filters from neural networks. Quantization converts the network parameters of a neural network from 32-bit float values to 8-bit integer values. This implemented optmization algorithms reduces the memory requirements of the model and speeds up the inference.

The figure below shows the basic pipeline of TFL2uC. At the beginning, a TensorFlow model is trained on a computer. The trained model is then passed to the tool. In this tool the neural network can be optimized by pruning or quantization. In this case, the model has to be retrained again with previously transferred training data. Next, the (optimized) model is converted into a TensorFlow Lite C++ model. In addition, a project folder is created which contains the TensorFlow Lite C++ model, the files to load and run the model, and the TensorFlow Lite library. These can then be included in a C++ project and executed on a microcontroller.

<p align="center">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/Tool_Pipeline.png" width="75%" height="75%">
</p>



## Installation
TFL2uC was developed on **Windows 10** and tested using **Python v.3.7.10** and **pip v.21.0.1**.
All other frameworks needed to use TFL2uC are located in the **requirements.txt** file. These can be installed as follows:
```
pip install -r requirements.txt
```

If **Ubuntu** is used, the following must also be installed:
```
sudo apt-get install python3-pyqt5 -y
sudo apt-get install pyqt5-dev-tools -y
sudo apt-get install qttools5-dev-tools -y
```



## Usage
To start TFL2uC, the TFL2uC.py file is executed. </br>Afterwards the fist window of the GUI will be opened. In the first window the project name, the output path and the neural network to be converted are passed.

<p align="center">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/GUI_windows/GUI_window_1.PNG" width="45%" height="45%">
</p>


In the second window of the GUI, the optimization algorithms pruning and quantization can be selected. It is important to know that only for fully connected and convolutional layers the pruning algorithm can be applied.

<p align="center">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/GUI_windows/GUI_window_2.PNG" width="45%" height="45%">
</p>

If you select pruning, you can choose between two options:
- Factor: For the fully connected and convolutional layers, a factor is specified in each case, which indicates the percentage of neurons or filters to be deleted from the layer.

<p align="center">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/GUI_windows/GUI_window_2a.PNG" width="45%" height="45%">
</p>

- Accuracy: The minimum accuracy of the neural network or the loss of accuracy that may result from pruning can be specified here.

<p align="center">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/GUI_windows/GUI_window_2b.PNG" width="45%" height="45%">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/GUI_windows/GUI_window_2c.PNG" width="45%" height="45%">
</p>

If quantization is selected, you can choose between two options:
- int8 + float32: This quantization approach converts all weights to int8 values. But the input and output still remain 32-bit float.
- int8 only: All weights get converted to int8 values. Also the input and output will be converted to 8-bit integer. When executing the net on a microcontroller later, the input values of the model must be passed as signed int8 values. Also the output values are returned as signed int8 values.

<p align="center">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/GUI_windows/GUI_window_2d.PNG" width="45%" height="45%">
</p>


The next window appears only if at least one optimization algorithm has been selected. In this window the training data are selected which the neural network requires for the optimization. The data can be transferred in different ways:
- Path: Images are to be used as training data. In the given path there are subfolders containing the name of the different classes of the neural network and the corresponding images.
- File (CSV file): The data is stored in a CSV file.
- File (Python file): The data is loaded and returned in a Python script. Here it is important that the Python script contains the function get_data() with the return values x_train, y_train, x_test, y_test (training data, training label, test data, test label). The return values here are Numpy arrays.

<p align="center">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/GUI_windows/GUI_window_3.PNG" width="45%" height="45%">
</p>

If a CSV file is selected the CSV dataloader window opens. With the browse button a new CSV file can be selected again. By using the different separators, it is possible to define how the data is separated. The Preview button shows an overview of how the data will look with the selected settings. In addition, the label of each data series must be specified. Here it is possible to set the label to the first or the last position of a data series. In addition, the number of rows and columns in the data set is displayed. If all settings are correct, the settings can be taken over for the later optimization via the button Load data.

<p align="center">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/GUI_windows/GUI_window_3a.PNG" width="45%" height="45%">
</p>


In the last window of the GUI, the amount of memory for the input, output, and intermediate arrays of the neural network on the microcontroller must be specified. In addition, an overview of all selected parameters is displayed here. The button in the lower right corner starts the process of the conversion.

<p align="center">
<img src="https://github.com/konegen/TFL2uC/blob/main/Images/GUI_windows/GUI_window_4.PNG" width="45%" height="45%">
</p>



## License
Code released under the [Apache-2.0 License](LICENSE).