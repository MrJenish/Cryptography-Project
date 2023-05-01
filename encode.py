def encode(zigzag_list, encoded_list):
    # Get the number of rows and columns in the zigzag_list
    num_rows, num_cols = get_num_rows_and_cols(zigzag_list[0])
    
    # Calculate the value of k based on the number of rows
    k = 0
    for i in range(1, num_rows+1):
        k += 2**i
    
    # Convert k and num_cols to binary and insert them into the encoded_list
    k_binary = decimal_to_binary(k)
    num_cols_binary = decimal_to_binary(num_cols)
    encoded_list = insert_into_array(encoded_list, k_binary, -1, 1)
    encoded_list = insert_into_array(encoded_list, num_cols_binary, num_rows, 1)
    
    # Count the number of consecutive zeroes in the zigzag_list
    num_zeroes = 0
    for i in range(1, len(zigzag_list)):
        if zigzag_list[i] == 0:
            num_zeroes += 1
        else:
            # Get the row and column of the non-zero value and encode them
            row, col = get_row_and_col(zigzag_list[i])
            if num_zeroes < 16:
                encoded_list = insert_into_array(encoded_list, encode_row_zeroes(row, num_zeroes), -1, 2)
                encoded_list = insert_into_array(encoded_list, decimal_to_binary(col), row, 2)
            else:
                # If there are more than 15 consecutive zeroes, split them into multiple codes
                for j in range(1, num_zeroes//15 + 1):
                    encoded_list = insert_into_array(encoded_list, 11111111001, -1, 2)
                num_zeroes -= (num_zeroes//15)*15
                encoded_list = insert_into_array(encoded_list, encode_row_zeroes(row, num_zeroes), -1, 2)
                encoded_list = insert_into_array(encoded_list, decimal_to_binary(col), row, 2)
            num_zeroes = 0
    
    # If there are remaining zeroes, encode them
    if num_zeroes != 0:
        encoded_list = insert_into_array(encoded_list, 1010, -1, 2)
    
    return encoded_list