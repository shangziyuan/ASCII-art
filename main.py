# Import libraries
from PIL import Image
import numpy as np

# Brightness to character map
brightness_map = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
map_len = len(brightness_map)

# Read image and print height and width
im = Image.open("cat.jpg")
im.thumbnail((500,500))
print("Successfully loaded image!")

im_arr = np.array(im, dtype='int64')

for x in range(len(im_arr)):
    for y in range(len(im_arr[x])):
        pixel = im_arr[x][y]

        # Get average brightness
        avg = (pixel[0] + pixel[1] + pixel[2]) / 3
        mapped_val = int((avg/255) * map_len)
        print(brightness_map[mapped_val], end="")
    print("")