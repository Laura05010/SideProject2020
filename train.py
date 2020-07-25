<<<<<<< HEAD
#VIDEO 12:46
=======
#VIDEO 3:27
>>>>>>> 1c94912575fdbed09bbcc43b004f20aefa56e06b
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

<<<<<<< HEAD
def build_model(size, num_classes):
  inputs = Input((size, size, 3))
  backbone = MobileNetV2(input_tensor=inputs, include_top=False, weights="imagenet")
  backbone.trainable = True
  x = backbone.output
  x = GlobalAveragePooling2D()(x)
  x = Dropout(0.2)(x)
  x = Dense(1024, activation="relu")(x)
  x = Dense(num_classes, activation="softmax")(x)

  model = tf.keras.Model(inputs, x)
  return model

=======
>>>>>>> 1c94912575fdbed09bbcc43b004f20aefa56e06b
if __name__ == "__main__":
  path = "dog-breed-identification/"
  train_path = os.path.join(path, "train/*")
  test_path = os.path.join(path, "test/*")
  labels_path = os.path.join(path, "labels.csv")
  
  labels_df = pd.read_csv(labels_path)
  breed = labels_df["breed"].unique() 
  #breed = the list of unique breed
  #.unique() is unique list of values from a particular column
<<<<<<< HEAD
  print("Number of breeds: ", len(breed))
  #creating a dictionary by indexing the breeds of the list
  breed2id = {name: i for i, name in enumerate(breed)}
  
  ids = glob(train_path) #list of the path to all images
  labels = []
  for image_id in ids:
    image_id = image_id.split("/")[-1].split(".")[0]
     #last element of lst of "/" and the first element of the list "."!!!
    breed_name = list(labels_df[labels_df.id == image_id]["breed"])[0] #string obj, realted to the ids on csv
    breed_index = breed2id[breed_name]
    labels.append(breed_index)

  #Splitting the dataset
  train_x, valid_x = train_test_split(ids, test_size=0.2, random_state=42)
  train_y, valid_y = train_test_split(labels, test_size=0.2, random_state=42)
  
  #HyperParameters : trying to aim for goldilocks and best steps
  size = 224
  num_classes = 120 
  learning_rate = 1e-4
  batch = 8
  epochs = 10

  #Build the model_selection

  
  
=======
  print(breed)
>>>>>>> 1c94912575fdbed09bbcc43b004f20aefa56e06b
