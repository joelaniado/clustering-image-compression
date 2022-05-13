import streamlit as st
from src.data_import import import_image
from src.model import image_compression
import cv2
import os

class webapp:
    def buildapp(self):
        st.title('Welcome to my image compression app, submit the image you want compressed below: ')
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            image, shape = import_image(uploaded_file)
            st.image(uploaded_file,'Image to be compressed.')
            st.write('Image is being c:ompressed')
            compressed_im = image_compression(4, 50, image,shape)
            st.image(compressed_im.astype('int32'), caption='Compressed image.',channels='BGR')
            if cv2.imwrite('images/output/test.jpg', compressed_im):
                with open("images/output/test.jpg", "rb") as file:
                    st.download_button(label="Download compressed image.", data=file, file_name='compressed_image.jpg')
            os.remove('images/output/test.jpg')





