import streamlit as st
from utils.deployment import *
import cv2

opt = st.sidebar.selectbox("",("Home", "Transform"))

if opt=="Home":
    st.write("Hi")

else:
    video_upload()
    path = "utils/test/test.mp4"
    st.video(path)




 