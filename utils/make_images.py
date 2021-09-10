import cv2
import numpy as np

data = np.load("../data/training_data.npy", allow_pickle=True)
targets = np.load("../data/target_data.npy", allow_pickle=True)

print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Lets see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])

count_up, let_up = 0, 0
count_left, let_left = 0, 0
count_right, let_right = 0, 0
count_jump, let_jump = 0, 0
count_down, let_down = 0, 0
do_nothing = 0

for data in holder_list:
    #print(data[1])
    if 'w' in data[1]:
        count_up += 1
        cv2.imwrite(f"../data/Up/H7-u{count_up}.png", data[0]) 
    elif 'a' in data[1]:
        count_left += 1
        cv2.imwrite(f"../data/Left/H7-l{count_left}.png", data[0]) 
    elif 'd' in data[1]:
        count_right += 1
        cv2.imwrite(f"../data/Right/H7-r{count_right}.png", data[0])
    elif 's' in data[1]:
        count_down += 1
        cv2.imwrite(f"../data/Down/H7-d{count_jump}.png", data[0]) 
    elif 'space' in data[1]:
        count_jump += 1
        cv2.imwrite(f"../data/Jump/H7-j{count_jump}.png", data[0])
    elif '-w' in data[1]:
        let_up += 1
        cv2.imwrite(f"../data/aUp/H7-u{let_up}.png", data[0]) 
    elif '-a' in data[1]:
        let_left += 1
        cv2.imwrite(f"../data/aLeft/H7-l{let_left}.png", data[0]) 
    elif '-d' in data[1]:
        let_right += 1
        cv2.imwrite(f"../data/aRight/H7-r{let_right}.png", data[0])
    elif '-s' in data[1]:
        let_down += 1
        cv2.imwrite(f"../data/aDown/H7-d{let_jump}.png", data[0]) 
    elif '-space' in data[1]:
        let_jump += 1
        cv2.imwrite(f"../data/aJump/H7-j{let_jump}.png", data[0])
    elif not data[1]:
        do_nothing += 1
        #try to balance out dataset so it doesn't just do nothing all the time
        if do_nothing % 50 == 0:
            cv2.imwrite(f"../data/Nothing/H7-n{do_nothing}.png", data[0])