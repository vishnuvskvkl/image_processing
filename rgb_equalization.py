import cv2
import matplotlib.pyplot as plt
image = cv2.imread('D:/image/gg.jpg')
channels = cv2.split(image)
eq_channels = []
for ch, color in zip(channels, ['B', 'G', 'R']):
    eq_channels.append(cv2.equalizeHist(ch))
eq_image = cv2.merge(eq_channels)
cv2.namedWindow("Original", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Equalized Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Original", image)

cv2.imshow("Equalized Image", eq_image)
cv2.waitKey()
cv2.destroyAllWindows()




def show_rgb_equalized(image):
    channels = cv2.split(image)
    eq_channels = []
    for ch, color in zip(channels, ['B', 'G', 'R']):
        eq_channels.append(cv2.equalizeHist(ch))

    eq_image = cv2.merge(eq_channels)
    eq_image = cv2.cvtColor(eq_image, cv2.COLOR_BGR2RGB)
    plt.imshow(eq_image)
    plt.show()
