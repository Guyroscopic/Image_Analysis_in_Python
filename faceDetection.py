import numpy as np
import cv2

#loading the har cascade files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#starting video capture
cap = cv2.VideoCapture(0)

while True:
    #Reading frame by frame and converting them to grayscale
    ret, capture = cap.read()    
    gray = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)

    #Finding Faces in the grayscales image and drawing blue rectangles around them
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)    
    for (x,y,w,h) in faces:
        cv2.rectangle(capture, (x,y), (x+w,y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = capture[y:y+h, x:x+w]
        
    #Finding eyes in the faces and drawing green rectangles aroung them
        eyes = eye_cascade.detectMultiScale(roi_gray)        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh),(0,255,0), 2)

    #Showing output
    cv2.imshow('capture', capture)

    #Press escape key to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
 
