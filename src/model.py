import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def get_comp_image(cen, lab):
    new_image = [cen[i] for i in lab]
    return new_image


def image_compression(seed, k, image, shape, file):
    k_means = KMeans(n_clusters=k, random_state=seed).fit(image)
    centroids, labels = k_means.cluster_centers_, k_means.labels_
    vec_comp_im = np.array(get_comp_image(centroids, labels))
    print(vec_comp_im, vec_comp_im.shape)
    compressed_im = np.reshape(vec_comp_im, shape)
    cv2.imwrite("images/output/{}".format(file), compressed_im)
    plt.imshow((compressed_im / 255)[..., ::-1])
    plt.show()
    return compressed_im
