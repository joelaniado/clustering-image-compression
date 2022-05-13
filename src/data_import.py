import cv2
import numpy as np


def import_image(image):
    im = cv2.imread(image)
    print(im.shape)

    proc_im = np.reshape(im, (im.shape[0] * im.shape[1], im.shape[2]))
    print(proc_im.shape)
    return proc_im, im.shape
