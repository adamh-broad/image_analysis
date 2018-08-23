# Python script for mRNA quantification using smFISH images

This repo contains Python code for image analysis based on  <a href="https://opencv.org/">OpenCV</a>.




## Getting Started
### Installation
- Install OpenCV with Python bindings.
- For example, using Homebrew on Mac OS X:
```bash 
brew install opencv
```
- Clone this repo:
```bash
git clone https://github.com/NVIDIA/vid2vid
cd vid2vid
```

### Image analysis

- To run the analysis code:
  ```bash
  #!./scripts/test_2048.sh
  python detect_cells/contour.py --input input/Control_60X_1_C002.tif --bright-blobs  --min_pixel 35 --min_distance 2
  ```
  The test results will be saved to a HTML file here: `./results/label2city_2048/test_latest/index.html`.

- You can find more example scripts in the `test_input` directory.


Input image            |  Quantification by contour detection and merging
:-------------------------:|:-------------------------:
![](https://github.com/adamh-broad/image_analysis/blob/master/dclk1_il13.jpg)  |  ![](https://github.com/adamh-broad/image_analysis/blob/master/dclk1_il13_quant.jpg)

## Related Resources

* <a href="https://portals.broadinstitute.org/single_cell/study/small-intestinal-epithelium">Single Cell Portal (Broad Institute)</a>
* <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE106510">GEO Database link</a>

For questions or issues email:
ahaber -at- broadinstitute.org
