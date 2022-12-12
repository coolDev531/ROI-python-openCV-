# ROI (Region of Interest)
# With Frame moving across the screen in a bouncing way

import cv2
import numpy as np
import time

print(cv2.__version__)

WinWidth=640
WinHeight=480
rectColor=(0,255,0)
# Region of Interest (ROI) Rectangle 
ROIHeight=100
ROIWidth=200
ROIxStartPoint=0
ROIyStartPoint=0
moveFactor=5 # For every iteration of fetch & show, how much pixels to move the Frame
# Move factory decides if the Rectangle moved forward
# or backwards in x or y axis
xMoveFactor=1  # +1 for forwared, -1 backward
yMoveFactor=1  


cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,WinWidth)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, WinHeight)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))


while True:
    _, colorFrame = cam.read()
    grayFrame = cv2.cvtColor(colorFrame,cv2.COLOR_BGR2GRAY);
    grayFrame = cv2.cvtColor(grayFrame,cv2.COLOR_GRAY2BGR);

    ROIyStartPoint=ROIyStartPoint+(moveFactor*yMoveFactor)

    if ROIyStartPoint+ROIHeight > WinHeight or (yMoveFactor<0 and (ROIyStartPoint <= 0)):
        yMoveFactor = -1*yMoveFactor
        print("ymovefactor"+str(yMoveFactor))
        ROIyStartPoint=ROIyStartPoint+(moveFactor*yMoveFactor)


    ROIxStartPoint=ROIxStartPoint+(moveFactor*xMoveFactor)

    if ROIxStartPoint+ROIWidth > WinWidth or (xMoveFactor<0 and (ROIxStartPoint <= 0)):
        xMoveFactor = -1*xMoveFactor
        print("xmovefactor"+str(xMoveFactor))
        ROIxStartPoint=ROIxStartPoint+(moveFactor*xMoveFactor)



    ROIFrame = colorFrame[ROIyStartPoint:ROIyStartPoint+ROIHeight,ROIxStartPoint:ROIxStartPoint+ROIWidth];

    # ROIGrayFrame = cv2.cvtColor(ROIFrame,cv2.COLOR_BGR2GRAY);
    # ROIFrame =  cv2.cvtColor(ROIGrayFrame,cv2.COLOR_GRAY2BGR);
   
    cv2.imshow("ROI Gray", ROIFrame)
    cv2.moveWindow("ROI Gray", 640, 0)

    grayFrame[ROIyStartPoint:ROIyStartPoint+ROIHeight,ROIxStartPoint:ROIxStartPoint+ROIWidth]= ROIFrame
    cv2.rectangle(grayFrame,(ROIxStartPoint,ROIyStartPoint),(ROIxStartPoint+ROIWidth, ROIyStartPoint+ROIHeight),rectColor,1)

    cv2.imshow("mainView",grayFrame);
    cv2.moveWindow("mainView",0,0);
    keypressed=cv2.waitKey(1) 
    
    if keypressed == ord('q'):
        print(ord('q'))
        break

cam.release()