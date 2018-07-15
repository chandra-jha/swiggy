import cv2
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
import numpy as np 
from glob import glob
import pickle
import multiprocessing
import os

sift_object = cv2.xfeatures2d.SIFT_create()

def features(image):
    keypoints, descriptors = sift_object.detectAndCompute(image, None)
    return descriptors

image_dir = "/home/ubuntu/foodissues_cat/PACKAGING_ISSUES"
im_list = glob(image_dir + "/*")
output_dir = "/home/ubuntu/foodissues_features/"


def extract_features(image_path):
    cv2img = cv2.imread(image_path)
    feat = features(cv2img)
    name = os.path.basename(image_path).strip('.jpg')
    np.savetxt(os.path.join(output_dir, name + ".feat"), feat, delimiter=',')

count = 0
for im in im_list:
    print("trying", im)
    try:
        name = os.path.basename(im).strip('.jpg')
        if not os.path.exists(os.path.join(output_dir, name + ".feat")):
            extract_features(im)
            count += 1
            print(count, len(im_list))
        else:
            count += 1
    except Exception as e:
        print(e)
        pass
