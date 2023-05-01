def bin_to_dec(binary):
    """
    Converts a binary number to a decimal number
    
    Parameters:
        binary (int): The binary number to convert
        
    Returns:
        dec (int): The decimal equivalent of the binary number
    """
    decimal = 0
    power = 0
    while binary > 0:
        remainder = binary % 10
        decimal += remainder * 2 ** power
        binary //= 10
        power += 1
    return decimal