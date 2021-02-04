import cv2
import datetime
import requests
import urllib.request
import numpy as np
import time
cap=cv2.VideoCapture(0)
url="http://192.168.43.157:8080/shot.jpg"
while True:
    img_resp=requests.get(url)
    img_array=np.array(bytearray(img_resp.content),dtype=np.uint8)
    img=cv2.imdecode(img_array, 1)
    font=cv2.FONT_HERSHEY_COMPLEX
    datet=str(datetime.datetime.now())
    img=cv2.line(img,(0,0),(255,255),(0,255,0),10)
    img=cv2.putText(img,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
    cv2.imshow("AndroidCam",img)

    if cv2.waitKey(1) == 27:
        break