import cv2
import numpy as np
from PIL import Image
from skimage.feature import corner_harris, corner_subpix, corner_peaks

img = cv2.imread("147.jpg")
print(img.shape)
# The image with shape (1280, 1024, 3) has a resolution of 1280 pixels by 1024 pixels and has 3 color channels, which means it is a color image.

print(img.size)


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Compute Harris corners
corners = corner_harris(blur_img, k=0.04)

# Subpixel corner refinement
corners = corner_subpix(blur_img, corners, window_size=13)

# Find the peaks of the corners
coords = corner_peaks(corners, min_distance=5)

# Find contours
contours, hierarchy = cv2.findContours(blur_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# SIFT Feature Detection
sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray_img, None)


# Draw keypoints on the image
img_with_keypoints = cv2.drawKeypoints(img, kp, None)

# This is the text for testing
# This is the text for testing
# This is the text for testing
# This is the text for testing