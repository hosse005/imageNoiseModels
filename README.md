# imageNoiseModels
CS712 Project 3
Evan Hosseini

#Description:
This package contains my submission for project 3.

#Contents:
README.md - this file
noiseModels.py - Source python file for this project
circle.png - Generated circle image
Circle Histogram.png - Histogram of circle image
uniformCorruption.png - Circle image corrupted by uniform noise between 
    64 and 192
Uniform Corruption Histogram.png - Corresponding histogram of circle image 
    corrupted by uniform noise
saltPepperCorruption.png - Circle image corrupted by salt and pepper noise of 
    values 192 and 64 respectively, both occuring with probability of 0.05
Salt and Pepper Corruption Histogram.png - Corresponding histogram of circle
    image corrupted by salt and pepper noise

#Dependencies:
* Python3
  * Numpy
  * Matplotlib
  * Pillow

#Usage:
Simply execute the noiseModels.py from a python environment.  All of the files
included in this package will be generated in the directory that the script
was executed from.

Note: Since the histograms are calculated after the additive noise is applied,
the gray scale normalization will shift the bins slightly towards the y-axis 
from where you might expect them to be. 