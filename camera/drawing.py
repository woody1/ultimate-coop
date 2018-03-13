# USAGE
# python drawing.py

# Import the necessary packages
import numpy as np
import cv2

# Initialize our canvas as a 300x300 with 3 channels,
# Red, Green, and Blue, with a black background
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# Reset our canvas and draw a white circle at the center
# of the canvas with increasing radii - from 25 pixels to
# 150 pixels
canvas = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

# Show our masterpiece
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)