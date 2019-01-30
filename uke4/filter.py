from scipy import ndimage
from skimage import io
import numpy
import sys
import math

def gaussian(a,b, sigma = 1):
    
    m = 2*a + 1
    n = 2*b + 1

    ret = numpy.zeros((m,n))
    
    for x in range(m):
        for y in range(n):
            dx = abs(a - x)
            dy = abs(b - y)
            ret[x][y] = (1/(2*math.pi*sigma**2))*math.e**(-(dx**2+dy**2)/(2*sigma**2))

    return ret

def avg(a,b):
    m = 2*a + 1
    n = 2*b + 1
    ret = numpy.ones((m,n))
    ret = ret / (m*n)
    return ret

def weight(a,b):
    m = 2*a + 1
    n = 2*b + 1

    ret = numpy.zeros((m,n))

    s = 0
    
    for x in range(m):
        for y in range(n):
            dx = abs(a - x)
            dy = abs(b - y)
            num = 1/((dx + dy + 1)**2)
            s += num
            ret[x][y] = num 

    return ret / s

    
image = io.imread(sys.argv[1], as_gray=True)

#k = numpy.array([[1,1,1],[1,1,1],[1,1,1]])
#k2 = numpy.array([[1,2,1],[2,4,2],[1,2,1]])

sharpen =  numpy.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
edge =  numpy.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

#k = k/9
#k2 = k2/16

#k = avg(2,2)
#k2 = weight(2,2)

#utjevning = ndimage.convolve(image,k,mode='constant',cval=0)
#weighted = ndimage.convolve(image,k2,mode='constant',cval=0)
#gaus = ndimage.convolve(image,gaussian(2,2,7), mode='constant', cval=0)
#sharp = ndimage.convolve(image,sharpen,mode='constant',cval=0)
edges = ndimage.convolve(image,edge,mode='constant',cval=0)

io.imshow_collection([image,edges], cmap='gray')
io.show()
