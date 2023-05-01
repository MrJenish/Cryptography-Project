def count_digits(num):
    """
    Counts the number of digits in a non-negative integer.

    Parameters:
        num (int): The integer to count the digits of.

    Returns:
        count (int): The number of digits in the integer.
    """
    if num == 0:
        return 1
    else:
        digit_count = 0
        while num > 0:
            digit_count += 1
            num //= 10
        return digit_count