import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open Camera")
    exit()

def nothing(x):
    pass
def nothing2(x):
    print("nothing 2")
    pass
cv.namedWindow("Trackbars")
cv.createTrackbar("L-H", "Trackbars", 0, 255, nothing)
cv.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv.createTrackbar("U-H", "Trackbars", 255, 255, nothing)
cv.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv.createTrackbar("U-V", "Trackbars", 45, 255, nothing)

cv.createTrackbar("Area(px)", "Trackbars", 500000, 1000000, nothing)

font = cv.FONT_HERSHEY_COMPLEX
while True:
    #Capture Frame by frame
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


    #if frame is read correctly ret is True
    if not ret:
        print("Cant receive frame (stream end?). Exiting...")
        break

    #define UI elements
    l_h = cv.getTrackbarPos("L-H", "Trackbars")
    l_s = cv.getTrackbarPos("L-S", "Trackbars")
    l_v = cv.getTrackbarPos("L-V", "Trackbars")
    u_h = cv.getTrackbarPos("U-H", "Trackbars")
    u_s = cv.getTrackbarPos("U-S", "Trackbars")
    u_v = cv.getTrackbarPos("U-V", "Trackbars")

    area_slider = cv.getTrackbarPos("Area(px)", "Trackbars")
    cv.createButton("Ramp V", nothing2, None, cv.QT_PUSH_BUTTON, 1)

    #ops on the frame go here.
    lower_black = np.array([l_h,l_s,l_v])
    upper_black = np.array([u_h,u_s,u_v])

    mask = cv.inRange(hsv, lower_black, upper_black)
    kernel = np.ones((8,8), np.uint8)
    mask = cv.erode(mask, kernel)


    #contour detection
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv.contourArea(c)
        approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]


        if area > area_slider:
            cv.drawContours(frame, [approx], 0, (0, 0, 255), 2)

            if len(approx) == 4:
                cv.putText(frame, "Card", (x, y), font, 1, (0, 125, 255))

    # maybe double buffer thE frames? is that done in video capture?
    cv.imshow('frame', frame)
    #cv.imshow('Mask', mask)
    if cv.waitKey(1) == ord('q'):
        break

#when everything is done, release the capture
cap.release()
cv.destroyAllWindows()
