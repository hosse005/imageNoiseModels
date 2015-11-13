#!/usr/bin/python

import sys
import random
import numpy as np
from PIL import Image


# Global parameters
width = height = 256
radius = 50
a = width / 4
b = 3 * width / 4
p_a = 0.05
p_b = 0.05


# Entry point
def main():
    print('Executing noiseModels..')

    # Create the base circle
    circleData = createCircle()
    img = Image.fromarray(np.uint8(circleData))
    filename = 'circle.png'
    img.save(filename)
    print('Wrote base circle image to %s' % filename)

    # Add uniform noise to the circle image
    uniformCorruption = circleData + genUniformNoise() 
    normGrayscale(uniformCorruption)
    img = Image.fromarray(np.uint8(uniformCorruption))
    filename = 'uniformCorruption.png'
    img.save(filename)
    print('Wrote uniformly corrupted image to file %s' % filename)

    # Add salt and pepper noise to the image
    sltPepCorruption = circleData + genSaltPepperNoise()
    normGrayscale(sltPepCorruption)
    img = Image.fromarray(np.uint8(sltPepCorruption))
    filename = 'saltPepperCorruption.png'
    img.save(filename)
    print('Wrote salt and pepper corrupted image to file %s' % filename)    
                          


# Create a base circle of width x height and radius
def createCircle():
    data = np.zeros((width, height), dtype=np.uint8)

    # Iterate through the image, and create a centered circle
    for (x,y), _ in np.ndenumerate(data):
        if np.square(x - width/2) + np.square(y - height/2) <= np.square(radius):
            data[x,y] = 100

    return data


# Generate uniform noise
def genUniformNoise():
    data = np.zeros((width, height))

    for (x,y), _ in np.ndenumerate(data):
        data[x,y] = a + (b - a) * random.random()

    return data


# Generate salt and pepper noise
def genSaltPepperNoise():
    data = np.zeros((width, height))

    for (x,y), _ in np.ndenumerate(data):
        rdm_n = random.random()
        if rdm_n <= p_a:
            data[x,y] = a
        elif rdm_n >= 1 - p_b:
            data[x,y] = b

    return data

        
# Image normalization to 0-255
def normGrayscale(data):
    ''' @param data : numpy array '''
    min = data.min()
    max = data.max()

    for (x,y), value in np.ndenumerate(data):
        data[x,y] = (value - min) * 255 / (max - min)


if __name__ == '__main__':
    main()
