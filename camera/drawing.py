# USAGE
# python drawing.py

# Import the necessary packages
import numpy as np
import cv2

# Initialize our canvas as a 300x300 with 3 channels,
# Red, Green, and Blue, with a black background
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# Let's draw one last rectangle: blue and filled in rgb - bgr
cv2.circle(canvas, (20, 20), 20, white)

# Show our masterpiece
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)