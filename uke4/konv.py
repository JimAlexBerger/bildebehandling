import numpy
from scipy import ndimage

m = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
w = numpy.array([[0,1,0],[1,1,1],[0,1,0]])

conv = ndimage.convolve(m,w,mode='constant', cval=0)
corr = ndimage.correlate(m,w,mode='constant', cval=0)

print(conv)
print(corr)
print(numpy.array_equal(conv, corr))