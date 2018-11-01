

### Software to count mRNA dots in FISH images ###
### Written by Adam Haber, July 2017. email: ahaber@broadinstitute.org ###
 
### Installation (only tested on OS X, but should work on linux)

1. Install OpenCv3 with python bindings. On mac, the easiest way is to use homebrew:
$ brew install opencv3

2. Install this python package:
$ cd detect_cells
$ pip install --user .

3. Run the code. By default will look in the 'test_input' directory for input images. 
$ python runQuant.py

4. There are two parameters to control dot resolution. The first is 'min_pixel', which thresholds the image with all pixels less than min_pixel in brightness being made black. The second is 'min_distance' which controls how much merging is done for nearby dots; higher 'min_distance' give more merging.
