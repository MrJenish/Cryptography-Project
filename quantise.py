import numpy as np

def quantize_data(data, operation_type, block_size_rows, block_size_cols):
    """
    Quantizes or dequantizes a matrix J based on the type t and the block size defined by Ia and Ib
    
    Parameters:
        data (ndarray): The matrix to quantize or dequantize
        operation_type (int): The type of operation to perform (1 for quantize, 2 for dequantize)
        block_size_rows (int): The block size along the rows
        block_size_cols (int): The block size along the columns
    
    Returns:
        data (ndarray): The quantized or dequantized matrix
    """
    quantization_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                                    [12, 12, 14, 19, 26, 58, 60, 55],
                                    [14, 13, 16, 24, 40, 57, 69, 56],
                                    [14, 17, 22, 29, 51, 87, 80, 62],
                                    [18, 22, 37, 56, 68, 109, 103, 77],
                                    [24, 35, 55, 64, 81, 104, 113, 92],
                                    [49, 64, 78, 87, 103, 121, 120, 101],
                                    [72, 92, 95, 98, 112, 100, 103, 99]])
    
    # Quantize
    if operation_type == 1:
        for i in range(0, block_size_rows, 8):
            for j in range(0, block_size_cols, 8):
                data[i:i+8, j:j+8] = data[i:i+8, j:j+8] / quantization_matrix
        data = np.round(data)
        
    # Dequantize
    else:
        for i in range(0, block_size_rows, 8):
            for j in range(0, block_size_cols, 8):
                data[i:i+8, j:j+8] = data[i:i+8, j:j+8] * quantization_matrix
    
    return data