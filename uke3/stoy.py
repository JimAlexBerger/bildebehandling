import skimage
import numpy
from skimage import io,util

image = io.imread("../Bilder/image_resources/checkerboard1024.tif")

def noise(image, num = 10, var = 0.01):
    noised_images = []

    for x in range(num):
        noised_images.append(skimage.util.random_noise(image, mode='gaussian', seed=None, clip=True, var=var))
    
    return sum(noised_images)/num


denoised = noise(image, 100, 0.5)

#denoised = skimage.exposure.rescale_intensity(denoised)

print(denoised)

#print(image)

io.imshow(denoised)
io.show()
