def check_coef(bits, coef_type):
    """
    Checks the coefficient of the compressed data.

    Parameters:
        bits (list): A list of binary digits representing the coefficient.
        coef_type (int): The type of the coefficient.

    Returns:
        row (int): The row number of the coefficient in the coefficient table.
        zeros (int): The number of zeroes preceding the coefficient.
    """
    coeff_table = [
        [0b00, 0b01, 0b100, 0b1011, 0b11010, 0b1111000, 0b11111000, 0b1111110110, 0b1111111110000010, 0b1111111110000011],
        [0b1100, 0b11011, 0b1111001, 0b111110110, 0b11111110110, 0b1111111110000100, 0b1111111110000101, 0b1111111110000110, 0b1111111110000111, 0b1111111110001000],
        [0b11100, 0b11111001, 0b1111110111, 0b111111110100, 0b1111111110001001, 0b1111111110001010, 0b1111111110001011, 0b1111111110001100, 0b1111111110001101, 0b1111111110001110],
        [0b111010, 0b111110111, 0b111111110101, 0b1111111110001111, 0b1111111110010000, 0b1111111110010001, 0b1111111110010010, 0b1111111110010011, 0b1111111110010100, 0b1111111110010101],
        [0b111011, 0b1111111000, 0b1111111110010110, 0b1111111110010111, 0b1111111110011000, 0b1111111110011001, 0b1111111110011010, 0b1111111110011011, 0b1111111110011100, 0b1111111110011101],
        [0b1111010, 0b11111110111, 0b1111111110011110, 0b1111111110011111, 0b1111111110100000, 0b1111111110100001, 0b1111111110100010, 0b1111111110100011, 0b1111111110100100, 0b1111111110100101],
        [0b1111011, 0b111111110110, 0b1111111110100110, 0b1111111110100111, 0b1111111110101000, 0b1111111110101001, 0b1111111110101010, 0b1111111110101011, 0b1111111110101100, 0b1111111110101101],
        [0b11111010, 0b111111110111, 0b1111111110101110, 0b1111111110101111, 0b1111111110110000, 0b1111111110110001, 0b1111111110110010, 0b1111111110110011, 0b1111111110110100, 0b1111111110110101],
        [0b111111000, 0b111111111000000, 0b1111111110110110, 0b1111111110110111, 0b1111111110111000, 0b1111111110111001, 0b1111111110111010, 0b1111111110111011, 0b1111111110111100, 0b1111111110111101],
        [0b111111001, 0b1111111110111110, 0b1111111110111111, 0b1111111111000000, 0b1111111111000001, 0b1111111111000010, 0b1111111111000011, 0b1111111111000100, 0b1111111111000101, 0b1111111111000110],
        [0b111111010, 0b1111111111000111, 0b1111111111001000, 0b1111111111001001, 0b1111111111001010, 0b1111111111001011, 0b1111111111001100, 0b1111111111001101, 0b1111111111001110, 0b1111111111001111],
        [0b1111111001, 0b1111111111010000, 0b1111111111010001, 0b1111111111010010, 0b1111111111010011, 0b1111111111010100, 0b1111111111010101, 0b1111111111010110, 0b1111111111010111, 0b1111111111011000],
        [0b1111111010, 0b1111111111011001, 0b1111111111011010, 0b1111111111011011, 0b1111111111011100, 0b1111111111011101, 0b1111111111011110, 0b1111111111011111, 0b1111111111100000, 0b1111111111100001],
        [0b11111111000, 0b1111111111100010, 0b1111111111100011, 0b1111111111100100, 0b1111111111100101, 0b1111111111100110, 0b1111111111100111, 0b1111111111101000, 0b1111111111101001, 0b1111111111101010],
        [0b1111111111101011, 0b1111111111101100, 0b1111111111101101, 0b1111111111101110, 0b1111111111101111, 0b1111111111110000, 0b1111111111110001, 0b1111111111110010, 0b1111111111110011, 0b1111111111110100],
        [0b1111111111110101, 0b1111111111110110, 0b1111111111110111, 0b1111111111111000, 0b1111111111111001, 0b1111111111111010, 0b1111111111111011, 0b1111111111111100, 0b1111111111111101, 0b1111111111111110]
    ]

    if coef_type == 0:
        zeros = int(bits[1:], 2)
        row = 0
    else:
        n = len(bits)
        for i in range(n):
            if int(bits[:i+1], 2) == coeff_table[coef_type-1][i]:
                row = i
        zeros = n-row-1

    return row, zeros