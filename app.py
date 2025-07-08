import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
from PIL import Image

# Initialize session state
if 'camera_running' not in st.session_state:
    st.session_state['camera_running'] = False

# Cache model loading to optimize performance
@st.cache_resource
def load_model():
    try:
        return tf.keras.models.load_model("sign_language_model.h5")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

model = load_model()

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5
)

# Define class names
sign_language_classes = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "ExcuseMe",
    "F", "Food", "G", "H", "Hello", "Help", "House", "I", "I Love You", "J", "K", "L",
    "M", "N", "No", "O", "P", "Please", "Q", "R", "S", "T", "ThankYou", "U", "V", "W",
    "X", "Y", "Yes", "Z"
]

def process_landmarks(hand_landmarks):
    landmarks = [lm.x for lm in hand_landmarks.landmark] + \
                [lm.y for lm in hand_landmarks.landmark] + \
                [lm.z for lm in hand_landmarks.landmark]
    return landmarks

def pad_landmarks():
    return [0.0] * 63

def classify_gesture(frame):
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(image_rgb)

    if result.multi_hand_landmarks:
        combined_landmarks = process_landmarks(result.multi_hand_landmarks[0])
        
        if len(result.multi_hand_landmarks) > 1:
            combined_landmarks += process_landmarks(result.multi_hand_landmarks[1])
        else:
            combined_landmarks += pad_landmarks()

        landmarks_array = np.array(combined_landmarks).reshape(1, -1)
        
        if model:
            prediction = model.predict(landmarks_array, verbose=0)
            class_id = np.argmax(prediction[0])
            confidence = prediction[0][class_id]
            return sign_language_classes[class_id], result.multi_hand_landmarks, confidence
        
    return None, None, None

def run_camera():
    st.write("Attempting to access the webcam...")
    cap = cv2.VideoCapture(0)  # Open the webcam
    if not cap.isOpened():
        st.error("Failed to access the webcam. Please check your camera permissions.")
        return

    stframe = st.empty()  # Placeholder for the video feed

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture video frame.")
            break

        # Convert the frame to RGB (Streamlit requires RGB format)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame_rgb, channels="RGB", use_column_width=True)

        # Stop the camera when the user clicks the "Stop Camera" button
        if st.button("Stop Camera", key="stop_camera"):
            break

    cap.release()
    
def process_uploaded_image(image_bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return frame

def main():
    st.title("Hand Sign Recognition")

    input_source = st.radio("Select Input Source:", ["Webcam", "Upload Image"])

    if input_source == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])
        
        if uploaded_file:
            image_bytes = uploaded_file.read()
            frame = process_uploaded_image(image_bytes)
            gesture, hand_landmarks, confidence = classify_gesture(frame)

            if hand_landmarks:
                for landmarks in hand_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            if gesture:
                cv2.putText(frame, f"Prediction: {gesture}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                st.write(f"Detected Sign: {gesture}")
                if confidence:
                    st.write(f"Confidence: {confidence:.2%}")
            else:
                st.write("No sign detected")

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            st.image(frame_rgb, caption="Processed Image", use_container_width=True)

    else:  # Webcam
        video_placeholder = st.empty()
        prediction_placeholder = st.empty()
        confidence_placeholder = st.empty()

        if st.button("Start Camera", key="start_camera"):
            st.session_state['camera_running'] = True
        
        if st.session_state['camera_running']:
            cap = cv2.VideoCapture(0)

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    st.error("Failed to read from webcam")
                    break

                gesture, hand_landmarks, confidence = classify_gesture(frame)

                if hand_landmarks:
                    for landmarks in hand_landmarks:
                        mp.solutions.drawing_utils.draw_landmarks(
                            frame, landmarks, mp_hands.HAND_CONNECTIONS)

                if gesture:
                    cv2.putText(frame, f"Prediction: {gesture}", (10, 30),
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    prediction_placeholder.text(f"Detected Sign: {gesture}")
                    if confidence:
                        confidence_placeholder.progress(float(confidence), f"Confidence: {confidence:.2%}")

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                video_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

            cap.release()
            st.session_state['camera_running'] = False
        
        if st.button("Stop Camera", key="stop_camera"):
            st.session_state['camera_running'] = False

    # Take and predict an image
    st.title("Predict Sign from Captured Image")
    
    if st.button("Capture Photo", key="capture_photo"):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            gesture, hand_landmarks, confidence = classify_gesture(frame)

            if hand_landmarks:
                for landmarks in hand_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(
                        frame, landmarks, mp_hands.HAND_CONNECTIONS)

            if gesture:
                cv2.putText(frame, f"Prediction: {gesture}", (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                st.write(f"Detected Sign: {gesture}")
                if confidence:
                    st.write(f"Confidence: {confidence:.2%}")
            else:
                st.write("No sign detected")

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            st.image(frame_rgb, caption="Captured Image", use_container_width=True)
        else:
            st.error("Failed to capture image")

if __name__ == "__main__":
    main()