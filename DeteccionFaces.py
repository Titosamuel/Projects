#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:21:53 2020

@author: Edgard
"""


import cv2

face_cascade = cv2.CascadeClassifier('/Users/usuario/Documents/GitHub/opencv/data/haarcascades/haarcascade_frontalcatface.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()