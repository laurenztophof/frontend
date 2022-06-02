import streamlit as st
import numpy as np
from PIL import Image

image = Image.open('../wally_foto.jpeg')

st.title('Where is Wally?')

wally = st.image(image, width=700)



raw_picture = st.file_uploader('Upload Picture with Wally in it here:')
with st.container():
    with st.spinner('Wait for it...'):

        if raw_picture:
            wally.empty()
            np_picture = np.load(raw_picture)


        if raw_picture:
            st.markdown('Wally is found!')
            st.image(np_picture)
            st.balloons()
