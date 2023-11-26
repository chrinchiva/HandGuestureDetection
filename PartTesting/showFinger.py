import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x,y,w,h=hand['bbox']

        imgWhite = np.ones((imgSize, imgSize,3),np.uint8)*255
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h/w
        if aspectRatio>1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop,(wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCal)/2)
            imgWhite[:, wGap:wCal+wGap] = imgResize
        else:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize-hCal)/2)
            imgWhite[hGap:hCal+hGap, :] = imgResize
        #cv2.imshow("hand", imgCrop)
        #cv2.imshow("imgWhite", imgWhite)

        if imgCrop is not None and imgCrop.any():
            height, width, _ = imgCrop.shape
            print(f"Image Dimensions: {width} x {height}")
            cv2.imshow('Image', imgCrop)
        else:
            print("Failed to load the image.")
        ########################################################################################
        cv2.imshow('imgWhite', imgWhite)
        # if imgWhite is not None and imgWhite.any():
        #     height, width, _ = imgWhite.shape
        #     #cv2.imshow('imgWhite', imgWhite)
        #     if width > 0 and height > 0:
        #         # Resize the image
        #         resized_image = cv2.resize(imgWhite, (600, 600))
        #         cv2.imshow('Resized Image', resized_image)
        #     else:
        #         print("Image dimensions are zero.")
        # else:
        #     print("Failed to load the image White.")
        ########################################################################################
    cv2.imshow("webcam 0", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Program end")
        break


# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()