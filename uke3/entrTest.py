# imports needed for skimage and pyplot
from skimage import io

# Read the image called "lena.png" from file
im = io.imread("../Bilder/bilde.jpg")

for x in range(len(im)):
        for y in range(len(im[x])):
            avg = (im[x][y][0] + im[x][y][1] + im[x][y][2])/3
            im[x][y][0] = avg
            im[x][y][1] = avg
            im[x][y][2] = avg


        

# show image
io.imshow(im)
io.show()
