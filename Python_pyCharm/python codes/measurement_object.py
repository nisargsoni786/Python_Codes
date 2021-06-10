import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)
img=cv2.imread('datafile/objmeasure.png')
# cv2.imshow("img",img)
# cv2.waitKey(0)
def getcon(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.GaussianBlur(img,(9,9),1)
    img=cv2.Canny(img,100,200)
    kernal=np.ones((5,5))
    # img=cv2.dilate(img,kernal,iterations=1)
    # img=cv2.erode(img,kernal,iterations=1)

    con,heiarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,con,-1,(0,255,255),0)

    return img

img=getcon(img)
cv2.imshow("imageeee",img)
cv2.waitKey(0)
















# while cap.isOpened():
#     _,img=cap.read()
#     cv2.imshow("img",img)
#     if cv2.waitKey(1)==ord('q'):
#         break

