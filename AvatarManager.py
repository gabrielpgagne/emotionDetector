import matplotlib.pyplot as plt
import cv2

class AvatarManager:
    def __init__(self, name: str, imgDir: str, imgDict: dict):
        self.name = name
        self.imgDir = imgDir
        self.imgDict = imgDict
        self.emotion = "none"
        self.img = None

    def __str__(self) -> str:
        return self.getName()

    def getName(self) -> str:
        return self.name

    def getImgDir(self) -> str:
        return self.imgDir

    def getImgDict(self) -> dict:
        return self.imgDict

    def setName(self, newName:str):
        self.name = newName

    def setImgDir(self, newImgDir:str):
        self.imgDir = newImgDir

    def setEmotion(self, emotion:str):
        self.emotion = emotion
    
    def getEmotion(self):
        return self.emotion

    def getEmotionPath(self):
        return self.getImgDir() + (self.getImgDict())[self.getEmotion()]

    def showAvatar(self):
        print("Avatar emotion: " + self.getEmotion())
        self.img = cv2.imread(self.getEmotionPath())
        cv2.imshow(self.getName(), self.img)
        cv2.waitKey(3000)
    
