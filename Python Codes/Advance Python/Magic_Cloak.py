#In this project, we use a red cloth as a cover background, but you can change it any color u want!!!
##Like and follor my GitHub acc for more!
#https://github.com/akarshan2602


import cv2 
import numpy as np
import time

fourCC = cv2.VideoWriter_fourcc(*'XVID')
# this is used to capture video in OpenCV
# fourCC is a 4-byte video code, used to specify the video code
# for Windows, the video code is "*'XVID'" and for Mac, it is "*'MJPG'"

out = cv2.VideoWriter('output.avi', fourCC, 20, (200, 200))
# (fileName, fourCCvariable, framesPerSec, frameSize)

cap = cv2.VideoCapture(0)  # you can use 0 or 1 to capture the video

time.sleep(3) 
# 3 second delay to give time for the settings to process before webcam starts

# variables
count = 0
background = 0 

# while this forloop runs, capture the background 
for i in range(60): # capturing the bkgrd 60 times, and overlapping to make one
    returnV, background = cap.read() 
    # returnV is a boolean value which returns True if captured properly
    # background is the captured background in an array of pixels 
    
background = np.flip(background, axis=1) 
# flipping the background to avoid mirror image

while(cap.isOpened()): # while your camera is opened, this will run
    returnV, img = cap.read() # returnV is true or false
    if not(returnV): # if at any point, return becomes false, break the loop
        break
    count += 1 # keeping count of the number of times this run (no use1)
    img = np.flip(img, axis=1) # flipping the current video 
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # converting your image to HSV
    lower_red = np.array([0, 120, 50]) # saturation is 120-255, value is 50-255
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red) 
    # detecting wheter image pixel colors are in range of the colors
    # creates binary mask, so binary operations can be used 
    
    lower_red = np.array([170, 120, 50])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask1 += mask2 # combining both masks
    
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    
    ''' MORPH_OPEN preforms 2 operations: Erosion and Dilation
    Erosion removes extra white spaces (noise) from image, shrinking it
    Dilation is reverse of Erosion, wherein clean white spaces are added, 
    making the image the same size '''
    
    # np.ones makes it so that every kernel is more smooth
    # np.uint8 makes it so that every kernel is within 0-255
    
    mask2 = cv2.bitwise_not(mask1) 
    result1 = cv2.bitwise_and(img, img, mask=mask2)
    result2 = cv2.bitwise_and(background, background, mask=mask1)
    
    finalOutput = cv2.addWeighted(result1, 1, result2, 1, 0)
    # equal dominance of result1 and result 2 (0 is just nessecary for syntax)
    
    out.write(finalOutput)
    # writing the output and making it offical
    
    cv2.imshow('Magic!', finalOutput)
    # shown in fourCC video writer as 'Magic'
    
    # if you hold q for 1 second, the loop breaks
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when the loop breaks, everything stops
cap.release()
out.release()
cv2.destroyAllWindows()
