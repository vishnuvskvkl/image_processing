import cv2
import matplotlib.pyplot as plt
image = cv2.imread('D:/image/gg.jpg')
for i,col in enumerate(['b','g','r']):
    histr = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
channels = cv2.split(image)
eq_channels = []
for ch, color in zip(channels, ['B', 'G', 'R']):
    eq_channels.append(cv2.equalizeHist(ch))
eq_image = cv2.merge(eq_channels)

cv2.imshow("Original", image)
cv2.imshow("Equalized Image", eq_image)
cv2.waitKey()
cv2.destroyAllWindows()

for i, color in enumerate(['b','g','r']):
    histogram = cv2.calcHist([eq_image], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)
    plt.xlim([0, 256])
plt.show()
