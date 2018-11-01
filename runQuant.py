
from os import listdir
from os.path import isfile, join, splitext
import sys
from detect_cells.contour import quant

min_distance = 2.5
min_pixel = 30

image_dir = "test_input"
image_files = [f for f in listdir(image_dir) if isfile(join(image_dir, f))]

for img in image_files:
	fn = splitext(img)[0]
	output_img = fn + "_quant.jpg"
	quant(join(image_dir,img), output_img, min_pixel, min_distance)
	print("=======================================" + "\n\n\n")
