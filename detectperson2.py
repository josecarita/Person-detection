import time
import numpy as np
import cv2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
# initialize the camera and grab a reference to the raw camera capture
cap = cv2.VideoCapture(0)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (bounding_boxes, weights) = hog.detectMultiScale(frame, winStride=(4, 4),
                                                   padding=(8, 8), 
                                                   scale=1.05)
    
    for (x, y, w, h) in bounding_boxes: 
        cv2.rectangle(frame, 
                  (x, y),  
                  (x + w, y + h),  
                  (0, 0, 255), 
                   4)
    
    boxes=np.array(bounding_boxes)
    
    if boxes.size > 3:
        GPIO.output(7,True)
    else:
        GPIO.output(7,False)
        
    cv2.imshow("Frame", frame);
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
       break
    
cap.release()
cv2.destroyAllWindows()