import streamlit as st
import numpy as np
from PIL import Image

image = Image.open('../wally_foto.jpeg')

st.title('Where is Wally?')

wally = st.image(image, width=700)

def content():

    option = st.radio(
     'How would you like to upload a picture of Wally?',
     ('Upload file', 'Take photo through camera'))

    if option == 'Upload file':
        uploader = st.file_uploader('Upload Picture with Wally in it here:')

    if option == 'Take photo through camera':
        uploader = st.camera_input('Take a photo of Wally')



    button = st.button('Start searching for Wally')

    if uploader:
        suc = st.success('Photo uploaded')


    with st.spinner('Wait for it...'):

        if button and not uploader:
            st.error('You have not uploaded any picture. Upload picture and try again.')


        if uploader and button:
            wally.empty()
            np_picture = np.load(uploader)
            suc.empty()
            st.success('Wally is found!')
            st.image(np_picture)
            st.balloons()


content()
