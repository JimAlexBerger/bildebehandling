from scipy import ndimage
from skimage import io,util,color
from IPython import display
import numpy
import sys
import math

import matplotlib.pyplot as plt


def isOutside(x,y,width,height):
    if(x < 0 or y < 0):
        return True
    if(x >= width or y >= height):
        return True
    return False

def convolve(filtr, image, mode, value = 0):
    
    filtr = numpy.rot90(filtr, k=2)
    
    width, height = image.shape
    Fwidth, Fheight = filtr.shape
    
    Mx = math.ceil(Fwidth/2)
    My = math.ceil(Fheight/2)
    
    ret = numpy.zeros(image.shape, dtype=numpy.ubyte)

    for x in range(width):
        for y in range(height):
            s = 0
            
            for x2 in range(Fwidth):
                for y2 in range(Fheight):
                    imX = x - (x2 + 1 - Mx)
                    imY = y - (y2 + 1 - My)
                    
                    if(isOutside(imX, imY, width, height)):
                        outValue = 0
                        
                        if(mode == 'constant'):
                            outValue = value
                        elif(mode == 'wrap'):
                            outValue = image[imX % width, imY % height]
                        else:
                            outValue = 0
                        
                        s += outValue * filtr[x2,y2]
                    else:
                        s += image[imX, imY] * filtr[x2,y2]
            
            ret[x,y] = s
    
    return ret

def update(image):
    im = util.img_as_ubyte(color.rgb2gray(io.imread(image)))
    filtr = numpy.ones((5,5)) / (5*5)
    #filtr = numpy.array([[1,2,3],[4,5,6],[7,8,9]]) / 45
    
    builtin = ndimage.convolve(im, filtr, mode='wrap', cval=0.0)
    
    image = convolve(filtr, im, 'wrap', 0.0)
    
    io.imshow_collection([image,builtin], cmap='gray')
    io.show()
    

update('Bilder/image_resources/lenna-gray.tif')
print('Hello World')