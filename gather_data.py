import numpy as np
import cv2
import time
import os

from utils.screengrab import grab
from pynput import keyboard, mouse

from functools import partial

#from utils.keyslisten import key_listener
#from utils.mouselisten import mouse_listener
#from utils.getkeys import key_check

filename = "data/training_data.npy"
filename2 = "data/target_data.npy"

def read():
    if os.path.isfile(filename):
        print('File exists, loading old image data.')
        img_data = list(np.load(filename, allow_pickle=True))
        targets = list(np.load(filename2, allow_pickle=True))
    else:
        print('File does not exist. New data.')
        img_data, targets = [], []
    
    return img_data, targets

def save(image_data, target):
    np.save(filename, image_data)
    np.save(filename2, target)


def on_press(keylist, key):
    try:
        if key.char != 'q':
            keylist.append(key.char)
    except AttributeError:
        keylist.append(str(key).split('.')[1])
    #print(keylist)

def on_release(keylist, key):
    try:
        if key.char=='q':
            pass
        else:
            keylist.append('-'+str(key.char))
    except AttributeError:
        keylist.append('-'+str(key).split('.')[1])
    #print(keylist)


#def on_move(target, x, y):
#    target.append((x, y))

#keys = key_listener()
#keys.start()
#mouses = mouse_listener()
#mouses.start()

img_data, targets = read()

"""
while True:
    keys = key_check()
    print("Waiting to start. Press g.")
    if keys == "g":
        print("Starting")
        break
"""

while True:
    last_time = time.time()
    img = grab()
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    img = cv2.Canny(img, threshold1=50, threshold2=200)
    img = cv2.resize(img, (224,224))

    cv2.imshow("ClusterTruck AI peak", img)
    cv2.waitKey(1)

    new_targets = [] #new moves

    on_press_partial = partial(on_press, new_targets)
    on_release_partial = partial(on_release, new_targets)
    listener = keyboard.Listener(on_press=on_press_partial, on_release=on_release_partial)
    listener.start()

    #print(new_targets)
    #on_move_partial = partial(on_move, targets)
    #listener = mouse.Listener(on_press=on_move_partial)

    img = np.array(img)
    img_data.append(img)

    # always move forward criterion.
    #if not new_targets:
    #    new_targets.append('w')

    targets.append(new_targets) # save the moves for this loop as a tuple

    #keys = key_check()
    #targets.append(keys)

    print("fps: {}".format(1 / (time.time() - last_time)))
    #print(time.time())

    # this only works when the cv2 window is active!
    # k = cv2.waitKey(5) 
    # if k > 0:
    #     print(cv2.waitKeyEx(0))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        print("Exiting!\n")
        break

    listener.stop()

targets = np.asanyarray(targets)
save(img_data, targets)