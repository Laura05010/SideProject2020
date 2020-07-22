#VIDEO 3:27
#pip install pandas
#pip install opencv-python
#pip install tensorflow
#pip install sklearn
import os
import numpy as np
import pandas as pd
import cv2
from glob import glob

import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam

from sklearn.model_selection import train_test_split

if __name__ == "__main__":
  path = "dog-breed-identification/"
  train_path = os.path.join(path, "train/*")
  test_path = os.path.join(path, "test/*")
  labels_path = os.path.join(path, "labels.csv")
  
  labels_df = pd.read_csv(labels_path)
  breed = labels_df["breed"].unique() 
  #breed = the list of unique breed
  #.unique() is unique list of values from a particular column
  print(breed)
