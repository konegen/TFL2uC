import os
import fileinput
import shutil
import pathlib


def create_project_dir(project_name, output_path):
    """
    Creates a directory where all files of the project will be stored.
    
    Args: 
        project_name: Name of the project which should be generated
        output_path: Directory where the project should be generated
            
    Return: 
        project_dir: Path of the project directory
    """    
    
    path = output_path
    project_dir = path + "/" + project_name
    
    if not os.path.exists(path):
        os.mkdir(path)
        
    if not os.path.exists(project_dir):
        os.mkdir(project_dir)
        os.mkdir(project_dir + "/src")
        os.mkdir(project_dir + "/inc")

    if not os.path.exists(project_dir + "/compiled_files/"):
        os.mkdir(project_dir + "/compiled_files/")
        
    return project_dir
        

def main_cc(project_dir):
    """
    Creates the main file which execute the model by starting the microcontroller.
    
    Args: 
        project_dir: Path of the project directory where the file should be created
            
    Return: 
        ---
    """    
    
    with open(project_dir + "/src/main.cc", "w") as f:
        f.write('#include "./../lcd/inc/lcd_exe.h"\n'
                '\n'
                'int main(int argc, char* argv[]) {\n'
                '  loop();\n'
                '}\n')


def main_functions(project_dir, model_name, model_input_neurons, model_output_neurons, model_input_dtype):
    """
    The script which loads and executes the model is created
    
    Args: 
        project_dir: Path of the project directory where the file should be created
        model_name: Name of the model
        model_input_neurons: Number of neurons in the input layer of the model
        model_output_neurons: Number of neurons in the output layer of the model
        model_input_dtype: Dtype of the inputdata of the model
            
    Return: 
        ---
    """    
     
    with open(project_dir + "/src/TF_Lite_exe.cc", "w") as f:

        f.write('#include "./../inc/TF_Lite_exe.h"\n'
                '\n'
                "char pred_labels[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};\n"
                '\n'
                'namespace {\n'
                '// Create an area of memory to use for input, output, and intermediate arrays.\n'
                'constexpr int kTensorArenaSize = 170 * 1024;\n'
                'uint8_t tensor_arena[kTensorArenaSize];\n'
                '\n'
                'tflite::ErrorReporter* error_reporter = nullptr;\n'
                'const tflite::Model* model = nullptr;\n'
                'tflite::MicroInterpreter* interpreter = nullptr;\n'
                'TfLiteTensor* input = nullptr;\n'
                'TfLiteTensor* output = nullptr;\n'
                '}\n'
                '\n'
                'void setup() {\n'
                '  static tflite::MicroErrorReporter micro_error_reporter;\n'
                '  error_reporter = &micro_error_reporter;\n'
                '\n'
                "  // Map the model into a usable data structure.\n"
                '  model = tflite::GetModel(' + model_name + '_tflite);\n'
                '  if (model->version() != TFLITE_SCHEMA_VERSION) {\n'
                '    error_reporter->Report(\n'
                '        "Model provided is schema version %d not equal "\n'
                '        "to supported version %d.",\n'
                '        model->version(), TFLITE_SCHEMA_VERSION);\n'
                '    return;\n'
                '  }\n'
                '\n'
                '  // This pulls in all the operation implementations we need.\n'
                '  static tflite::ops::micro::AllOpsResolver resolver;\n'
                '\n'
                '  // Build an interpreter to run the model with.\n'
                '  static tflite::MicroInterpreter static_interpreter(\n'
                '      model, resolver, tensor_arena, kTensorArenaSize, error_reporter);\n'
                '  interpreter = &static_interpreter;\n'
                '\n'
                "  // Allocate memory from the tensor_arena for the model's tensors.\n"
                '  TfLiteStatus allocate_status = interpreter->AllocateTensors();\n'
                '  if (allocate_status != kTfLiteOk) {\n'
                '    error_reporter->Report("AllocateTensors() failed");\n'
                '    return;\n'
                '  }\n'
                '\n'
                "  // Obtain pointers to the model's input and output tensors.\n"
                '  input = interpreter->input(0);\n'
                '  output = interpreter->output(0);\n'
                '}\n'
                '\n'
                'void model_execute(float *input_im, char *label_pred_1, float *acc_pred_1, char *label_pred_2, float *acc_pred_2, char *label_pred_3, float *acc_pred_3) {\n'
                'for (int i = 0; i < ' + str(model_input_neurons) + '; ++i) {\n'
                '  input->data.f[i] = *input_im;\n'
                '  input_im++;\n'
                '}\n'
                '\n'
                '// Run inference, and report any error\n'
                'TfLiteStatus invoke_status = interpreter->Invoke();\n'
                'if (invoke_status != kTfLiteOk) {\n'
                '  error_reporter->Report("Error by invoking interpreter'r"\n"'");\n'
                '  return;\n'
                '}\n'
                '\n'
                '*acc_pred_1 = 0;\n'
                '*acc_pred_2 = 0;\n'
                '*acc_pred_3 = 0;\n'
                '\n'
                'for (int i = 0; i < ' + str(model_output_neurons) + '; ++i) {\n'
                '      float current = output->data.f[i];\n'
                '      error_reporter->Report("Current %d: %f'r"\n"'", i+1, current);\n'
                '      if(current > *acc_pred_1) {\n'
                '        *acc_pred_3 = *acc_pred_2;\n'
                '      	 *label_pred_3 = *label_pred_2;\n'
                '\n'
                '		*acc_pred_2 = *acc_pred_1;\n'
                '		*label_pred_2 = *label_pred_1;\n'
                '\n '     
                '        *acc_pred_1 = current;\n'
                '		*label_pred_1 = pred_labels[i];\n'
                '      }\n'
                '      else if(current > *acc_pred_2) {\n'
                '        *acc_pred_3 = *acc_pred_2;\n'
                '		*label_pred_3 = *label_pred_2;\n'
                '\n'
                '        *acc_pred_2 = current;\n'
                '		*label_pred_2 = pred_labels[i];\n'
                '	  }\n'
                '      else if(current > *acc_pred_3) {\n'
                '        *acc_pred_3 = current;\n'
                '		 *label_pred_3 = pred_labels[i];\n'
                '	  }\n'
                '}\n'
                '\n'  
                '}\n')
                
                          
    with open(project_dir + "/inc/TF_Lite_exe.h", "w") as f:
        f.write('#include "./' + model_name + '_data.h"\n'
                '#include "./../../../TensorFlow_library/tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h"\n'
                '#include "./../../../TensorFlow_library/tensorflow/lite/experimental/micro/micro_error_reporter.h"\n'
                '#include "./../../../TensorFlow_library/tensorflow/lite/experimental/micro/micro_interpreter.h"\n'
                '#include "./../../../TensorFlow_library/tensorflow/lite/schema/schema_generated.h"\n'
                '#include "./../../../TensorFlow_library/tensorflow/lite/version.h"\n'
                '\n'
                '\n'
                'void setup();\n'
                'void model_execute(float *, char *, float *, char *, float *, char *, float *);\n')
   

def TensorFlow_library(project_dir):
    """
    Creates the TensorFlow library with all necessary files in the project directory.
    
    Args: 
        project_dir: Path of the project directory where the file should be created
            
    Return: 
        ---
    """    
    
    if not os.path.exists(project_dir + "/TensorFlow_library"):
        shutil.copytree(str(pathlib.Path(__file__).parent.absolute()) + "/TensorFlow_library", project_dir + "/TensorFlow_library")
        
        
def STM32F7_library(project_dir):
    """
    Creates the STM32F7 library with all necessary files in the project directory.
    
    Args: 
        project_dir: Path of the project directory where the file should be created
            
    Return: 
        ---
    """    
    
    if not os.path.exists(project_dir + "/STM32F7_library"):
        shutil.copytree(str(pathlib.Path(__file__).parent.absolute()) + "/STM32F7_library", project_dir + "/STM32F7_library")
    
    
def compile_file(project_dir, project_name):
    """
    Creates the bash script which compiles the project and loads the binary file to the microcontroller
    
    Args: 
        project_dir: Path of the project directory where the file should be created
        project_name: Name of the project
            
    Return: 
        ---
    """    
    
    template = str(pathlib.Path(__file__).parent.absolute()) + '/templates/main_project_STM.sh'
    target = project_dir + '/main_' + project_name + '.sh'
    
    shutil.copy(template, target)
      
    
def Makefile_STM(project_dir, project_name):
    """
    Creates the Makefile which compiles the project
    
    Args: 
        project_dir: Path of the project directory where the file should be created
        project_name: Name of the project
            
    Return: 
        ---
    """    
    
    template = str(pathlib.Path(__file__).parent.absolute()) + '/templates/Makefile_project_STM'
    target = project_dir + '/Makefile'
    
    shutil.copy(template, target)
    
    with fileinput.FileInput(target, inplace=True) as file:
        for line in file:
            print(line.replace("###PROJECT_NAME###", project_name), end='')


