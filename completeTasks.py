from pyautogui import *
import pyautogui as py
import time
import keyboard
import random
import win32api
import win32con

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
    for i in range(20):
        click(1055, 302)
        click(1508, 302)
        click(1055, 302)
        click(1055, 302)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') is False:
    if py.locateOnScreen('adminCard.png', confidence=0.9) is not None:
        print("admindCard on screen")
        time.sleep(0.5)
        adminCard()
    elif py.locateOnScreen('QR.png', confidence=0.9) is not None:
        print("QR on screen")
        QR()
        time.sleep(0.5)
    elif py.locateOnScreen('download.png', confidence=0.9) is not None:
        print("download on screen")
        download()
        time.sleep(0.5)
    elif py.locateOnScreen('waterWheel.png', confidence=0.9) is not None:
        print("waterWheel on screen")
        waterWheel()
        time.sleep(0.5)
    elif py.locateOnScreen('waterJug.png', confidence=0.9) is not None:
        print("waterJug on screen")
        waterJug()
        time.sleep(0.5)
    elif py.locateOnScreen('wifi.png', confidence=0.9) is not None:
        print("wifi on screen")
        wifi()
        time.sleep(0.5)
    elif py.locateOnScreen('wifi2.png', confidence=0.9) is not None:
        print("wifi2 on screen")
        wifi2()
        time.sleep(0.5)
    elif py.locateOnScreen('drill.png', confidence=0.9) is not None:
        print("drill")
        drill()
        time.sleep(0.5)
    else:
        print("Hello?")
