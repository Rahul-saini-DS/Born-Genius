import cv2
import streamlit as st
import mediapipe as mp

def smile_detection():
    st.info("Smile when you're happy!")
    cap = cv2.VideoCapture(0)
    mp_face = mp.solutions.face_mesh
    mesh = mp_face.FaceMesh()
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        rgb = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        results = mesh.process(rgb)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            if abs(landmarks[13].y - landmarks[14].y) > 0.03:
                st.success("😊 Detected a smile!")
                st.balloons()
                break
        stframe.image(frame, channels="BGR")
    cap.release()