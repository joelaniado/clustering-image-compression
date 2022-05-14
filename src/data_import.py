import cv2
import numpy as np


def import_image(file):
    bytes_data = np.asarray(bytearray(file.read()), dtype=np.uint8)
    im = cv2.imdecode(bytes_data, cv2.IMREAD_COLOR)
    print("Original image shape: {}".format(im.shape))

    proc_im = np.reshape(im, (im.shape[0] * im.shape[1], im.shape[2]))
    print("Processed image shape: {}".format(proc_im.shape))
    return proc_im, im.shape, len(np.unique(proc_im, axis=0))
