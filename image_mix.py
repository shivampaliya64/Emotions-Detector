from matplotlib import pyplot as plt
import numpy as np
import cv2

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

print(apple.shape)
print(orange.shape)

mix = np.hstack((apple[:,:256],orange[:,256:]))

apple_copy = apple.copy()
gp_apple = [apple_copy]

#Gaussian pyramid for apple
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]

#Gaussian pyramid for orange
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#genrating laplacian pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5,0,-1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1],gaussian_expanded)
    lp_apple.append(laplacian)

#genrating laplacian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5,0,-1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1],gaussian_expanded)
    lp_orange.append(laplacian)

for i in range(5,0,-1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1],gaussian_expanded)
    lp_orange.append(laplacian)

mix_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple,lp_orange):
    n+=1
    cols,rows,ch=apple_lap.shape
    laplacian = np.hstack((apple_lap[:,0:int(cols/2)], orange_lap[:, int(cols/2):]))
    mix_pyramid.append(laplacian)

mix_final = mix_pyramid[0]
for i in range(1,6):
    mix_final = cv2.pyrUp(mix_final)
    mix_final = cv2.add(mix_pyramid[i],mix_final)

cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('mix',mix_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
