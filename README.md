# Computer-Vision-Project
This is a collaborative final project for the BSCS 4388 - Computer Vision course. Out of the nine project topics to choose from, our group chose the Document Analysis and Recognition topic, and implemented two sub-ideas: 
- Handwritten digit recognition for automated data entry
- Extracting text using Optical Character Recognition (OCR)


## Handwritten Digit Recognition
Model: Implemented an 8-layer CNN Model to recognize handwritten digits.

### Installation
We used OpenCV, Matplotlib, TensorFlow, and Keras libraries. These modules can be installed using ```pip```.

```python -m pip install matplotlib opencv-python tensorflow```

## Datasets used
- Yann LeCun, Corinna Cortes and Chris Burges.  (n.d). The MNIST database of handwritten digits [Data set] (n.d.). http://yann.lecun.com/exdb/mnist/ 
- https://www.tensorflow.org/datasets/catalog/mnist

## Extracting text using OCR
### Installation
We used OpenCV, PyTesseract, and EasyOCR. These modules can be installed using ```pip```. The PyTesseract module has a few installation prerequisites, and instructions can be found [here.](https://github.com/madmaze/pytesseract) If you are on Windows, EasyOCR requires you to install torch and torchvision with the official instructions here https://pytorch.org.

```python -m pip install opencv-python pytesseract easyocr```



## Datasets used
- G. Jaume, H. K. Ekenel, J. Thiran. (2019). FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents [Data set]. https://guillaumejaume.github.io/FUNSD/
- David Doermann. (2019, Sept. 13). Tobacco 800 Dataset (Tobacco800) ,1,ID:Tobacco800_1, [Data Set]. https://www.kaggle.com/datasets/sprytte/tobacco-800-dataset http://tc11.cvc.uab.es/datasets/Tobacco800_1
- Lucas, S. (2011). ICDAR 2003 Robust Reading Competitions - TC11 (v1.0) [Dataset]. http://iapr-tc11.org/mediawiki/index.php?title=ICDAR_2003_Robust_Reading_Competitions 

Included the following reference(s) when citing the Tobacco800 database:
- D. Lewis, G. Agam, S. Argamon, O. Frieder, D. Grossman, and J. Heard, “Building a test collection for complex document information processing,” in Proc. 29th Annual Int. ACM SIGIR Conference (SIGIR 2006), pp. 665–666, 2006.
- G. Agam, S. Argamon, O. Frieder, D. Grossman, and D. Lewis, The Complex Document Image Processing (CDIP) test collection project, Illinois Institute of Technology, 2006. http://ir.iit.edu/projects/CDIP.html.
- The Legacy Tobacco Document Library (LTDL), University of California, San Francisco, 2007.http://legacy.library.ucsf.edu/.
