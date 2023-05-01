def dec_to_bin(k):
    """
    Converts a non-negative decimal integer k to its binary representation.
    """
    if k == 0:
        return '0b0'
    else:
        binary = ""
        while k > 0:
            binary = str(k % 2) + binary
            k //= 2
        return '0b' + binary