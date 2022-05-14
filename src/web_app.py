import sys

import streamlit as st
from src.data_import import import_image
from src.model import image_compression
import cv2
import os


class webapp:
    def buildapp(self):
        st.title(
            "Welcome to my image compression app, submit the image you want compressed below: "
        )
        st.subheader('Please begin by reading the project description on the sidebar.')
        st.sidebar.title("Project description")
        st.sidebar.write(
            "This project consists of using machine learning for compressing the size of an image by means "
            "of clustering similar pixel color values. \n"
        )
        st.sidebar.write(
            "Images are made out of individual pixels which are represented with a numeric value to specify"
            "its specific color. To give some perspective, each pixel has the option to choose between 16,581,375 "
            "different color values when rendering an image. Many of those colors are small variations of the same one "
            "but slightly different. By uploading your image on the right, you can see just how many unique colors there"
            " are in your picture. "
        )

        st.sidebar.write('In order to reduce the memory requirements of our image we can group similar colors of pixels'
                         ' into a single color! This will help us reduce its size while keeping the same dimensions. ')
        st.sidebar.write('Try it out! Select the number of colors that you want your image to have and see if you if the '
                         'quality is comparable to the original.')
        uploaded_file = st.file_uploader("Please upload your image here.")
        if uploaded_file is not None:
            image, shape, color_n = import_image(uploaded_file)
            st.image(uploaded_file, "Image to be compressed.")
            st.write(
                "Your image has {0} unique colors in {1} pixels. Its size is around {2} Kilobytes.".format(
                    str(color_n),
                    str(shape[0] * shape[1]),
                    str(int(uploaded_file.size / 1024)),
                )
            )
            st.sidebar.write(
                'In order to reduce the memory requirements of our image we can group similar colors of pixels'
                ' into a single color! This will help us reduce its size while keeping the same dimensions. ')
            st.sidebar.write(
                'Try it out! Select the number of colors that you want your image to have and see if you if the '
                'quality is comparable to the original.')
            k = st.sidebar.slider(
                "Select number of clusters:", min_value=2, max_value=200, value=30
            )

            if st.button("Compress"):
                st.write(
                    "Please wait, your image is being compressed....................................................")

                compressed_im = image_compression(24, k, image, shape)
                st.image(
                    compressed_im.astype("int32"),
                    caption="Compressed image.",
                    channels="BGR",
                )

                if cv2.imwrite("images/output/test.jpg", compressed_im):
                    with open("images/output/test.jpg", "rb") as file:
                        st.write(
                            "Your image has {0} unique colors in {1} pixels. Its size is around {2} Kilobytes.".format(
                                str(k),
                                str(shape[0] * shape[1]),
                                str(sys.getsizeof(file)/1024),
                            )
                        )
                        st.download_button(
                            label="Download compressed image.",
                            data=file,
                            file_name="compressed_image.jpg",
                        )
                os.remove("images/output/test.jpg")
