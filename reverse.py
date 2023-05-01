def count_digits(number):
    """
    Counts the number of digits in an integer number
    
    Parameters:
        number (int): The integer to count the digits of
    
    Returns:
        digit_count (int): The number of digits in number
    """
    digit_count = 0
    while number > 0:
        digit_count += 1
        number //= 10
    return digit_count