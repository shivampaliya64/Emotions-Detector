import numpy as np
import cv2

img= cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))
dst=cv2.addWeighted(img,.5,img2,.5,0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()