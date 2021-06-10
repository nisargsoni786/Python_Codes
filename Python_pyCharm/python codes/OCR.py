import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img=cv2.imread('datafile/name_img.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hei,wid,_=img.shape
# print(pytesseract.image_to_string(img))       # (for only show the texts in the image)


# doo=pytesseract.image_to_boxes(img)              # to make rectangles at every letter
# for b in doo.splitlines():
#     b=b.split(' ')
#     letter=b[0]n
#     print(b)
#     x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hei-y),(w,hei-h),(0,255,0),3)
#     cv2.putText(img,letter,(x,hei-y-50),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)    # over every letter rectangle

boxes=pytesseract.image_to_data(img)
# print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if(x!=0):
        b=b.split()
        print(b)
        if len(b)==12:
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x,y), (x+w,y+h), (0, 255, 0), 3)
            cv2.putText(img,b[11], (x,y-12), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)



#cv2.imwrite('last output file.jpg',img)            # to save
cv2.imshow('img2',img)
cv2.waitKey(0)