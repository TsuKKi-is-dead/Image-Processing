# Image-Processing

🛰️ Satellite Image Processing & Computer Vision
NIT Rourkela Internship Project

A structured learning journey through image processing and computer vision techniques applied to satellite and remote sensing imagery.

📌 Project Overview
This repository documents my internship project at National Institute of Technology Rourkela (NIT RKL), focused on learning and applying image processing and computer vision techniques specifically for satellite and remote sensing imagery. The project covers everything from fundamental image operations to advanced deep learning-based analysis of geospatial data.

🗂️ Table of Contents

Environment Setup
Module 1 — Image Fundamentals
Module 2 — Preprocessing Techniques
Module 3 — Feature Extraction
Module 4 — Image Segmentation
Module 5 — Spectral Analysis
Module 6 — Object Detection & Classification
Module 7 — Change Detection
Module 8 — Deep Learning for Remote Sensing
Datasets
Tools & Libraries
References

⚙️ Environment Setup
bash# Clone the repository
git clone https://github.com/your-username/Image-Processing.git
cd Image-Processing

# Create and activate virtual environment

python3 -m venv .venv
source .venv/bin/activate # macOS/Linux
.venv\Scripts\activate # Windows

# Install dependencies

pip install -r requirements.txt
Core dependencies:
opencv-python
numpy
matplotlib
rasterio
gdal
scikit-image
scikit-learn
torch
torchvision
earthpy
geopandas

Module 1 — Image Fundamentals

Understanding how satellite images differ from standard RGB images.

Topics Covered:

Digital image representation (raster data, pixels, bands)
Grayscale vs. RGB vs. multispectral vs. hyperspectral images
Image coordinate systems and spatial resolution
Reading and writing images with OpenCV and Rasterio
Bit depth and radiometric resolution
Visualizing multi-band satellite images (RGB composites)

Key Concepts:

cv2.imread(), cv2.imshow(), cv2.imwrite()
Band stacking and false-color composites
DN (Digital Number) values vs. reflectance values

Module 2 — Preprocessing Techniques

Cleaning and preparing raw satellite data for analysis.

Topics Covered:

Radiometric correction (converting DN to radiance/reflectance)
Atmospheric correction (DOS, FLAASH methods)
Geometric correction and image orthorectification
Image resampling and reprojection
Histogram equalization and contrast stretching
Noise reduction:

Gaussian blur
Median filter
Bilateral filter

Pan-sharpening (combining panchromatic + multispectral)

Key Concepts:

cv2.equalizeHist(), cv2.GaussianBlur(), cv2.medianBlur()
CLAHE (Contrast Limited Adaptive Histogram Equalization)
Image normalization techniques

Module 3 — Feature Extraction

Identifying meaningful patterns and structures in satellite imagery.

Topics Covered:

Edge detection:

Sobel, Prewitt, Laplacian operators
Canny edge detector

Corner detection: Harris, Shi-Tomasi
Texture analysis: GLCM (Gray-Level Co-occurrence Matrix)
Morphological operations (erosion, dilation, opening, closing)
Blob detection and contour analysis
Keypoint descriptors: SIFT, ORB, BRIEF
Line detection: Hough Transform (roads, runways)

Key Concepts:

cv2.Canny(), cv2.findContours(), cv2.HoughLinesP()
Feature matching for image stitching
Scale-space theory

Module 4 — Image Segmentation

Partitioning satellite images into meaningful regions (land, water, urban, vegetation).

Topics Covered:

Thresholding:

Global (Otsu's method)
Adaptive thresholding

Region-based segmentation:

Region growing
Watershed algorithm

Clustering-based segmentation:

K-Means clustering
Mean-Shift

Graph-cut segmentation
Superpixel segmentation (SLIC)
Semantic segmentation using pre-trained models

Key Concepts:

cv2.threshold(), cv2.watershed()
sklearn.cluster.KMeans for pixel clustering
NDWI masking for water body extraction

Module 5 — Spectral Analysis

Leveraging the unique multi-band nature of satellite imagery.

Topics Covered:

Spectral indices:

NDVI — Normalized Difference Vegetation Index
NDWI — Normalized Difference Water Index
NDBI — Normalized Difference Built-up Index
EVI — Enhanced Vegetation Index
SAVI — Soil Adjusted Vegetation Index

Band math and raster algebra
Principal Component Analysis (PCA) on spectral bands
Spectral signature analysis
Minimum Noise Fraction (MNF) transform
False color composites for feature emphasis

Key Formulas:
NDVI = (NIR - Red) / (NIR + Red)
NDWI = (Green - NIR) / (Green + NIR)
NDBI = (SWIR - NIR) / (SWIR + NIR)

Module 6 — Object Detection & Classification

Identifying and labeling objects (buildings, roads, ships, aircraft) in satellite images.

Topics Covered:

Classical ML classification:

SVM (Support Vector Machine)
Random Forest
Maximum Likelihood Classification

Object-Based Image Analysis (OBIA)
Sliding window detection
Deep learning-based object detection:

YOLO (You Only Look Once) for aerial imagery
Faster R-CNN
RetinaNet

Accuracy assessment: confusion matrix, kappa coefficient, F1 score

Key Concepts:

Training data collection and labeling
Handling class imbalance in remote sensing datasets
Intersection over Union (IoU) metric

Module 7 — Change Detection

Comparing multi-temporal satellite images to identify changes on the ground.

Topics Covered:

Image differencing and ratioing
Change Vector Analysis (CVA)
Post-classification comparison
Normalized Difference Change Index
Deep learning-based change detection:

Siamese networks
U-Net based change detection

Applications:

Urban sprawl monitoring
Deforestation detection
Flood mapping
Disaster damage assessment

Key Concepts:

Co-registration of multi-temporal images
Binary change maps vs. categorical change maps
Threshold selection for change maps

Module 8 — Deep Learning for Remote Sensing

Applying modern neural networks to satellite image analysis tasks.

Topics Covered:

CNN fundamentals and transfer learning
Semantic segmentation architectures:

U-Net (most widely used for satellite imagery)
DeepLab v3+
SegNet

Land use / Land cover (LULC) classification
Instance segmentation with Mask R-CNN
Working with geospatial data in PyTorch
Data augmentation for satellite images (flips, rotations, spectral jitter)
Model evaluation on geospatial datasets

Key Concepts:

Patch-based training for large satellite images
Handling GeoTIFF files in deep learning pipelines
Geospatial data loaders with rasterio + torch

📦 Datasets
DatasetDescriptionSourceSentinel-213-band multispectral, 10m resolutionESA CopernicusLandsat 8/911-band multispectral, 30m resolutionUSGS Earth ExplorerISRO ResourcesatIndian remote sensing dataBhuvan (ISRO)DOTAObject detection in aerial imagesDOTA DatasetDeepGlobeLand cover, road, building segmentationDeepGlobe ChallengeSpaceNetBuilding footprint & road detectionAWS Open Data

🛠️ Tools & Libraries
ToolPurposeOpenCV (cv2)Core image processing operationsRasterioReading/writing geospatial raster dataGDALGeospatial data abstractionNumPyArray and matrix operationsMatplotlibVisualizationscikit-imageAdvanced image processing algorithmsscikit-learnClassical ML classificationPyTorchDeep learning model trainingEarthPyRemote sensing specific utilitiesGeoPandasVector geospatial dataQGISGeospatial visualization & analysis (GUI)

📚 References

Gonzalez & Woods — Digital Image Processing (4th Ed.)
Lillesand, Kiefer & Chipman — Remote Sensing and Image Interpretation
ESA Sentinel Online
USGS Earth Explorer
ISRO Bhuvan Portal
OpenCV Documentation
Rasterio Documentation

🏫 Internship Details
FieldDetailsInstitutionNational Institute of Technology Rourkela (NIT RKL)DomainSatellite Image Processing & Computer VisionTech StackPython, OpenCV, PyTorch, Rasterio, GDALDuration(add your internship duration)Guide(add your faculty/mentor name)

This README will be updated progressively as each module is completed during the internship.
