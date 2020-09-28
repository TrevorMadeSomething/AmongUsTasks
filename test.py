from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

break_program = False


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') is False:
    if pyautogui.locateOnScreen('download.png', confidence=0.7) is not None:
        print("Download")
        time.sleep(0.5)
    elif pyautogui.locateOnScreen('download.png', confidence=0.7) is not None:
        print("Admin Card")
        time.sleep(0.5)
    elif pyautogui.locateOnScreen('wires.png', confidence=0.7) is not None:
        print("Wires")
        time.sleep(0.5)
    elif pyautogui.locateOnScreen('QR.png', confidence=0.7) is not None:
        print("QR")
        time.sleep(0.5)
    else:
        print("Hello?")
