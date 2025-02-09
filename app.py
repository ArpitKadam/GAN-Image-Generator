import streamlit as st
import numpy as np
import cv2
from tensorflow import keras

model = keras.models.load_model('my_model.keras')
class_name = ['angry','happy','sad']

def preprocess_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    image = cv2.resize(image, (48, 48))  # Resize to the input size of the model
    image = image / 255.0  # Normalize the image
    return np.expand_dims(image, axis=0)  # Add batch dimension

st.title("Human Emotion Detection")
st.write("Upload an image to detect the emotion.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    processed_image = preprocess_image(image)

    predictions = model.predict(processed_image)
    emotion = class_name[np.argmax(predictions)]  # Get the index of the highest probability

    st.write(f"Predicted Emotion: {emotion}")
