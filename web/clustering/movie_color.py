import cv2
import os
import numpy as np
from collections import Counter
from sklearn.cluster import KMeans

image1 = "https://image.tmdb.org/t/p/original/8dzKn3RtPWUJRG9ymSpi423eMNV.jpg"
image2 = "https://image.tmdb.org/t/p/original/2R8smeSDkPx6TKIRveKPXi0JVI6.jpg"


os.system("curl " + image1 + " > test1.jpg")
os.system("curl " + image2 + " > test2.jpg")

img1 = cv2.imread("test1.jpg")
img2 = cv2.imread("test2.jpg")

#print(img1)
img1 = cv2.resize(img1,(320,480))

img= np.array(img1)

clt=KMeans(n_clusters=3)

from collections import Counter


def palette_perc(k_cluster):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)

    n_pixels = len(k_cluster.labels_)
    counter = Counter(k_cluster.labels_)  # count how many pixels per cluster
    perc = {}
    for i in counter:
        perc[i] = np.round(counter[i] / n_pixels, 2)
    perc = dict(sorted(perc.items()))

    # for logging purposes
    #print(perc)
    #print(k_cluster.cluster_centers_)

    step = 0

    for idx, centers in enumerate(k_cluster.cluster_centers_):
        palette[:, step:int(step + perc[idx] * width + 1), :] = centers
        step += int(perc[idx] * width + 1)

    return palette


clt_1 = clt.fit(img.reshape(-1, 3))
cv2.imshow("ddd",img1)
cv2.imshow('ss',palette_perc(clt_1))
print(palette_perc(clt_1))
cv2.waitKey(0)
