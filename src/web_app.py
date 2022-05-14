import sys
import numpy as np
import streamlit as st
from src.data_import import import_image
from src.model import image_compression
import cv2
import os


class webapp:
    def buildapp(self):
        st.title("Welcome to my image compression app.")
        st.subheader("Please begin by reading the project description on the sidebar.")
        st.sidebar.title("Project description")
        st.sidebar.subheader(
            "Note: JPG images not supported, please use PNG extension."
        )
        st.sidebar.write(
            "Images are made out of individual pixels which are represented with a numeric value to specify"
            " its color. To give some perspective, each pixel has the option to choose between 16,581,375 "
            "different color values when rendering an image. Many of those colors are small variations of each other so "
            "by combining similar colors into one, we can reduce the amount of memory our picture needs."
        )
        st.sidebar.write(
            "Try it out! Upload an image, select the number of colors to compress to and see the result!"
        )
        uploaded_file = st.file_uploader(
            "Please upload your image here.", type=["png", "PNG"]
        )
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
            k = st.sidebar.slider(
                "Colors selector:", min_value=2, max_value=150, value=30
            )

            if st.button("Compress"):
                st.write(
                    "Please wait, if the image is too big it might take a couple of minutes... "
                )
                st.write(
                    "your image is being compressed...................................................."
                )
                st.write(
                    'Meanwhile think about how to finish this sentence:"If you give a moose a cupcake......"'
                )

                compressed_im = image_compression(24, k, image, shape).astype(np.uint8)
                st.image(
                    compressed_im,
                    caption="Compressed image.",
                    channels="BGR",
                )

                if cv2.imwrite("images/output/temp.png", compressed_im):
                    with open("images/output/temp.png", "rb") as file:
                        st.write(
                            "Your image has {0} unique colors in {1} pixels. Its size is around {2} Kilobytes.".format(
                                str(k),
                                str(shape[0] * shape[1]),
                                str(int(int(os.path.getsize(file.name)) / 1024)),
                            )
                        )
                        st.download_button(
                            label="Download compressed image.",
                            data=file,
                            file_name="compressed_{}".format(uploaded_file.name),
                        )
                os.remove("images/output/temp.png")


#
