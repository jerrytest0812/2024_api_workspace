import streamlit as st
import tensorflow as tf
import numpy as np


def load_and_use_tflite(tflite_mode_path):
    """
    Load a TensorFlow Lite model and use it for prediction
    
    Args:
        tflite_model_path (str): Path to the TFLite model
    
    Returns:
        function: A function that takes input and returns the prediction
    """
    # Load the TFLite model
    interpreter = tf.lite.Interpreter(model_path=tflite_mode_path)
    interpreter.allocate_tensors()
    
    # Get the input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    def predict(input_data):
         # Prepare input data
        input_data = np.array(input_data, dtype=np.float32).reshape(input_details[0]['shape'])
        
        # Set the tensor to point to the input data to be inferred
        interpreter.set_tensor(input_details[0]['index'], input_data)
        
        # Run the inference
        interpreter.invoke()
        
        # Get the output tensor
        output_data = interpreter.get_tensor(output_details[0]['index'])
        
        return output_data
    
    return predict


st.title('一元一次方程式')
st.title('Y = 2X - 1 ')

prompt = st.chat_input('請輸入X值:')
if prompt:
    input_value = float(prompt)
    thlite_model_path = 'linear_model.tflite'
    tf_predict = load_and_use_tflite(thlite_model_path)
    test_input = [input_value]
    predict_value = tf_predict(test_input)
    round_value = float(round(predict_value[0][0]))
    st.write(f'X={input_value} 預測值Y: {round_value}')
