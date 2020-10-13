from pyautogui import *
import pyautogui as py
import time
import keyboard
import random
import win32api
import win32con
import PIL
from PIL import ImageGrab, Image

# 607, 437
# 1948, 437
# 1948, 884
# 607, 884
# 607, 437, 1341, 447

maze = PIL.ImageGrab.grab(bbox=(558, 395, 1995, 931))
maze.save("maze.png")
px = maze.load()
print(px[300, 300])

checkXLocs = [608, 687]
pixX = 0
pixY = 0
# while (pixX < 1948 or pixY < 884):
#     curr = maze.getPixel(pixX, pixY)
