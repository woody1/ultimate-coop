import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Show our masterpiece
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)