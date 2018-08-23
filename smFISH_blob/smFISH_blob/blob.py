#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("dclk1_il13.jpg", cv2.IMREAD_GRAYSCALE)
im_col = cv2.imread("dclk1_il13.jpg")

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 0
params.maxThreshold = 255


## find bright blobs:
params.filterByColor = 1
params.blobColor = 255
params.filterByInertia = False
params.filterByConvexity = False
params.filterByCircularity = False


# Filter by Area.
params.filterByArea = True
params.minArea = 25
params.maxArea = 100000


# Filter by Circularity
#params.filterByCircularity = True
#params.minCircularity = 0.1

# Filter by Convexity
#params.filterByConvexity = True
#params.minConvexity = 0.87
    
# Filter by Inertia
#params.filterByInertia = True
#params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)


if len(keypoints)==0:
	print("No blobs!")
	# just show the image
	screen_res = 1280, 720
	scale_width = screen_res[0] / im.shape[1]
	scale_height = screen_res[1] / im.shape[0]
	scale = min(scale_width, scale_height)
	window_width = int(im.shape[1] * scale)
	window_height = int(im.shape[0] * scale)
	cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('dst_rt', window_width, window_height)
	cv2.imshow('dst_rt', im)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
else:
	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob
	print("Found " + str(len(keypoints)) + " blobs!")
	im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	# Show blobs
	cv2.imshow("Keypoints", im_with_keypoints)
	cv2.waitKey(0)
	cv2.imwrite("Keypoints.jpg", cv2.drawKeypoints(im_col, keypoints, np.array([]), (0,255,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS))

