import os
import ntpath
import pathlib

from Auto_TF_to_uC.convert_keras_to_cc import *
from Auto_TF_to_uC.write_files_uc import *


def convert_and_write(Keras_model_dir, project_name, output_path, optimizations, data_loader_path, quant_dtype, separator, csv_target_label, model_memory):
    """
    A keras model get's converted into a C++ model, the project directory is created
    and all files that are needed to compile the project get generated.
    
    Args: 
        Keras_model_dir:  Path of the keras model
        project_name:     Name of the project which should be generated
        output_path:      Directory where the project should be generated
        optimization:     Selected optimization algorithms
        data_loader_path: Path of the folder or file with the training data
        quant_dtype:      Data type to quantize to
        separator:        Separator for reading a CSV file
        csv_target_label: Target label from the CSV file
        model_memory:     Preallocate a certain amount of memory for input, 
                          output, and intermediate arrays in kilobytes
    """   
    converted_model_dir = str(pathlib.Path(__file__).parent.absolute()) + "/Converted_model_files/"
    model_name = ntpath.basename(Keras_model_dir)
    model_name,_ = os.path.splitext(model_name)
    model_input_neurons = 1
    
    project_dir = create_project_dir(project_name, output_path, converted_model_dir, model_name)
    
    
    model_input_shape, model_output_neurons = convert_model_to_tflite(Keras_model_dir, project_dir, model_name, optimizations, data_loader_path, quant_dtype, separator, csv_target_label)
    convert_model_to_cpp(converted_model_dir, model_name, project_dir)
    
    for i in range(1,len(model_input_shape)):
        model_input_neurons = model_input_neurons * model_input_shape[i]
    
    
    main_functions(project_dir, model_name, model_input_neurons, model_output_neurons, quant_dtype, model_memory)
    TensorFlow_library(project_dir)
    if 'Pruning' in optimizations:
        pruned_keras_model(Keras_model_dir, project_dir, model_name)
        os.remove(Keras_model_dir)