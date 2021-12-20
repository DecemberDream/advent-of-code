import numpy as np


def enhance(img, num_of_steps=2, fill_value=0, pad_size=2):
    for steps in range(num_of_steps):
        img = np.pad(img, pad_size, constant_values=fill_value)
        rows, cols = img.shape
        
        stride_rows = rows - pad_size
        stride_cols = cols - pad_size
        stride_shape = stride_rows, stride_cols, 3, 3
        stride = np.lib.stride_tricks.as_strided(img, stride_shape, 2 * img.strides)
        stride = np.reshape(stride, (stride_rows, stride_cols, 9))
        
        codes = stride[:, :, 0] * 256 + np.packbits(stride[:, :, 1:]).reshape(stride_rows, stride_cols)
        
        img = algorithm[codes]
        
        fill_value = algorithm[fill_value * 511]
        
    return img


algorithm, img = open("../../input/day_20_data.txt").read().replace(".", "0").replace("#", "1").split("\n\n")
algorithm = np.array([int(x) for x in algorithm], dtype=np.uint8)
img_temp = []
img = img.split("\n")

for row in img:
    img_temp.append([int(x) for x in row])

img_in = np.array(img_temp, dtype=np.uint8)

print(np.sum(enhance(img_in)))