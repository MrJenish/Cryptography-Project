import numpy as np

def zigzag_conversion(matrix, direction, num_rows, num_cols):
    """
    Converts a matrix of 8x8 blocks to/from a 1D array in zigzag order
    
    Parameters:
        matrix (numpy.ndarray): The input matrix of 8x8 blocks
        direction (int): The direction of the conversion (1 for forward, -1 for inverse)
        num_rows (int): The number of rows in the input matrix
        num_cols (int): The number of columns in the input matrix
    
    Returns:
        converted (numpy.ndarray): The output array in zigzag order (if direction=1) or the output matrix of 8x8 blocks (if direction=-1)
    """
    if direction == 1:
        # Subtract subsequent DC coefficients with the first DC coefficient of image
        # Transform blocks into zigzag fashion
        for i in range(0, num_rows, 8):
            for j in range(0, num_cols, 8):
                if i == 0 and j == 0:
                    continue
                matrix[i:i+8, j:j+8] -= matrix[0:8, 0:8]
        
        converted = np.zeros((num_rows * num_cols // 64, 64))
        x = 0
        for i in range(0, num_rows, 8):
            for j in range(0, num_cols, 8):
                x += 1
                block = matrix[i:i+8, j:j+8]
                converted[x,:] = [block[0,0], block[0,1], block[1,0], block[2,0], block[1,1], block[0,2], block[0,3], block[1,2], block[2,1], block[3,0], block[4,0], block[3,1], block[2,2], block[1,3], block[0,4], block[0,5], block[1,4], block[2,3], block[3,2], block[4,1], block[5,0], block[6,0], block[5,1], block[4,2], block[3,3], block[2,4], block[1,5], block[0,6], block[0,7], block[1,6], block[2,5], block[3,4], block[4,3], block[5,2], block[6,1], block[7,0], block[7,1], block[6,2], block[5,3], block[4,4], block[3,5], block[2,6], block[1,7], block[2,7], block[3,6], block[4,5], block[5,4], block[6,3], block[7,2], block[7,3], block[6,4], block[5,5], block[4,6], block[3,7], block[4,7], block[5,6], block[6,5], block[7,4], block[7,5], block[6,6], block[5,7], block[6,7], block[7,6], block[7,7]]
    
    else:
        k = 0
        converted = np.zeros((num_rows, num_cols))
        for i in range(0, num_rows, 8):
            for j in range(0, num_cols, 8):
                block_1d = np.array([matrix[k,:]])
                block_2d = np.array([[block_1d[0], block_1d[1], block_1d[5], block_1d[6], block_1d[14], block_1d[15], block_1d[27], block_1d[28]],
                              [block_1d[2], block_1d[4], block_1d[7], block_1d[13], block_1d[16], block_1d[26], block_1d[29], block_1d[42]],
                              [block_1d[3], block_1d[8], block_1d[12], block_1d[17], block_1d[25], block_1d[30], block_1d[41], block_1d[43]],
                              [block_1d[9], block_1d[11], block_1d[18], block_1d[24], block_1d[31], block_1d[40], block_1d[44], block_1d[53]],
                              [block_1d[10], block_1d[19], block_1d[23], block_1d[32], block_1d[39], block_1d[45], block_1d[52], block_1d[54]],
                              [block_1d[20], block_1d[22], block_1d[33], block_1d[38], block_1d[46], block_1d[51], block_1d[55], block_1d[60]],
                              [block_1d[21], block_1d[34], block_1d[37], block_1d[47], block_1d[50], block_1d[56], block_1d[59], block_1d[61]],
                              [block_1d[35], block_1d[36], block_1d[48], block_1d[49], block_1d[57], block_1d[58], block_1d[62], block_1d[63]]])
                converted[i:i+8, j:j+8] = block_2d
                k += 1
        
        for i in range(0, num_rows, 8):
            for j in range(0, num_cols, 8):
                if i == 0 and j == 0:
                    continue
                converted[i:i+8, j:j+8] += converted[0:8, 0:8]
    
    return converted