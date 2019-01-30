from skimage import io, color, util
import sys
import numpy

def gammaTransform(image, c, gamma):
    #height, width = image.shape

    #ret = numpy.zeros(image.shape, dtype=numpy.float)
    
    #for x in range(height):
    #    for y in range(width):
    #        ret[x,y] = c*image[x,y]**gamma

    #ret = numpy.clip(ret,0,255)

    return c*image**gamma


image = io.imread(sys.argv[1])

image = color.rgb2gray(image)

image = util.img_as_float(image)

c = numpy.float(sys.argv[2])
gamma = numpy.float(sys.argv[3])

gammaTransformed = gammaTransform(image,c,2000)


io.imshow(gammaTransformed)
io.show()
