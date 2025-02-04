import cv2
import numpy as np

cap   = cv2.VideoCapture("eye_recording.flv")



while True:
    ret, frame = cap.read()
    if ret is False:
        break


    roi = frame[269: 795, 537: 1416]    #cutting the frame of video ( pixels 1416 and 269...)

    
    #rows = roi.shape
    #cols = roi.shape


    #Converting roi to GraySCALE
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    

    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
    
    _, threshold = cv2.threshold(gray_roi, 3, 255, cv2.THRESH_BINARY_INV)

    #COntours removing noise
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Oreders COntours    
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse = True)
    
    
    for cnt in contours:
        (x, y, w, h )= cv2.boundingRect(cnt)
        thick = 2
        cv2.rectangle(roi, (x, y), (x+w, y+h), (255, 0, 0), thick)
        cv2.rectangle(roi, (x, y), (x+h, y+w), (0, 255, 0), thick)

        

    

        

        #cv2.line(roi, (x,y), (x+w,y+h), (0,255, 0), thick)

        

        #first_arg = x, int(w/2),0
        #second_arg = x + int(w/2), rows
        #cv2.rectangle(roi, first_arg, second_arg,(0, 255, 0), thick)
        #cv2.line(roi, (x, int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), thick)
        #cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2), rows), (0, 255, 0), 2)
        

        break
   


    #PRINTING / SHOWING
    cv2.imshow("ROI", roi)
    
    cv2.imshow("THRESHOLD", threshold)
    
    #cv2.imshow("GRAY ROI", gray_roi)            



    
    
    key = cv2.waitKey(30)
    if key == 27:
        break


cv2.destroyAllWindows()
