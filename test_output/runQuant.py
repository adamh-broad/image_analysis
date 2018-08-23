

from os import listdir
from os.path import isfile, join, splitext
import sys
from smFISH_blob.contour import quant

min_distance = 25 ### low -- less merging, high -- more merging
min_pixel = 50    ### low -- more dots, high -- less dots
min_area = 20	  ### high -- less dots

image_dir = "../test_input/batch_IHC"
image_files = [f for f in listdir(image_dir) if isfile(join(image_dir, f))]

nums = list()
for img in image_files:
	fn = splitext(img)[0]
	output_img = fn + "_quant.jpg"
	n_cells = quant(join(image_dir,img), output_img, min_pixel, min_distance, min_area=min_area)
	nums.append(n_cells)
	print("=======================================" + "\n\n\n")
	

num_fn = "nums.txt"
print("Saving all numbers to: " + num_fn)
f = open(num_fn, 'w')
for i in range(0,len(nums)):
  	f.write(image_files[i] + "\t" + str(nums[i]) + "\n")
print("Done.")
