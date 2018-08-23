# A revised airway epithelial hierarchy includes CFTR-expressing ionocytes

# Python script for mRNA quantification using smFISH images
This repo contains Python code for image analysis based on  <a href="https://opencv.org/">OpenCV</a>.

Instructions to install OpenCV with Python bindings can be found here.

```{r }
## try http:// if https:// URLs are not supported
source("https://bioconductor.org/biocLite.R")
biocLite("sva")
``` 

## Abstract
We combine single-cell RNA-seq and in vivo lineage tracing to study the cellular composition and hierarchy of the murine tracheal epithelium. We identify a new rare cell type, the pulmonary ionocyte; functional variations in club cells based on their proximodistal location; a distinct cell type that resides in high turnover squamous epithelial structures that we named “hillocks”; and disease-relevant subsets of tuft and goblet cells. With a new method, Pulse-Seq, we show that tuft, neuroendocrine, and ionocyte cells are continually and directly replenished by basal progenitor cells. Remarkably, the cystic fibrosis gene, CFTR, is predominantly expressed in both mouse and human pulmonary ionocytes. Genetic perturbation of murine ionocytes causes a loss of Cftr expression and disrupts airway fluid and mucus physiology, which are also altered in cystic fibrosis. By associating cell type-specific expression programs with key disease genes, we establish a new cellular narrative for airways disease. 

Experimental workflow            |  GFP(Foxi1)+ ionocytes
:-------------------------:|:-------------------------:
![](https://github.com/adamh-broad/single_cell_airway/blob/master/fig1a.jpg)  |  ![](https://github.com/adamh-broad/single_cell_airway/blob/master/fox1_gfp.jpg)

## Related Resources

* <a href="https://portals.broadinstitute.org/single_cell/study/airway-epithelium">Single Cell Portal (Broad Institute)</a>
* <a href="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103354">GEO Database link</a>

For questions or issues email:
ahaber -at- broadinstitute.org
