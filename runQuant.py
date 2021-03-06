
from os import listdir
from os.path import isfile, join, splitext
import sys
import argparse
import cv2
import numpy as np
import sys
import argparse

# run spot counting
def quant(  input_img, 
            output, 
            min_pixel, 
            min_distance, 
            min_area=0,
            adaptive=False, 
            bright_blobs=True, 
            highlight_col = (0,255,0),     # green
            show_threshold=False):
    print("Starting quant.")
    print("Loading image from: " + input_img)
    try:
        img = cv2.imread(input_img)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        print("Loaded. Processing..")
    except cv2.error as err:
        #print(err)
        print("Not an image")
        return(-1)

    
    
    if not bright_blobs:
        gray = cv2.bitwise_not(gray)
    if adaptive:
        print("Using adaptive thresholding")
        thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
               cv2.THRESH_BINARY,11,2)
    else:
        ret,thresh = cv2.threshold(gray,min_pixel,255,0)
    #
    if show_threshold:
        cv2.imshow('Thresholded input', thresh)
        cv2.waitKey(0)

    _, contours, _= cv2.findContours(thresh,cv2.RETR_EXTERNAL,2)

    LENGTH = len(contours)
    print("Found " + str(LENGTH) + " contours..")

    if min_area > 0:
        filtered = []
        area = []
        for hull in contours:
            a = cv2.contourArea(hull)
            area.append(a)

            if a >  min_area:

                filtered.append(hull)
        print("[min_area] Mean blob area: " + str(round(np.mean(area), 3)))
        print("[min_area: " + str(min_area) + "]: Filtered out " + str(len(contours) - len(filtered)) + " hulls - " + str(len(filtered)) + " remain")
        n_hulls = str(len(filtered))
        contours = filtered
        print(area)

    LENGTH = len(contours)
    status = np.zeros((LENGTH,1))

    toolbar_width = LENGTH
    print("Merging nearby contours.. (min_distance=" + str(min_distance) + ")")

    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i,cnt1 in enumerate(contours):
        x = i    
        if i != LENGTH-1:
            for j,cnt2 in enumerate(contours[i+1:]):
                x = x+1
                
                dist = find_if_close(cnt1,cnt2,min_distance)
                if dist == True:
                    val = min(status[i],status[x])
                    status[x] = status[i] = val
                else:
                    if status[x]==status[i]:
                        status[x] = i+1
            sys.stdout.write("=")
            sys.stdout.flush()

    sys.stdout.write("\n")
    unified = []
    try:
        maximum = int(status.max())+1
    except ValueError:
        print "WARN: No blobs found! Try reducing min_pixel"
        return 0

    for i in xrange(maximum):
        pos = np.where(status==i)[0]
        if pos.size != 0:
            cont = np.vstack(contours[i] for i in pos)
            hull = cv2.convexHull(cont)
            unified.append(hull)

    
    n_hulls = str(len(unified))
    print("Merged into " + n_hulls + " hulls ")
    
    info_str = n_hulls + " blobs found. min_pixel="+str(min_pixel) + ", min_distance="+str(min_distance) + "min_area="+str(min_area)
    im_with_contours = cv2.drawContours(img,unified,-1,highlight_col,2)
    cv2.putText(im_with_contours,info_str, (25,100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, highlight_col, 2)
    print("Writing annotated image to " + output)
    cv2.imwrite(output, im_with_contours)
    return len(unified)


def find_if_close(cnt1,cnt2, min_distance):
    row1,row2 = cnt1.shape[0],cnt2.shape[0]
    for i in xrange(row1):
        for j in xrange(row2):
            dist = np.linalg.norm(cnt1[i]-cnt2[j])
            if abs(dist) < min_distance :
                return True
            elif i==row1-1 and j==row2-1:
                return False

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utility to identify mRNA molecules in FISH images (using OpenCV)")
    parser.add_argument('-I', '--input', help="Input image")
    parser.add_argument('-O', '--output', help="Output image")
    parser.add_argument('-M', '--min_pixel', help="Minimum pixel value (higher means less signal, less noise)")
    parser.add_argument('-MD', '--min_distance', help="Minimum distance (higher means less merging)")
    parser.add_argument('-MA', '--min_area', help="Minimum area of blobs (higher less blobs)")
    parser.add_argument('--bright-blobs', dest='bright', action='store_true', help="Look for dark blobs (default is false, looks for bright blobs)")
    parser.add_argument('--dark-blobs', dest='bright', action='store_false')
    parser.set_defaults(bright=True)
    parser.add_argument('--adaptive', action='store_true', help="Use adaptive thresholding")
    parser.add_argument('--show_threshold', action='store_true', help="Show the thresholded image before processing it")

args = parser.parse_args()

if not args.input:
    parser.print_help(sys.stderr)
    sys.exit(1)


#thresholds
if not args.min_pixel:
    min_pixel = 25
else:
    min_pixel = float(args.min_pixel)

if args.min_area:
    min_area = float(args.min_area)
else:
    min_area = 0

if not args.min_distance:
    min_distance = 20
else:
    min_distance = float(args.min_distance)
if not args.output:
    output = "processed_output.jpg"
else:
    output = args.output

quant(args.input, 
    output,
    min_pixel,
    min_distance,
    min_area = min_area,
    bright_blobs=args.bright, 
    adaptive=args.adaptive, 
    show_threshold=args.show_threshold)
