import cv2
import streamlit as st
import mediapipe as mp

def balloon_pop():
    st.info("Touch the balloon in the center to pop it!")
    cap = cv2.VideoCapture(0)
    hands = mp.solutions.hands.Hands()
    stframe = st.empty()

    bx1, by1, bx2, by2 = 250, 100, 350, 300
    mx1 = bx1 + int(0.2*(bx2-bx1))
    mx2 = bx2 - int(0.2*(bx2-bx1))
    my1 = by1 + int(0.2*(by2-by1))
    my2 = by2 - int(0.2*(by2-by1))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        cv2.rectangle(frame, (bx1, by1), (bx2, by2), (0, 0, 255), -1)
        cv2.putText(frame, "🎈", (bx1 + 30, by1 + 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 4)

        if results.multi_hand_landmarks:
            finger = results.multi_hand_landmarks[0].landmark[8]
            h, w, _ = frame.shape
            x, y = int(finger.x * w), int(finger.y * h)
            cv2.circle(frame, (x, y), 10, (255, 255, 255), -1)
            if mx1 < x < mx2 and my1 < y < my2:
                st.success("🎉 Balloon popped!")
                st.balloons()
                break

        stframe.image(frame, channels="BGR")
    cap.release()