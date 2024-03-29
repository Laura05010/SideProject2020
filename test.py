#pip install pandas
#pip install opencv-python
#pip install tensorflow
#pip install sklearn

import os
import numpy as np
import pandas as pd
import cv2
from glob import glob
from tqdm import tqdm
import tensorflow as tf
from sklearn.model_selection import train_test_split

def read_image(path, size):
  image = cv2.imread(path, cv2.IMREAD_COLOR)
  image = cv2.resize(image, (size,size))
  image = image / 255.0
  image = image.astype(np.float32)
  return image
  
if __name__ == "__main__":
  path = "dog-breed-identification/"
  train_path = os.path.join(path, "train/*")
  test_path = os.path.join(path, "test/*")
  labels_path = os.path.join(path, "labels.csv")
  
  labels_df = pd.read_csv(labels_path)
  breed = labels_df["breed"].unique() 
  #breed = the list of unique breed
  #.unique() is unique list of values from a particular column
  print("Number of breeds: ", len(breed))
  #creating a dictionary by indexing the breeds of the list
  breed2id = {name: i for i, name in enumerate(breed)}
  id2breed = {i: name for i, name in enumerate(breed)}

  ids = glob(train_path) #list of the path to all images
  labels = []

  for image_id in ids:
    image_id = image_id.split("/")[-1].split(".")[0]
     #last element of lst of "/" and the first element of the list "."!!!
    breed_name = list(labels_df[labels_df.id == image_id]["breed"])[0] #string obj, realted to the ids on csv
    breed_index = breed2id[breed_name]
    labels.append(breed_index)

  ids = ids[:1000]
  labels = labels[:1000]

  #Splitting the dataset
  train_x, valid_x = train_test_split(ids, test_size=0.2, random_state=42)
  train_y, valid_y = train_test_split(labels, test_size=0.2, random_state=42)
  
  #Model
  model = tf.keras.models.load_model("model.h5")

  for i, path in tqdm(enumerate(valid_x[:10])):
    image = read_image(path, 224)
    image = np.expand_dims(image, axis= 0)
    prediction = model.predict(image)[0]
    label_index = np.argmax(prediction)
    breed_name = id2breed[label_index]

    ori_breed = id2breed[valid_y[1]]
    ori_image = cv2.imread(path, cv2.IMREAD_COLOR)


  #WHAT ITS SUPPOSED TO BE 
    ori_image = cv2.putText(ori_image, breed_name, (0,10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0), 1)

  #WHAT ITS SUPPOSED TO BE 
    ori_image = cv2.putText(ori_image, ori_breed, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    
    # cv2.imwrite(f"save/valid_{i}.png", ori_image
    filename = "save/valid_{i}.png".format(i=i)
    #f"save/valid_{i}.png"
    cv2.imwrite(filename, ori_image)
