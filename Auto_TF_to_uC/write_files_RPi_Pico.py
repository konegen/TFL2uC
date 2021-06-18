import os
import fileinput
import shutil
import pathlib


def create_project_dir(project_name, output_path):
    """
    Creates a directory where all files of the Raspberry Pi Pico 
    project will be stored.
    
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
        os.mkdir(project_dir + "/build")
        
    return project_dir
        

def CMakeLists(project_dir, project_name, model_name):
    """
    Creates the CMakeLists of the project.
    """    
    
    with open(project_dir + project_name + "CMakeLists", "w") as f:
        f.write('set(BinName "' + project_name + '")\n'
                'add_executable(${BinName}\n'
                '	' + model_name + '.cpp\n'
                '	' + model_name + '.h\n'
                '	Main.cpp\n'
                ')\n'
                '\n'
                'pico_enable_stdio_usb(${BinName} 1)\n'
                'pico_enable_stdio_uart(${BinName} 1)\n'
                '\n'
                'target_link_libraries(${BinName}\n'
                '	pico_stdlib\n'
                '	hardware_spi\n'
                '	pico-tflmicro\n'
                ')\n'
                '\n'
                'pico_add_extra_outputs(${BinName})\n')


def main_functions(project_dir, project_name, model_name, model_input_neurons, model_output_neurons, model_input_dtype):
    """
    The script which loads and executes the model is created
    """    
     
    with open(project_dir + project_name + "Main.cc", "w") as f:

        f.write('/*** Include ***/\n'
                '#include <cstdint>\n'
                '#include <cstdio>\n'
                '#include <cstring>\n'
                '\n'
                '#include "arducam.h"\n'
                '#include "pico/stdlib.h"\n'
                '\n'
                '#include "tensorflow/lite/micro/all_ops_resolver.h"\n'
                '#include "tensorflow/lite/micro/micro_error_reporter.h"\n'
                '#include "tensorflow/lite/micro/micro_interpreter.h"\n'
                '#include "tensorflow/lite/schema/schema_generated.h"\n'
                '#include "tensorflow/lite/version.h"\n'
                '\n'
                '#include "' + model_name + '.h"\n'
                '\n'
                '#include "input_data.h"\n'
                '#include "image_provider.h"\n'
                '\n'
                '#include "model_settings.h"\n'
                '\n'
                'char label_pred[10];\n'
                '\n'
                'char buffer[50];\n'
                '\n'
                '// Globals, used for compatibility with Arduino-style sketches.\n'
                'namespace {\n'
                'tflite::ErrorReporter* error_reporter = nullptr;\n'
                'const tflite::Model* model = nullptr;\n'
                'tflite::MicroInterpreter* interpreter = nullptr;\n'
                'TfLiteTensor* input = nullptr;\n'
                'TfLiteTensor* output = nullptr;\n'
                '\n'
                'constexpr int kTensorArenaSize = 150 * 1024;\n'
                'uint8_t tensor_arena[kTensorArenaSize];\n'
                '}  // namespace\n'
                '\n'
                '// The name of this function is important for Arduino compatibility.\n'
                '\n'
                '\n'
                'void setup();\n'
                'void loop();\n'
                '\n'
                '\n'
                'int main() {\n'
                '    stdio_init_all();\n'
                '    sleep_ms(1000);		// wait until UART connected\n'
                '\n'
                '    setup();\n'
                '\n'
                '    while(1) {\n'
                '        loop();\n'
                '    }\n'
                '}\n'
                '\n'
                '\n'
                '\n'
                'void setup() {\n'
                '\n'
                '    // Set up logging. Google style is to avoid globals or statics because of\n'
                '    // lifetime uncertainty, but since this has a trivial destructor it is okay.\n'
                '    // NOLINTNEXTLINE(runtime-global-variables)\n'
                '    static tflite::MicroErrorReporter micro_error_reporter;\n'
                '    error_reporter = &micro_error_reporter;\n'
                '\n'
                '    // Map the model into a usable data structure. This does not involve any\n'
                '    // copying or parsing, it is a very lightweight operation.\n'
                '\n'
                '    model = tflite::GetModel(' + model_name + '_tflite);\n'
                '\n'
                '    if (model->version() != TFLITE_SCHEMA_VERSION) {\n'
                '    TF_LITE_REPORT_ERROR(error_reporter,\n'
                '                        "Model provided is schema version %d not equal "\n'
                '                        "to supported version %d.",\n'
                '                        model->version(), TFLITE_SCHEMA_VERSION);\n'
                '    return;\n'
                '    }\n'
                '\n'
                '    // This pulls in all the operation implementations we need.\n'
                '    // NOLINTNEXTLINE(runtime-global-variables)\n'
                '    static tflite::AllOpsResolver resolver;\n'
                '\n'
                '    // Build an interpreter to run the model with.\n'
                '    static tflite::MicroInterpreter static_interpreter(\n'
                '    model, resolver, tensor_arena, kTensorArenaSize, error_reporter);\n'
                '    interpreter = &static_interpreter;\n'
                '\n'
                '    // Allocate memory from the tensor_arena for the model tensors.\n'
                '    TfLiteStatus allocate_status = interpreter->AllocateTensors();\n'
                '    if (allocate_status != kTfLiteOk) {\n'
                '    TF_LITE_REPORT_ERROR(error_reporter, "AllocateTensors() failed");\n'
                '    return;\n'
                '    }\n'
                '\n'
                '    // Obtain pointers to the model input and output tensors.\n'
                '    input = interpreter->input(0);\n'
                '    output = interpreter->output(0);\n'
                '}\n'
                '\n'
                '\n'
                '// The name of this function is important for Arduino compatibility.\n'
                'void loop() {\n'
                '\n'
                '    // Get image from provider.\n'
                '    if (kTfLiteOk != GetImage(error_reporter, kNumCols, kNumRows, kNumChannels,\n'
                '                            input->data.f)) {\n'
                '    TF_LITE_REPORT_ERROR(error_reporter, "Image capture failed.");\n'
                '    }\n'
                '\n'
                '    // Run the model on this input and make sure it succeeds.\n'
                '    if (kTfLiteOk != interpreter->Invoke()) {\n'
                '    TF_LITE_REPORT_ERROR(error_reporter, "Invoke failed.");\n'
                '    }\n'
                '\n'
                '    float current = output->data.f[0];\n'
                '\n'
                '    if(current < 0.3) {\n'
                '    sprintf(label_pred, "Cat");\n'
                '    }\n'
                '    else if(current > 0.7) {\n'
                '    sprintf(label_pred, "Dog");\n'
                '    }\n'
                '    else {\n'
                '    sprintf(label_pred, "Nothing");\n'
                '    }\n'
                '\n'
                '    printf("Prediction score: %.2f\n", current);\n'
                '    printf("It is a %s\n\n", label_pred);\n'
                '\n'
                '}\n')
   

def TensorFlow_library(project_dir):
    """
    Creates the TensorFlow library with all necessary files in the project directory.
    
    Args: 
        project_dir: Path of the project directory where the file should be created
            
    Return: 
        ---
    """    
    
    if not os.path.exists(project_dir + "/pico-tflmicro"):
        shutil.copytree(str(pathlib.Path(__file__).parent.absolute()) + "Templates/Raspberry-Pi/pico-tflmicro", project_dir + "/pico-tflmicro")


def Pico_sdk(project_dir):
    if not os.path.exists(project_dir + "/pico-sdk"):
        shutil.copytree(str(pathlib.Path(__file__).parent.absolute()) + "Templates/Raspberry-Pi/pico-sdk", project_dir + "/pico-sdk")
    shutil.copyfile(str(pathlib.Path(__file__).parent.absolute()) + "Templates/pico_sdk_import.cmake", project_dir + "/pico_sdk_import.cmake")