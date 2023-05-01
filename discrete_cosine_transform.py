import numpy as np
from imageio import imread
from skimage.color import rgb2gray

# Load image
I = imread('C:/Users/deep/Pictures/Robomanipal.jpg')

# Convert to grayscale
I = rgb2gray(I)

# Convert to double precision
I = np.double(I)

# Initialize J and C
J = np.zeros((375, 384))
Cx = I

# Compute DCT
for k in range(0, 368, 8):
    for l in range(0, 384, 8):
        zx = 1
        for i in range(k, k + 8):
            cx = 1
            for j in range(l, l + 8):
                vx = 1
                for x in range(k, k + 8):
                    bx = 1
                    for y in range(l, l + 8):
                        J[i, j] += I[x, y] * np.cos((2 * (bx - 1) + 1) * (cx - 1) * np.pi / 16) * np.cos(
                            (2 * (v - 1) + 1) * (zx - 1) * np.pi / 16)
                        bx += 1
                    vx += 1
                if (zx - 1) == 0:
                    Ci = 1 / np.sqrt(2)
                else:
                    Ci = 1
                if (cx - 1) == 0:
                    Cj = 1 / np.sqrt(2)
                else:
                    Cj = 1
                J[i, j] = J[i, j] * Ci * Cj / 4
                cx += 1
                zx += 1
        J[k:k+8, l:l+8] = J[k:k+8, l:l+8]

# Store J in CC
CC = J

# Define quantization matrix
Q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
              [12, 12, 14, 19, 26, 58, 60, 55],
              [14, 13, 16, 24, 40, 57, 69, 56],
              [14, 17, 22, 29, 51, 87, 80, 62],
              [18, 22, 37, 56, 68, 109, 103, 77],
              [24, 35, 55, 64, 81, 104, 113, 92],
              [49, 64, 78, 87, 103, 121, 120, 101],
              [72, 92, 95, 98, 112, 100, 103, 99]])

# Perform quantization
for i in range(0, 368, 8):
    for j in range(0, 384, 8):
        J[i:i+8, j:j+8] = J[i:i+8, j:j+8] / Q

# Round off J
J = np.round(J)

# Count the number of zeros in J
count = 0
for i in range(368):
    for j in range(384):
        if J[i, j] == 0:
            count += 1

# Restore J from quantized values
for i in range(0, 368, 8):
    for j in range(0, 384, 8):
        J[i:i+8, j:j+8] = J[i:i+8, j:j+8] * Q

# Initialize I2
I2 = np.zeros((375, 384))

# Compute inverse DCT
for k in range(0, 368, 8):
    for l in range(0, 384, 8):
        zx = 1
        for i in range(k, k + 8):
            cx = 1
            for j in range(l, l + 8):
                vx = 1
                for x in range(k, k + 8):
                    bx = 1
                    for y in range(l, l + 8):
                        if (vx - 1) == 0:
                            Ci = 1 / np.sqrt(2)
                        else:
                            Ci = 1
                        if (bx - 1) == 0:
                            Cj = 1 / np.sqrt(2)
                        else:
                            Cj = 1
                        I2[i, j] += J[x, y] * Ci * Cj * np.cos((2 * (cx - 1) + 1) * (
                            bx - 1) * np.pi / 16) * np.cos((2 * (zx - 1) + 1) * (vx - 1) * np.pi / 16)
                        bx += 1
                    vx += 1
                I2[i, j] = I2[i, j] / 4
                cx += 1
                zx += 1

# Convert I and I2 to uint8 format
I = np.uint8(I)
I2 = np.uint8(I2)
