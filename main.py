import streamlit as st
from utils.deployment import *
import cv2
from utils.video import *

set_bg_local("misc/images/bg.jpg")
opt = st.sidebar.selectbox("",("Home", "Transform"))

try:
	if opt=="Home":
		html_temp = '''
			<div>
			<center><h2>EpilepsyEye.ai</h2></center>
			</div>
			Epilepsy is a disorder in which nerve cell activity in the brain is disturbed, causing seizures.
			<br></br>
			Photosensitive epilepsy is when seizures are triggered by flashing lights or contrasting light and dark pattern. Flashing or patterned effects can make people with or without epilepsy feel disorientated, uncomfortable or unwell.
			<br></br>
			when a person experiences abnormal behaviour, symptoms and sensations, sometimes including loss of consciousness.So this project aims to converts the disturbing images into grayscale and prevent seizures 
			<br>
			'''
		st.markdown(html_temp, unsafe_allow_html=True)
	
		st.markdown(" ### photosensitive epileptic image ")
		col1,col2,col3=st.columns(3)
		with col1:
			st.image("https://images.pond5.com/colorful-psychedelic-epileptic-background-footage-080296243_prevstill.jpeg")
		with col2:
			st.image("https://www.brainfacts.org/-/media/Brainfacts2/Diseases-and-Disorders/Epilepsy/Article-Images/Flashing-Lights-thumbnail.jpg")
		with col3:
			st.image("https://media.istockphoto.com/videos/rainbow-gay-flag-animation-on-white-background-video-id1173187170?s=256x256")

	else:

		if video_upload():
			st.info("Your video has been Uploaded!")

			if st.button("Start Processing"):
				run()

except Exception as e:
    pass