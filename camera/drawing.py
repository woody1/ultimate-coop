# USAGE
# python drawing.py

# Import the necessary packages
import numpy as np
import cv2

# Initialize our canvas as a 300x300 with 3 channels,
# Red, Green, and Blue, with a black background
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# Let's draw one last rectangle: blue and filled in rgb - bgr
green = (0, 255, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), green, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Show our masterpiece
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)