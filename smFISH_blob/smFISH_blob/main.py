import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utility to identify mRNA molecules in FISH images (using OpenCV)")
    parser.add_argument('-I', '--input', help="Input image")
    parser.add_argument('-O', '--output', help="Output image")
    parser.add_argument('-M', '--min_pixel', help="Minimum pixel value (higher means less signal, less noise)")
    parser.add_argument('-MD', '--min_distance', help="Minimum distance (higher means less merging)")
    parser.add_argument('--bright-blobs', dest='bright', action='store_true', help="Look for dark blobs (default is false, looks for bright blobs)")
    parser.add_argument('--dark-blobs', dest='bright', action='store_false')
    parser.set_defaults(bright=True)
    parser.add_argument('--adaptive', action='store_true', help="Use adaptive thresholding")
    parser.add_argument('--show_threshold', action='store_true', help="Show the thresholded image before processing it")

args = parser.parse_args()

#thresholds
if not args.min_pixel:
    min_pixel = 25
else:
    min_pixel = float(args.min_pixel)

if not args.min_distance:
    min_distance = 20
else:
    min_distance = float(args.min_distance)
if not args.output:
    output = "contours.jpg"
else:
    output = args.output

quant(args.input, 
    output,
    min_pixel,
    min_distance,
    bright_blobs=args.bright, 
    adaptive=args.adaptive, 
    show_threshold=args.show_threshold)
