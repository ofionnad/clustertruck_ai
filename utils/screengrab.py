import numpy as np
import cv2
import mss
import time

def grab(region=None):

    with mss.mss() as sct:
    # Part of the screen to capture
        if region:
            top, left, width, height = region
            monitor = {"top": top, "left": left, "width": width, "height": height}
        else:
            #default top left placement on my monitor-ish
            monitor = {"top": 65, "left": 80, "width": 1280, "height": 798}

        img = np.array(sct.grab(monitor))

        return img
        
        #some quick operations
        #img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        #img = cv2.resize(img, (224,224))

        # Display the picture
        #cv2.imshow("OpenCV/Numpy normal", img)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

if __name__=="__main__":
    grab()