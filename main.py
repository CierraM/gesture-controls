# from https://github.com/cvzone/cvzone/blob/master/Examples/HandTrackingExample.py

from cvzone.HandTrackingModule import HandDetector
import cv2
from pynput.keyboard import Key,Controller
import time
from Peace import Peace
from FourFingersCloseTogether import FourFingersCloseTogether
from FourFingersSpreadApart import FourFingersSpreadApart

keyboard = Controller()
capture = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    # Get image frame
    success, img = capture.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
        centerPoint1 = hand1['center']  # center of the hand cx,cy
        handType1 = hand1["type"]  # Handtype Left or Right

        # types of hand signs to look for:
        peace = Peace(hand1, detector).isShowing()
        fourFingersClose = FourFingersCloseTogether(hand1, detector).isShowing()
        fourFingersOpen = FourFingersSpreadApart(hand1, detector).isShowing()

        if fourFingersOpen:
            #volume up
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            time.sleep(0.5)

        if fourFingersClose:
            #volume down
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            time.sleep(0.5)

        if peace:
            # full screen shortcut toggle
            keyboard.press(Key.cmd)
            keyboard.press(Key.ctrl)
            keyboard.press('f')

            keyboard.release(Key.cmd)
            keyboard.release(Key.ctrl)
            keyboard.release('f')
            time.sleep(2)



    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
