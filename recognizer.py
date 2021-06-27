import os
import numpy as np
import pandas as pd
from keras.models import model_from_json
import cv2


def recognize(image, kind):
    # image we got from user.
    if kind == 'dog':
        path = r"C:\Users\מאי\Desktop\python\flask\dog_model"
    else:
        path = r"C:\Users\מאי\Desktop\python\flask\cat_model"
    labels_path = os.path.join(path, "labels.csv")
    # read labels file.
    labels_file = pd.read_csv(labels_path)
    # Get all uniqe breeds in file.
    breeds = labels_file["breed"].unique()
    # dictionary of index and name of breed.
    dic_index_breed = {i: name for i, name in enumerate(breeds)}
    model_path_json = os.path.join(path, "model.json")
    # load json and create model
    json_file = open(model_path_json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    model_path_h5 = os.path.join(path, "model.h5")
    # load weights into new model
    loaded_model.load_weights(model_path_h5)
    # print("Loaded model from disk")
    # read image we get from user and resize it.
    size = 224
    # from bytes to numpy values.
    decoded = cv2.imdecode(np.frombuffer(image, np.uint8), -1)
    # resize to the suitable size.
    image = cv2.resize(decoded, (size, size))
    # normaliztion.
    image = image / 255.0
    image = image.astype(np.float32)
    image = np.expand_dims(image, axis=0)
    prediction = loaded_model.predict(image)[0]
    # get the 3 highest index in the prediction array.
    three_max_label_idx = np.argpartition(prediction, -3)[-3:]
    three_highest_values = prediction[three_max_label_idx]
    # give precent to each dog breed you predict.
    sum_values = np.sum(three_highest_values)
    precent_array = (three_highest_values / sum_values) * 100
    precent_array_round = np.round_(precent_array, decimals=3)
    # create list of key:name breed and precent as value.
    list_result = {}
    for i in range(3):
        label_idx = three_max_label_idx[i]
        predicted_breed_name = dic_index_breed[label_idx]
        precent = precent_array_round[i]
        list_result[predicted_breed_name]=str(precent)
    return list_result

