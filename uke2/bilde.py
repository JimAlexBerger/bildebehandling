from skimage import io
from math import ceil

image = io.imread('bilde2.jpg')

numrows,numcols,z = image.shape

slicecols = ceil(numcols/3)
slicerows = ceil(numrows/3)

#subim = image[slicecols:slicecols*2,slicerows:slicerows*2]
subim = image[::20,::20]

io.imshow_collection([image,subim])
io.show()
