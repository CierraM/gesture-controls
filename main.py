# from https://github.com/cvzone/cvzone/blob/master/Examples/HandTrackingExample.py
import os

from cvzone.HandTrackingModule import HandDetector
import cv2
from pynput.keyboard import Key,Controller
import time
from dotenv import load_dotenv
from hand_models.Peace import Peace
from hand_models.FourFingersCloseTogether import FourFingersCloseTogether
from hand_models.FourFingersSpreadApart import FourFingersSpreadApart
from philips_hue.philipsHue import PhilipsHue

load_dotenv()
userId = os.getenv('PHILIPSUSERID')
lightController = PhilipsHue(userId)
lightGroups = lightController.lightGroups

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
            #brightness up
            lightGroups["Bedroom"].brightnessUp()
            time.sleep(0.05)

        if fourFingersClose:
            # brightness down
            lightGroups["Bedroom"].brightnessDown()
            time.sleep(0.05)

        if peace:
            #toggle bedroom lights
            lightGroups["Bedroom"].toggle()
            time.sleep(2)



    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
