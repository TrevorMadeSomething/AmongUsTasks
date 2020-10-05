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
    x = py.locateOnScreen('inspectRed.png', grayscale=False, confidence=.9)
    print(x)
    py.moveTo(x, duration=.2)
    py.moveRel(41, 363, duration=.3)
    py.click()


def wiresLeft():
    yellowLeft = locateOnScreen('yellowLeft.png', confidence=.95)
    blueLeft = locateOnScreen('blueLeft.png', confidence=.95)
    redLeft = locateOnScreen('redLeft.png', confidence=.95)
    pinkLeft = locateOnScreen('pinkLeft.png', confidence=.95)
    yellowRight = locateOnScreen('yellowRight.png', confidence=.95)
    blueRight = locateOnScreen('blueRight.png', confidence=.95)
    redRight = locateOnScreen('redRight.png', confidence=.95)
    pinkRight = locateOnScreen('pinkRight.png', confidence=.95)

    py.moveTo(yellowLeft[0] + 5, yellowLeft[1] + 5, duration=.2)
    py.mouseDown()
    py.moveTo(yellowRight[0], yellowRight[1], duration=.4)
    py.mouseUp()
    py.moveTo(blueLeft[0] + 5, blueLeft[1] + 5, duration=.2)
    py.mouseDown()
    py.moveTo(blueRight[0], blueRight[1], duration=.4)
    py.mouseUp()
    py.moveTo(redLeft[0] + 5, redLeft[1] + 5, duration=.2)
    py.mouseDown()
    py.moveTo(redRight[0], redRight[1], duration=.4)
    py.mouseUp()
    py.moveTo(pinkLeft[0] + 5, pinkLeft[1] + 5, duration=.2)
    py.mouseDown()
    py.moveTo(pinkRight[0], pinkRight[1], duration=.4)
    py.mouseUp()


def chute():
    py.moveTo(1693, 564, duration=.2)
    py.mouseDown()
    py.moveTo(1693, 1394, duration=.2)
    time.sleep(2)
    py.mouseUp()


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


def O2():
    for i in range(2):
        py.moveTo(1138, 350, duration=.2)
        py.mouseDown()
        py.moveTo(1120, 1400, duration=.2)
        py.mouseUp()
        time.sleep(2.5)
        py.moveTo(1310, 965, duration=.2)
        py.click()
        time.sleep(1.5)


def key():
    target = py.locateOnScreen('keyTarget.png',
                               region=(1083, 52, 700, 1350),
                               confidence=.95)
    py.moveTo(635, 1035, duration=.3)
    py.mouseDown()
    py.moveTo(target[0] + (110), target[1] + (110), duration=.3)
    py.mouseUp()
    py.moveTo(1225, 151, duration=.2)
    py.mouseDown()
    py.moveTo(1947, 1048, duration=.2)
    py.mouseUp()


def tree():
    yellow = py.locateOnScreen('treeY.png',
                               region=(664, 290, 270, 555),
                               confidence=.9)
    green = py.locateOnScreen('treeY.png',
                              region=(984, 413, 270, 655),
                              confidence=.9)
    red = py.locateOnScreen('treeY.png',
                            region=(1296, 290, 270, 700),
                            confidence=.9)
    blue = py.locateOnScreen('treeY.png',
                             region=(1631, 505, 270, 555),
                             confidence=.9)
    py.moveTo(yellow[0], yellow[1], duration=.2)
    py.mouseDown()
    py.moveTo(708, 808, duration=.2)
    py.mouseUp()
    py.moveTo(green[0], green[1], duration=.2)
    py.mouseDown()
    py.moveTo(1095, 390, duration=.2)
    py.mouseUp()
    py.moveTo(red[0], red[1], duration=.2)
    py.mouseDown()
    py.moveTo(1435, 936, duration=.2)
    py.mouseUp()
    py.moveTo(blue[0], blue[1], duration=.2)
    py.mouseDown()
    py.moveTo(1762, 482, duration=.2)
    py.mouseUp()


def chart():
    chartStart = py.locateOnScreen('chartStart.png',
                                   region=(684, 347, 125, 744),
                                   confidence=.6)
    node1 = py.locateOnScreen('chartNode.png',
                              region=(995, 347, 45, 744),
                              confidence=.3)
    node2 = py.locateOnScreen('chartNode.png',
                              region=(1260, 347, 45, 744),
                              confidence=.3)
    node3 = py.locateOnScreen('chartNode.png',
                              region=(1520, 347, 45, 744),
                              confidence=.4)
    node4 = py.locateOnScreen('chartFinal.png',
                              region=(1785, 347, 45, 744),
                              confidence=.5)
    # series of movements from node to node
    # calling funcation that takes (startX, startY, slopeToTravel, endingX)
    chartMouse(chartStart[0], chartStart[1],
               ((node1[1] - chartStart[1]) / (node1[0] - chartStart[0])), 1100)
    chartMouse(node1[0], node1[1],
               ((node2[1] - node1[1]) / (node2[0] - node1[0])), 1300)
    chartMouse(node2[0], node2[1],
               ((node3[1] - node2[1]) / (node3[0] - node2[0])), 1580)
    chartMouse(node3[0], node3[1],
               ((node4[1] - node3[1]) / (node4[0] - node3[0])), 1850)


def chartMouse(mouseX, mouseY, slope, destination):
    py.moveTo(mouseX, mouseY, duration=.1)
    py.mouseDown()
    while (mouseX < destination):
        mouseX += 10
        mouseY += 10 * slope
        py.moveTo(mouseX, mouseY, duration=.05)
    py.mouseUp()
    time.sleep(.2)


while keyboard.is_pressed('q') is False:
    if py.locateOnScreen('adminCard.png', grayscale=True) is not None:
        print("admindCard on screen")
        time.sleep(3)
        adminCard()
    elif py.locateOnScreen('chart.png', grayscale=True) is not None:
        print("chart on screen")
        chart()
        time.sleep(3)
    elif py.locateOnScreen('key.png', grayscale=True) is not None:
        print("keys on screen")
        key()
        time.sleep(3)
    elif py.locateOnScreen('QR.png', grayscale=True) is not None:
        print("QR on screen")
        QR()
        time.sleep(3)
    elif py.locateOnScreen('download.png', grayscale=True,
                           confidence=.9) is not None:
        print("download on screen")
        download()
        time.sleep(3)
    elif py.locateOnScreen('waterWheel.png', grayscale=True) is not None:
        print("waterWheel on screen")
        waterWheel()
        time.sleep(3)
    elif py.locateOnScreen('waterJug.png', grayscale=True) is not None:
        print("waterJug on screen")
        waterJug()
        time.sleep(3)
    elif py.locateOnScreen('wifi.png', grayscale=True) is not None:
        print("wifi on screen")
        wifi()
        time.sleep(3)
    elif py.locateOnScreen('wifi2.png', grayscale=True) is not None:
        print("wifi2 on screen")
        wifi2()
        time.sleep(4)
    elif py.locateOnScreen('drill.png', grayscale=True) is not None:
        print("drill")
        drill()
        time.sleep(4)
    elif py.locateOnScreen('lowerTemp.png', grayscale=True) is not None:
        print("lowerTemp")
        lowerTemp()
        time.sleep(4)
    elif py.locateOnScreen('telescope.png', grayscale=True) is not None:
        print("telescope")
        telescope()
        time.sleep(3)
    elif py.locateOnScreen('inspect1.png') is not None:
        print("inspect1")
        inspect1()
        time.sleep(3)
    elif py.locateOnScreen('inspect2.png', confidence=.9) is not None:
        print("inspect2")
        inspect2()
        time.sleep(3)
    elif py.locateOnScreen('raiseTemp.png') is not None:
        print("raiseTemp")
        raiseTemp()
        time.sleep(3)
    elif py.locateOnScreen('wires.png', confidence=.9,
                           grayscale=True) is not None:
        print("wiresLeft")
        wiresLeft()
        time.sleep(3)
    elif py.locateOnScreen('chute.png', grayscale=True) is not None:
        print("chute is on screen")
        chute()
        time.sleep(3)
    elif py.locateOnScreen('O2.png', grayscale=True) is not None:
        print("O2 is on screen")
        O2()
        time.sleep(3)
    elif py.locateOnScreen('tree.png', grayscale=True) is not None:
        print("tree on screen")
        tree()
        time.sleep(3)
    else:
        print("Hello?")
