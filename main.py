#emotion_detection.py
from time import sleep
import cv2
import os
from deepface import DeepFace
import matplotlib.pyplot as plt
import numpy as np  #this will be used later in the process
import AvatarManager as am
import random as rd

cwd = os.getcwd()

imgPathsList = list()

try:
    imgPathsList = os.listdir(cwd + "/res/test") # build a list of all test images
except FileNotFoundError:
    print("Make sure current working directory is ./EmotionDetector")

for i in range(len(imgPathsList)):
    imgPathsList[i] = cwd + "/res/test/" + imgPathsList[i]

av = am.AvatarManager("Gabriel", cwd + "/res/avatars/")

while(True):
    rdImg = rd.choice(imgPathsList)
    # angry, fear, neutral, sad, disgust, happy and surprise
    result = DeepFace.analyze(img_path = rdImg, models = {'emotion': DeepFace.build_model('Emotion')}, detector_backend='retinaface', enforce_detection=False, prog_bar=False)
    
    print("Random img picked: " + rdImg.replace(cwd + "/res/test/", ""))
    av.setEmotion(result["dominant_emotion"])
    av.showAvatar()
    