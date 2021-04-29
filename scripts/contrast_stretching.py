
import cv2
import numpy as np
import matplotlib.pyplot as plt


img =  cv2.imread('D:/Anaconda/Image_analysis/water.png')

# The values of xp and fp can be varied to create custom tables as required 
# and it will stretch the contrast even if min and max pixels are 0 and 255 

xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]

x = np.arange(256)
table = np.interp(x, xp, fp).astype('uint8')

# cv2.LUT will replace the values of the original image with the values in the
# table. For example, all the pixels having values 1 will be replaced by 0 and 
# all pixels having values 4 will be replaced by 1.
img = cv2.LUT(img, table)

plt.imshow(img)
plt.title('Contrast Stretched Image')


def contrast_stretching(z, a, b, z1, zk):

    new_array = np.copy(z)
        
    for i,value in enumerate(z):
        if value>=a and value<=b:
            new_pixel_value = (((zk - z1)/(b-a))*value) + ((z1*b - zk*a)/(b-a))

            new_array[i] = new_pixel_value

    return new_array
