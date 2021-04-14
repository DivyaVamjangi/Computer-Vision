# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:29:04 2020

@author: divya
"""

from keras.models import load_model
import cv2
import numpy as np
import sys

 filepath = (r"C:\Users\divya\Desktop\rock-paper-scissors-master\rock-paper-scissors-master\image_data\paper\1.jpg")

REV_CLASS_MAP = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}


def mapper(val):
    return REV_CLASS_MAP[val]


model = load_model("rock-paper-scissors-model.h5")

# prepare the image
img = cv2.imread(filepath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (227, 227))

# predict the move made
pred = model.predict(np.array([img]))
move_code = np.argmax(pred[0])
move_name = mapper(move_code)

print("Predicted: {}".format(move_name))