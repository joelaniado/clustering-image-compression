import cv2
import numpy as np


# Takes bytestream from input-file and returns np.array of image, og shape, and number of colors.
def import_image(file):
    # Read and decode image
    bytes_data = np.asarray(bytearray(file.read()), dtype=np.uint8)
    im = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR)
    # print("Original image shape: {}".format(im.shape))

    # Reshape and return
    proc_im = np.reshape(im, (im.shape[0] * im.shape[1], im.shape[2]))
    # print("Processed image shape: {}".format(proc_im.shape))
    return proc_im, im.shape, len(np.unique(proc_im, axis=0))
