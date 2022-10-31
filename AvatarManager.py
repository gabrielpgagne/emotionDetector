import matplotlib.pyplot as plt
import cv2

class AvatarManager:
    """
    Class AvatarManager handles the on-screen printing of the avatar corresponding with the Emotion and Eye status.
    """
    def __init__(self, name: str, imgDir: str):
        """
        Class initializer

        Parameter name: string for the Avatar's name. Used to identify avatar objects

        Parameter imgDir: absolute directory to ./avatars folder
            Enforced project structure:
                os.listdir(./avatars/) contains:
                    - angry/
                    - disgust/
                    - fear/
                    - happy/
                    - neutral/
                    - sad/
                    - surprise/
                
                os.listdir(./avatars/[any emotion]/) contains:
                    - 0.jpg : [emotion] avatar with both eyes open
                    - 1.jpg : [emotion] avatar with left eye closed
                    - 2.jpg : [emotion] avatar with right eye closed
                    - 3.jpg : [emotion] avatar with both eyes closed
        """
        self.name = name
        self.imgDir = imgDir
        self.emotion = "none"
        self.eyeState = 0
        self.img = None

    def __str__(self) -> str:
        return self.getName()

    def getName(self) -> str:
        return self.name

    def getImgDir(self) -> str:
        return self.imgDir

    def setName(self, newName:str):
        self.name = newName

    def setImgDir(self, newImgDir:str):
        self.imgDir = newImgDir

    def setEmotion(self, emotion:str):
        """
        Parameter emotion : str literal of the avatar instance's emotion. Case insensitive.
        
        Possibilities are:
        {"angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"}
        """
        self.emotion = emotion.lower()
    
    def getEmotion(self):
        return self.emotion

    def setEyeState(self, state:int):
        """
        Parameter state : int value for the current eyes state
        (0 = both eyes open, 1 = left eye closed, 2 = right eye closed, 3 = both eyes closed)
        """
        self.eyeState = state

    def getEyeState(self):
        return self.eyeState

    def getEmotionPath(self):
        """
        Returns current emotion + state's absolute .jpg path
        """
        return self.getImgDir() + self.getEmotion() + "/" + str(self.getEyeState()) + ".jpg"

    def showAvatar(self):
        print("Avatar emotion: " + self.getEmotion())
        path = self.getEmotionPath()
        self.img = cv2.imread(self.getEmotionPath())
        cv2.imshow(self.getName(), self.img)
        cv2.waitKey(3000)
