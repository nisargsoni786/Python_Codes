import cv2
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,1000)
data=[]
for i in range(200):
    _,img=cap.read()
    cv2.rectangle(img,(100,100),(350,360),(0,0,255),3)
    im=img[100:360,100:350]
    data.append(im)
    cv2.imshow("imm",img)
    cv2.imwrite('datafile/scissor/{}.png'.format(i),im)
    if cv2.waitKey(1)==ord('q'):
        break


# cv2.imshow("1",data[0])
# cv2.imshow("2",data[1])
# cv2.imshow("3",data[2])
# cv2.imshow("4",data[3])
# cv2.imshow("5",data[4])
# cv2.waitKey(0)