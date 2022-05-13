import streamlit as st
from src.data_import import import_image
from src.model import image_compression

class webapp:
    def buildapp(self):
        st.title('Welcome to my image compression app, submit the image you want compressed below: ')
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            image, shape = import_image(uploaded_file)
            st.image(uploaded_file,'Image to be compressed.')
            st.write('Image is being compressed')
            compressed_im = image_compression(4, 3 , image,shape)
            st.image(compressed_im/255,caption='Compressed image.',channels='BGR')
            st.download_button(label="Download compressed image.", data=compressed_im.tobytes(), file_name='test.jpg')





