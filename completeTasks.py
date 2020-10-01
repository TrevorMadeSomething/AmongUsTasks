from pyautogui import *
import pyautogui as py
import time
import keyboard
import random
import win32api
import win32con
from PIL import ImageGrab

break_program = False


def adminCard():
    py.moveTo(1071, 1092, duration=0.3)
    py.click()
    py.moveTo(790, 590, duration=1)
    py.dragTo(2444, 540, 1.3)


def QR():
    py.moveTo(790, 680, duration=.3)
    py.click()
    py.moveTo(672, 250, duration=.3)
    py.click()
    py.moveTo(950, 665, duration=.3)
    py.dragTo(1762, 654, duration=.2)
    time.sleep(2)


def download():
    py.moveTo(1290, 880, duration=.3)
    py.click()


def waterWheel():
    py.moveTo(1280, 620, duration=.5)
    py.click()
    for i in range(7):
        py.dragTo(1038, 620, duration=.2)
        py.dragTo(1038, 840, duration=.2)
        py.dragTo(1475, 840, duration=.2)
        py.dragTo(1475, 620, duration=.2)
    time.sleep(2)


def waterJug():
    py.moveTo(1280, 230, duration=.3)
    py.mouseDown()
    time.sleep(5.3)
    py.mouseUp()


def wifi():
    py.moveTo(1573, 326, duration=.3)
    py.mouseDown()
    py.moveTo(1564, 1030, duration=.3)
    py.mouseUp()


def wifi2():
    py.moveTo(1573, 1100, duration=.3)
    py.mouseDown()
    py.moveTo(1564, 56, duration=.3)
    py.mouseUp()
    time.sleep(4)


def drill():
    for i in range(5):
        click(1055, 318)
        time.sleep(.1)
        click(1512, 318)
        time.sleep(.1)
        click(1512, 1088)
        time.sleep(.1)
        click(1055, 1088)
        time.sleep(.1)


def telescope():
    notIsDone = False
    pix1 = (24, 19, 24)
    pix2 = (246, 249, 250)
    pix3 = (123, 116, 112)

    while (notIsDone is False):
        time.sleep(.3)
        testPix1 = ImageGrab.grab().getpixel((1899, 1210))
        testPix2 = ImageGrab.grab().getpixel((1846, 1079))
        testPix3 = ImageGrab.grab().getpixel((1967, 1216))
        if testPix1 == pix1 and testPix2 == pix2 and testPix3 == pix3:
            time.sleep(.1)
            py.moveTo(1684, 149, duration=.2)
            py.dragTo(1374, 800, duration=.2)
            notIsDone = True
        else:
            py.moveTo(606, 59, duration=.2)
            py.click()
            py.moveTo(2385, 1227, duration=.2)
            py.click()


def inspect1():
    py.moveTo(1680, 1248, duration=.2)
    py.click()
    py.moveTo(644, 177, duration=.2)
    py.click()


def inspect2():
    x = py.locateOnScreen('inspectRed.png', grayscale=False)
    py.moveTo(x, duration=.2)
    py.moveRel(41, 363, duration=.3)
    py.click()


def lowerTemp():
    py.moveTo(847, 859, duration=.3)
    while py.locateOnScreen('lowerTemp.png', confidence=0.9) is not None:
        for i in range(20):
            py.tripleClick()


def raiseTemp():
    py.moveTo(850, 449, duration=.3)
    while py.locateOnScreen('raiseTemp.png', confidence=0.9) is not None:
        for i in range(20):
            py.tripleClick()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') is False:
    if py.locateOnScreen('adminCard.png', confidence=0.9,
                         grayscale=True) is not None:
        print("admindCard on screen")
        time.sleep(3)
        adminCard()
    elif py.locateOnScreen('QR.png', confidence=0.9,
                           grayscale=True) is not None:
        print("QR on screen")
        QR()
        time.sleep(3)
    elif py.locateOnScreen('download.png', confidence=0.9,
                           grayscale=True) is not None:
        print("download on screen")
        download()
        time.sleep(3)
    elif py.locateOnScreen('waterWheel.png', confidence=0.9,
                           grayscale=True) is not None:
        print("waterWheel on screen")
        waterWheel()
        time.sleep(3)
    elif py.locateOnScreen('waterJug.png', confidence=0.9,
                           grayscale=True) is not None:
        print("waterJug on screen")
        waterJug()
        time.sleep(3)
    elif py.locateOnScreen('wifi.png', confidence=0.9,
                           grayscale=True) is not None:
        print("wifi on screen")
        wifi()
        time.sleep(3)
    elif py.locateOnScreen('wifi2.png', confidence=0.9,
                           grayscale=True) is not None:
        print("wifi2 on screen")
        wifi2()
        time.sleep(4)
    elif py.locateOnScreen('drill.png', confidence=0.9,
                           grayscale=True) is not None:
        print("drill")
        drill()
        time.sleep(4)
    elif py.locateOnScreen('lowerTemp.png', confidence=0.9,
                           grayscale=True) is not None:
        print("lowerTemp")
        lowerTemp()
        time.sleep(4)
    elif py.locateOnScreen('telescope.png', confidence=0.9,
                           grayscale=True) is not None:
        print("telescope")
        telescope()
        time.sleep(3)
    elif py.locateOnScreen('inspect1.png') is not None:
        print("inspect1")
        inspect1()
        time.sleep(3)
    elif py.locateOnScreen('inspect2.png', confidence=0.9) is not None:
        print("inspect2")
        inspect2()
        time.sleep(3)
    elif py.locateOnScreen('raiseTemp.png', confidence=0.9) is not None:
        print("raiseTemp")
        raiseTemp()
        time.sleep(3)
    else:
        print("Hello?")
