import numpy as np
import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
side = cv2.CascadeClassifier('lbpcascade_profileface.xml')

cap = cv2.VideoCapture(1)
move= cv2.createBackgroundSubtractorMOG2()

while 1:
    
    ret, frame = cap.read()
    #frame = frame + 10
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #********************************
    mask = move.apply(gray)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask,kernel, iterations = 1)
    kernel = np.ones((20,20),np.uint8)
    mask = cv2.dilate(mask,kernel, iterations = 1)
    #********************************
    
    #faces = face.detectMultiScale(gray, 1.1, 1, 0 , (100,100),(500,500))
    faces = face.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in faces:
        cv2.rectangle(mask,(x,y-60),(x+w,y+h+60),(255,255,255),-1)
        
    faces = side.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in faces:
        cv2.rectangle(mask,(x-10,y-10),(x+w+20,y+h+20),(255,255,255),-1)
    #********************************

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    low = np.array([0, 55, 48])
    up = np.array([130, 110, 269])    
    mask1 = cv2.inRange(hsv,low,up)

    kernel = np.ones((15,15),np.uint8)
    mask1 = cv2.erode(mask1,kernel, iterations = 1)
    kernel = np.ones((30,30),np.uint8)
    mask1 = cv2.dilate(mask1,kernel, iterations = 1)
    
    #********************************

    mask = mask + mask1
    img = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('img',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
