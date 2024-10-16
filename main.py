# Import pyautogui module to automate keys
import pyautogui
# From Python Imaging Library (PIL) import ImageGrab to take screenshot
from PIL import ImageGrab
# Time Module for adding delay
import time
# Creation of Hit Key Function to press require key
def hit(key):
    # keyDown will press the key
    pyautogui.keyDown(key)
    # adding delay of 0.1 second
    time.sleep(0.1)
    # keyUp will release the key
    pyautogui.keyUp(key)
# Creation of a function to check if cactus or flying bird (Low Scale) come in given coordinates
def is_cactus(data):
    for x in range(300, 415):
        for y in range(725, 775):
            # if pixels less than 100 means that is black
            if data[x, y] < 100:
                return True
    return False
# Creation of a function to check if flying bird (High Scale) come in given coordinates
def is_bird(data):
    for x in range(300, 320):
        for y in range(600, 700):
            if data[x, y] < 100:
                return True
    return False
# Executing the code if you're working in main.py
if __name__ == "__main__":
    time.sleep(2)
    while True:
        # Taking Screenshot and conversion of image to grayscale
        image = ImageGrab.grab().convert("L")
        # Loading the image to get pixels (arrays)
        data = image.load()
        if is_cactus(data):
            hit("space")
        elif is_bird(data):
            hit("down")