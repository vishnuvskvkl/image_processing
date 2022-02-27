import cv2
from matplotlib import pyplot as plt
img = cv2.imread('D:/vishnu/mn.jpeg',0)
cv2.imshow('image',img)
dst = cv2.calcHist(img, [0], None, [256], [0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram for gray scale image')
plt.show()
cv2.waitKey(0)
