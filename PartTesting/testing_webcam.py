import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow("webcam 0", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Program end")
        break


# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()