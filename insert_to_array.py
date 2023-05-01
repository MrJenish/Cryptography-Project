def insert_value(arr, value, index, coeff_type):
    """
    Inserts a value into an array arr based on the parameters value, index, and coeff_type
    
    Parameters:
        arr (list): The array to insert the value into
        value (int): The value to insert
        index (int): The row or column index to insert the value into (depending on coeff_type)
        coeff_type (int): The type of coefficient (1 for DC, 2 for AC)
    
    Returns:
        arr (list): The updated array
    """
    length = len(arr)
    if coeff_type == 1:  # DC coefficient encoding
        if index == -1:
            if value == 0:
                arr.append(0)
            else:
                length += count_digits(value)
        else:
            if index > 0:
                if value == 0:
                    arr[length + index - 1] = 0
                else:
                    length += index
            else:
                arr.append(0)
    if coeff_type == 2:  # AC coefficient encoding
        if index == -1:
            if value == 0:
                arr.extend([0, 0])
            elif value == 1:
                arr.append(0)
                length += count_digits(value)
            else:
                length += count_digits(value)
        else:
            if value == 0:
                arr[length + index - 1] = 0
            else:
                length += index
    while value > 0:
        arr[length - 1] = value % 10
        value //= 10
        length -= 1
    return arr