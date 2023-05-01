import cv2
import numpy as np
from dct import discrete_cosine
from quantize import quantize_data
from zigzag import zigzag_traversal
from huffman import huffman_encode, huffman_decode

# Read initial image
input_image = cv2.imread('passport_jaishree.jpg')

# Backup of image
backup_image = input_image.copy()

# Convert to grayscale and double precision
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
input_image = np.float64(input_image)

# Determine image size
height, width = input_image.shape

if height % 8 == 0:
    height_a = height - 8
else:
    height_a = height - (8 + height % 8)

if width % 8 == 0:
    width_b = width - 8
else:
    width_b = width - (8 + width % 8)

# Perform DCT
dct_coefficients = discrete_cosine(input_image, 1, height_a, width_b)

# Perform quantization
quantized_data = quantize_data(dct_coefficients, 1, height_a, width_b)

# Perform zig-zag traversal
zigzag_data = zigzag_traversal(quantized_data, 1, height_a, width_b)

# Initialize arrays for encoding/decoding
encoded_data = []
decoded_data = []

# Print loop iteration count
print('This loop will run until the iteration value reaches:')
print(height_a * width_b // 64)

# Loop over zig-zag blocks
for i in range(height_a * width_b // 64):
    a = len(encoded_data)
    encoded_data = huffman_encode(zigzag_data[i, :], encoded_data)
    decoded_data = huffman_decode(encoded_data, decoded_data, a + 1, i + 1)
    print(i + 1)

# Perform inverse zig-zag traversal
inverse_zigzag_data = zigzag_traversal(decoded_data, 2, height_a, width_b)

# Perform dequantization
dequantized_data = quantize_data(inverse_zigzag_data, 2, height_a, width_b)

# Perform inverse DCT
output_image = discrete_cosine(dequantized_data, 2, height_a, width_b)

# Convert to unsigned 8-bit integer
output_image = np.uint8(output_image)
input_image = np.uint8(input_image)

# Display final image
cv2.imshow("Final Image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()