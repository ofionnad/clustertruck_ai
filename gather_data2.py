import numpy as np
import cv2
import time
import os

from utils.screengrab import grab


while True:
    last_time = time.time()
    img = grab()
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    img = cv2.Canny(img, threshold1=50, threshold2=200)
    img = cv2.resize(img, (224,224))

    cv2.imshow("ClusterTruck AI peak", img)
    cv2.waitKey(1)

    #img = np.array(img)
    #img_data.append(img)

    #keys = key_check()
    #targets.append(keys)

    print("fps: {}".format(1 / (time.time() - last_time)))
    #print(time.time())

    if cv2.waitKey(50) & 0xFF == ord('q'):
        print("Exiting!\n")
        break