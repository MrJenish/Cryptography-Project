def decode_binary_sequence(binary_seq, decoded_seq, start_index, prev_row_count):
    """
    Decodes a binary sequence into a non-negative integer sequence using a custom algorithm.

    Parameters:
        binary_seq (list): A list of binary digits representing the input binary sequence.
        decoded_seq (list): An empty list to store the decoded integer sequence.
        start_index (int): The starting index of the binary sequence to decode.
        prev_row_count (int): The number of rows of the previously decoded coefficient table.

    Returns:
        end_index (int): The ending index of the binary sequence that was decoded.
    """
    seq_len = len(binary_seq)
    i = start_index
    while i < seq_len:
        row_no, zeroes = check_coeff(binary_seq[i:], 0)
        if row_no != -1:
            col_no = 0
            k = 0
            temp = binary_seq[i+row_no+1:i+2*row_no+1]
            for j in range(row_no):
                col_no += temp[row_no-j-1] * 2**j
            if col_no < 2**(row_no-1):
                decoded_seq[prev_row_count].append(col_no)
            else:
                decoded_seq[prev_row_count].append(col_no - 2**row_no)
            i += 2*row_no+1
            continue

        row_no, zeroes = check_coeff(binary_seq[i:], 1)
        if row_no != -1:
            col_no = 0
            k = 0
            temp = binary_seq[i+row_no+1:i+2*row_no+1]
            for j in range(row_no):
                col_no += temp[row_no-j-1] * 2**j
            if col_no < 2**(row_no-1):
                decoded_seq[prev_row_count].append(col_no)
            else:
                decoded_seq[prev_row_count].append(col_no - 2**row_no)
            i += 2*row_no+1+zeroes
            continue

        if binary_seq[i:i+11] == [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]:
            decoded_seq[prev_row_count].extend([0]*15)
            i += 11
            continue

        if binary_seq[i:i+4] == [1, 0, 1, 0]:
            decoded_seq[prev_row_count].append(0)
            start_index = i+4
            break

    return start_index