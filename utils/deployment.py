from __future__ import unicode_literals
#from pytube import YouTube
import streamlit as st
import cv2
import urllib
import io
import tempfile
import time
from mhyt import yt_download

import youtube_dl

def video_upload():

    html_temp = '''
    <div>
    <h2></h2>
    <center><h3>Please upload Video to run the Algorithm</h3></center>
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html=True)

    try:

        opt = st.selectbox("How do you want to upload the video?\n", ('Please Select', 'Upload video via link', 'Upload video from device'))

        temporary_location = "utils/test/test.mp4"

        if opt == 'Upload video from device':
            
            uploaded_file = st.file_uploader("Choose a video in .mp4 format", type=["mp4"])
            #temporary_location = False

            if uploaded_file is not None:
                g = io.BytesIO(uploaded_file.read())  ## BytesIO Object
                

                with open(temporary_location, 'wb') as out:  ## Open temporary file as bytes
                    out.write(g.read())  ## Read bytes into file

                # close file
                out.close()

        elif opt == 'Upload video via link':
            
            try:
                link = st.text_input('Enter the youtube URL')
                yt_download(link,temporary_location)

            except:
                st.error("")

    except:

         st.info("Please upload your video in '.mp4' format")
