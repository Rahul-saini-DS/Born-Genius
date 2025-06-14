
import streamlit as st
from smile_detection import smile_detection
from gaze_left import gaze_left
from raise_both_hands import raise_both_hands
from wave_hand import wave_hand
from balloon_pop import balloon_pop
from count_out_loud import count_out_loud

st.set_page_config(
    page_title="Born Genius AI",
    page_icon="👶",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<div style="text-align: center;">
    <h1 style="color:#ff4b4b;">👶 Born Genius AI</h1>
    <p style="font-size:18px;">Test your baby's early intelligence through fun activities using 👁️ Face, ✋ Hands, and 🧠 Movement detection!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #f8b400;'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("😊 Smile Detection"):
        smile_detection()
with col2:
    if st.button("👀 Gaze Left"):
        gaze_left()

col3, col4 = st.columns(2)
with col3:
    if st.button("🙌 Raise Both Hands"):
        raise_both_hands()
with col4:
    if st.button("👋 Wave Hand"):
        wave_hand()

st.markdown("<br>", unsafe_allow_html=True)
if st.button("🎈 Pop the Balloon"):
    balloon_pop()

if st.button("🧠 Count Out Loud"):
    count_out_loud()

st.markdown("""
<hr style='border:0.5px solid #eee;'>
<p style='text-align:center;font-size:14px;color:gray;'>
Made with ❤️ using <b>MediaPipe</b> and <b>Streamlit</b>
</p>
""", unsafe_allow_html=True)
