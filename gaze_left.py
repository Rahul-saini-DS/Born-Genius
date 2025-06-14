import cv2
import streamlit as st
import mediapipe as mp

def gaze_left():
    st.info("Look at the left side of the screen!")
    cap = cv2.VideoCapture(0)
    mesh = mp.solutions.face_mesh.FaceMesh()
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        rgb = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        results = mesh.process(rgb)
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            center_x = (landmarks[33].x + landmarks[263].x) / 2
            if center_x < 0.4:
                st.success("👀 Looked left!")
                st.balloons()
                break
        stframe.image(frame, channels="BGR")
    cap.release()