import cv2
import numpy as np
c=cv2.imread("datafile/img.JPG")
c=c[500:1200,500:1200]
c=cv2.cvtColor(c,cv2.COLOR_BGR2RGB)
#c.resize(500,500)
import numpy as np

x=np.zeros((512,512,3),np.uint8)
cv2.rectangle(x,(10,10),(0,400),(0,255,255),-1)
cv2.rectangle(x,(5,10),(10,500),(0,255,144),-1)
cv2.rectangle(x,(50,50),(400,511),(243,255,0),-1)
cv2.rectangle(x,(0,0),(200,405),(20,255,255),-1)
cv2.rectangle(x,(400,10),(400,400),(100,255,5),-1)
maskk=cv2.inRange(x,np.array([0,255,255]),np.array([30,255,255]))
while(1):
    cv2.imshow("img",x)
    cv2.imshow("maskkk",maskk)
    if cv2.waitKey(1)==ord('q'):
        break