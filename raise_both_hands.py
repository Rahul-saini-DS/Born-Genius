import cv2
import streamlit as st
import mediapipe as mp

def raise_both_hands():
    st.info("Raise both hands above your shoulders!")
    cap = cv2.VideoCapture(0)
    pose = mp.solutions.pose.Pose()
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            if landmarks[15].y < landmarks[11].y and landmarks[16].y < landmarks[12].y:
                st.success("🙌 Both hands are up!")
                st.balloons()
                break
        stframe.image(frame, channels="BGR")
    cap.release()