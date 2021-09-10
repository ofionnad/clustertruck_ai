from fastai.vision.all import *
import time
import cv2
from utils.screengrab import grab

def label_func(x): return x.parent.name

def run():
    path = Path("/home/dualta/Documents/code/ml/game_bot/clusterbot/data/", recurse=True)
    fnames = get_image_files(path)
    print("Total Images: {}".format(len(fnames)))

    dls = ImageDataLoaders.from_path_func(path, fnames, label_func, bs=40, num_workers=0)
    learn = cnn_learner(dls, models.resnet18, 
        pretrained=True, metrics=[error_rate, accuracy], 
        loss_func=CrossEntropyLossFlat())
    print("Loaded")
    learn.fine_tune(50, base_lr=0.01)

    learn.export(fname='trained_model.pkl')

    start_time = time.time()
    img = grab()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, threshold1=50, threshold2=200)
    img = cv2.resize(img, (224, 244))
    test = learn.predict(img)
    print("--- {} seconds ---".format(time.time() - start_time))
    print(test)

if __name__ == '__main__':
    run()