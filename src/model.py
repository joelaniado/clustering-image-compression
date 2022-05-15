import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
import time

# Builds compressed image using new colors for each pixel.
def get_comp_image(cen, lab):
    new_image = np.array([cen[i] for i in lab])
    return new_image


# Performs Kmeans clustering on image array and returns compressed image array.
def image_compression(seed, k, image, shape, file="test"):
    start = time.time()
    k_means = MiniBatchKMeans(n_clusters=k, random_state=seed).fit(image)
    print(time.time()-start)
    centroids, labels = k_means.cluster_centers_, k_means.labels_

    # Build compressed image and reshape
    vec_comp_im = get_comp_image(centroids, labels)
    compressed_im = np.reshape(vec_comp_im, shape)

    # cv2.imwrite("images/output/{}".format(file), compressed_im)
    # plt.imshow((compressed_im / 255)[..., ::-1])
    # plt.show()
    return compressed_im
