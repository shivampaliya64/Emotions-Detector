import cv2,time

img=cv2.imread('lena.jpg',1)
img=cv2.line(img,(0,0),(255,255),(0,255,0),5)
img =cv2.arrowedLine(img,(0,255 ),(255,255),(255,0,0),10)

img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),1)
img=cv2.circle(img,(255,255),60,(0,255,0),10)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'jyotsna',(10,200),font,4,(255,255,255),10)
cv2.imshow('image',img)
k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()