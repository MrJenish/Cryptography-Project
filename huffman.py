import math

matrix_A = [[3, 0, 0, 0, 0, 0, 0, -5],
            [0, 10, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

zigzag_list = [matrix_A[0][0], matrix_A[0][1], matrix_A[1][0], matrix_A[2][0], matrix_A[1][1], matrix_A[0][2], matrix_A[0][3], matrix_A[1][2], matrix_A[2][1], matrix_A[3][0], matrix_A[4][0], matrix_A[3][1], matrix_A[2][2], matrix_A[1][3], matrix_A[0][4], matrix_A[0][5], matrix_A[1][4], matrix_A[2][3], matrix_A[3][2], matrix_A[4][1], matrix_A[5][0], matrix_A[6][0], matrix_A[5][1], matrix_A[4][2], matrix_A[3][3], matrix_A[2][4], matrix_A[1][5], matrix_A[0][6], matrix_A[0][7], matrix_A[1][6], matrix_A[2][5], matrix_A[3]
           [4], matrix_A[4][3], matrix_A[5][2], matrix_A[6][1], matrix_A[7][0], matrix_A[7][1], matrix_A[6][2], matrix_A[5][3], matrix_A[4][4], matrix_A[3][5], matrix_A[2][6], matrix_A[1][7], matrix_A[2][7], matrix_A[3][6], matrix_A[4][5], matrix_A[5][4], matrix_A[6][3], matrix_A[7][2], matrix_A[7][3], matrix_A[6][4], matrix_A[5][5], matrix_A[4][6], matrix_A[3][7], matrix_A[4][7], matrix_A[5][6], matrix_A[6][5], matrix_A[7][4], matrix_A[7][5], matrix_A[6][6], matrix_A[5][7], matrix_A[6][7], matrix_A[7][6], matrix_A[7][7]]

# Create a dictionary that maps the index of each non-zero element in zigzag_list to its value
nonzero_dict = {i: zigzag_list[i] for i in range(len(zigzag_list)) if zigzag_list[i] != 0}

# Get the dimensions of the original matrix
num_rows = len(matrix_A)
num_cols = len(matrix_A[0])

# Create a new matrix of zeros with the same dimensions as the original matrix
matrix_B = [[0 for j in range(num_cols)] for i in range(num_rows)]

# Iterate over the dictionary and assign the non-zero values to their corresponding positions in the new matrix
for i in range(num_rows):
    for j in range(num_cols):
        index = i*num_cols + j
        if index in nonzero_dict:
            matrix_B[i][j] = nonzero_dict[index]

# Print the new matrix
for row in matrix_B:
    print(row)