from scipy import ndimage
from skimage import io,util,color
from IPython import display
import numpy
import sys
import math

import matplotlib.pyplot as plt


def histogram(im):
    ret = numpy.zeros(256, dtype=numpy.uint)

    height, width = im.shape

    for x in range(height):
        for y in range (width):
            ret[im[x][y]] += 1
    
    return ret

def printHistogramBilde(image):
    hist = histogram(image)
    ind = numpy.arange(len(hist))  

    ax = plt.subplots()[1]
    ax.bar(ind, hist)

    plt.show()

def readAndShowImageWHistogram(image):
    im = util.img_as_ubyte(color.rgb2gray(io.imread(image)))
    
    printHistogramBilde(im)
    
    io.imshow(im)
    io.show()


def cumulativeDistribution(hist):
    ret = numpy.zeros(256)
    ret[0] = hist[0]
    
    for x in range(1,256):
        ret[x] = ret[x-1] + hist[x]
    
    return ret

def cumulativeDistributionImage(im):
    hist = histogram(im)
    
    width, height = im.shape
    
    hist2 = numpy.zeros(256)
    
    for x in range(256):
        hist2[x] = hist[x] / (width*height)
    
    return cumulativeDistribution(hist2)

def plotCD(image):
    im = util.img_as_ubyte(color.rgb2gray(io.imread(image)))
    
    CD = cumulativeDistributionImage(im)
    
    ind = numpy.arange(len(CD))  # the x locations for the groups

    ax = plt.subplots()[1]
    ax.bar(ind, CD)

    plt.show()

def histogramEqualization(im):
    width, height = im.shape
    
    CD = cumulativeDistributionImage(im)
        
    for x in range(width):
        for y in range(height):
            im[x,y] = numpy.floor(CD[im[x,y]] * 255)
            
    return im

def histogramEq(image):
    im = util.img_as_ubyte(color.rgb2gray(io.imread(image)))
    
    im = histogramEqualization(im)
    
    printHistogramBilde(im)

    io.imshow(im, cmap='gray')
    io.show()

def inverseCumulative(cumulative):
    ret = numpy.zeros(256)
    
    cumulative = numpy.floor(cumulative*255)
    
    for x in range(256):
        ret[int(cumulative[x])] = x
    
    for x in range(1,256):
        if(ret[x] == 0):
            ret[x] = ret[x-1]
    
    return ret

def histogramMatch(image, specification):
    im = util.img_as_ubyte(color.rgb2gray(io.imread(image)))
    
    if(specification == 'Linear Increase'):
        specification = numpy.arange(256)
    elif(specification == 'Linear Decrease'):
        specification = numpy.flip(numpy.arange(256))
    elif(specification == 'Exponential Growth'):
        specification = numpy.zeros(256)
        for x in range(256):
            specification[x] = x**2
    elif(specification == 'Exponential Decay'):
        specification = numpy.zeros(256)
        for x in range(256):
            specification[x] = 256/(0.5*(x+1))
    elif(specification == 'Logarithmic'):
        specification = numpy.zeros(256)
        for x in range(256):
            specification[x] = math.log(x+1)
    elif(specification == 'spec.txt'):
        specification = numpy.loadtxt('spec.txt')
        
    specification = specification / sum(specification)
        
    ind = numpy.arange(len(specification))  

    ax = plt.subplots()[1]
    ax.bar(ind, specification)

    plt.show()
    
    specification = inverseCumulative(cumulativeDistribution(specification))
    
    width, height = im.shape
    
    #Normalize before matching
    im = histogramEqualization(im)
    
    for x in range(width):
        for y in range(height):
            im[x,y] = specification[im[x,y]]
    
    printHistogramBilde(im)
    io.imshow(im, cmap='gray')
    io.show()

inputImage2 = {
    'Lena':'Bilder/image_resources/lenna-gray.tif',
    'Pollen Mørkt':'Bilder/image_resources/magnified-pollen-dark.tif',
    'Trump':'Bilder/trump1.jpg',
    'Pollen Lav Kontrast':'Bilder/image_resources/pollen-lowcontrast.tif',
    'Einstein Lav Kontrast':'Bilder/image_resources/einstein-low-contrast.tif'}


readAndShowImageWHistogram(inputImage2['Pollen Lav Kontrast'])
histogramEq(inputImage2['Pollen Lav Kontrast'])
histogramMatch(inputImage2['Pollen Lav Kontrast'],'Linear Increase')