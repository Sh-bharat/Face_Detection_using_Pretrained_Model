#Importing Libraries
import cv2
import math
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Error: Camera can not be opened. ")

# For Every Frame
while True:
    ret, frame = cap.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
    # here haarcascade_frontalface_default.xml is a file whih is already trained
    haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
    
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9) 
    # Drawing rectangle around the face 
    for (x, y, w, h) in faces_rect:
        r=max(w,h)
        R=int(r/2)
        cv2.circle(frame,(int(x+(w/2)),int(y+(h/2))),R,(255, 255, 0), 2)
    cv2.imshow('Camera', frame)

    c = cv2.waitKey(1)
    if c == 27: # For Esc character
        break

cap.release()
cv2.destroyAllWindows()