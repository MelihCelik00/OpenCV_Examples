import cv2

print("OpenCV Version:\n")
print(cv2.__version__)

img = cv2.imread("mountain.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Mountaing",img)
cv2.imshow("Mountain -gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()