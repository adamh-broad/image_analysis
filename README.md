# Python script for blob detection-based image analysis

This repo contains Python code for image analysis based on  <a href="https://opencv.org/">OpenCV</a>. The program detects local, contiguous regions (blobs) of high signal intensity. Depending on the image modality, these can correspond to cells in immunohistochemistry (IHC) stains, or to individual messenger RNA (mRNA) molecules in single-molecule FISH (smFISH) images. This code was used to quantify images in the study <a href="https://www.biorxiv.org/content/early/2017/11/14/217133">Biton et al., 2017</a>.  


## Getting Started
### Installation (only tested on OS X, but should work on linux)
- Install OpenCV with Python bindings. There are several blogs with instructions to do so such as <a href="https://www.learnopencv.com/install-opencv3-on-macos/"> this one</a>/
- For example, using Homebrew on Mac OS X:
```bash 
brew install opencv3
```
- Clone this repo:
```bash
git clone https://github.com/adamh-broad/image_analysis.git
cd smFISH_blob
pip install --user .

```

### Image analysis

- To run the analysis code for a single image:
  ```bash
  python detect_cells/contour.py --input input/Control_60X_1_C002.tif --bright-blobs  --min_pixel 35 --min_distance 2
  ```
  The output results will be saved a jpg image: `image_quant.jpg` so the blobs detected and their total number can be visually inspected.

- To run the code in a batched manner on all images in a directory (e.g, the `test_input` directory).
  ```bash
  python runQuant.py
  ```
- There are several parameters to control dot resolution. The first is 'min_pixel', which thresholds the image with all pixels less than min_pixel in brightness being made black. The second is 'min_distance' which controls how much merging is done for nearby dots; higher 'min_distance' give more merging.


Input image            |  Quantification by contour detection and merging
:-------------------------:|:-------------------------:
![](https://github.com/adamh-broad/image_analysis/blob/master/dclk1_il13.jpg)  |  ![](https://github.com/adamh-broad/image_analysis/blob/master/dclk1_il13_quant.jpg)

## Related Resources

* <a href="https://portals.broadinstitute.org/single_cell/study/small-intestinal-epithelium">Single Cell Portal (Broad Institute)</a>
* <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE106510">GEO Database link</a>

For questions or issues email:
ahaber -at- broadinstitute.org
