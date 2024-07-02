import streamlit as st
import cv2
import numpy as np
from app_controllers.controller import Controller
from app_models.model import Model
from app_views.view import View  # Adjust if necessary

# Assuming the `Model`, `Controller`, and `View` are compatible with Streamlit
model_name = "small640.pt"

class App:
    def __init__(self, model_name):
        self.model = Model(model_name)
        self.view = View(self.model)
        self.controller = Controller(self.model, self.view)
        print("All modules loaded")

# Streamlit App
st.title("Posture Detection App")

run = st.checkbox('Run')
FRAME_WINDOW = st.image([])

app = App(model_name)
camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret:
        st.write("Failed to access webcam.")
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame using the controller
    processed_frame = app.controller.process_frame(frame)
    
    # Display the processed frame
    FRAME_WINDOW.image(processed_frame)
else:
    st.write('Stopped')
    camera.release()
    cv2.destroyAllWindows()
