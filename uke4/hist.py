import skimage
import numpy
import sys
from skimage import io,util,color

def histogram(image, bins):
    histogram = numpy.zeros((bins,1), dtype=numpy.int)

    height, width = image.shape

    for x in range(height):
        for y in range (width):
            histogram[int(round(image[x][y]*(bins-1)))] += 1
    
    return histogram

image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

bins = numpy.int(sys.argv[2])


print(histogram(image,bins))
