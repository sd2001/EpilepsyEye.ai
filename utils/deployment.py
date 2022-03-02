import streamlit as st
import cv2
import urllib
import io
import tempfile
import time

def video_upload():

    html_temp = '''
    <div>
    <h2></h2>
    <center><h3>Please upload Video to run the Algorithm</h3></center>
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html=True)

    #try:

    opt = st.selectbox("How do you want to upload the image?\n", ('Please Select', 'Upload image via link', 'Upload image from device'))
    
    if opt == 'Upload image from device':
        
        uploaded_file = st.file_uploader("Choose a video in .mp4 format", type=["mp4"])
        temporary_location = False

        if uploaded_file is not None:
            g = io.BytesIO(uploaded_file.read())  ## BytesIO Object
            temporary_location = "utils/test/test.mp4"

            with open(temporary_location, 'wb') as out:  ## Open temporary file as bytes
                out.write(g.read())  ## Read bytes into file

            # close file
            out.close()

    # elif opt == 'Upload image via link':
        
    #     try:
    #         img = st.text_input('Enter the Image Address')
    #         input_video = cv2.VideoCapture(urllib.request.urlopen(img))
        
    #     except:
    #         if st.button('Submit'):
    #             show = st.error("Please Enter a valid Image Address!")
    #             time.sleep(4)
    #             show.empty()

    #return input_video

    #except:

    #    st.info("Please upload your image in '.jpg', '.jpeg' or '.png'")
