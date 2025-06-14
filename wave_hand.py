import cv2
import streamlit as st
import mediapipe as mp

def wave_hand():
    st.info("Wave your hand left and right!")
    cap = cv2.VideoCapture(0)
    hands = mp.solutions.hands.Hands()
    stframe = st.empty()
    motion_count = 0
    last_x = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            x = results.multi_hand_landmarks[0].landmark[8].x
            if last_x is not None and abs(x - last_x) > 0.05:
                motion_count += 1
            last_x = x
            if motion_count > 3:
                st.success("👋 Hand wave detected!")
                st.balloons()
                break
        stframe.image(frame, channels="BGR")
    cap.release()