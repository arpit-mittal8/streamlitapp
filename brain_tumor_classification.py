# brain_tumor_classification.py
import streamlit as st
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Function to navigate to the Parkinson's page
def navigate_to_parkinsons():
    st.session_state.page = 'park_pred'  # Set the session state to navigate to 'park_pred'

# Load the pre-trained Keras model
@st.cache_resource
def load_keras_model():
    return load_model('models/BrainTumor10Epochs.h5')

model = load_keras_model()

# Define a function to classify the uploaded image
def classify_image(image, model):
    # Resize the image to the size the model expects (64x64)
    size = (64, 64)
    image = ImageOps.fit(image, size, Image.LANCZOS)
    
    # Convert the image to an array
    img_array = np.asarray(image)
    
    # Normalize the image array
    img_array = img_array / 255.0
    
    # Expand dimensions to match the model's input shape
    img_array = np.expand_dims(img_array, axis=0)
    
    # Make a prediction
    prediction = model.predict(img_array)
    
    return prediction

# Define the Streamlit app interface for this page
def main():
    st.title("Brain Tumor Classification from MRI Images")
    st.write("Upload an MRI image to classify if it has a brain tumor or not.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an MRI image...", type="jpg")

    if uploaded_file is not None:
        # Display the uploaded image in a smaller size
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded MRI image', use_column_width=False, width=200)
        
        st.write("")
        st.write("Classifying...")
        
        # Classify the uploaded image
        prediction = classify_image(image, model)
        
        # Get the class with the highest probability
        class_names = ['No Brain Tumor', 'Yes Brain Tumor']
        result = class_names[np.argmax(prediction)]
        
        st.write(f"Prediction: {result}")
        st.write(f"Confidence: {prediction[0][np.argmax(prediction)] * 100:.2f}%")
        
        # Display the "Proceed Further" button
        if st.button("We suggest you to also check for Parkinsons Disease ->"):
            st.session_state.page = 'park_pred'  # Navigate to the Parkinson's page

# This ensures that the main() function is only called when this file is run directly
if __name__ == "__main__":
    main()
